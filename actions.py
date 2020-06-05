from typing import Dict, Text, Any, List, Union, Optional

from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction

from api.WienerLinienAPI import validate_station_name, StationNameValidationResult


class JourneyDetailsForm(FormAction):

    def name(self):
        return 'journey_details_form'

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ['arrival_date', 'first_station']

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {
            'arrival_date': [self.from_entity(entity='time')],
            'first_station': [self.from_entity(entity='station', intent=['select_first_station'])],
        }

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]
    ):
        dispatcher.utter_template('utter_submit_journey_details', tracker)
        return []


class SingleConnectionForm(FormAction):

    def name(self):
        return 'lookup_single_connection_form'

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ['departure_station', 'arrival_station', 'departure_date_time']

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {
            'departure_station': [self.from_entity(
                entity='station',
                role='departure',
                intent=['specify_departure_and_arrival_station']
            )],
            'arrival_station': [self.from_entity(
                entity='station',
                role='arrival',
                intent=['specify_departure_and_arrival_station']
            )],
            'departure_date_time': [self.from_entity(entity='time')],
        }

    def validate_departure_station(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        print(value)
        if isinstance(value, list):
            departure_station_name = self._validate_single_departure_station(
                value[0], dispatcher, tracker, domain
            )
            arrival_station_name = self._validate_single_arrival_station(
                value[1], dispatcher, tracker, domain
            )
            if departure_station_name is not None and arrival_station is not None:
                return {
                    'departure_station': departure_station_name,
                    'arrival_station': arrival_station_name
                }
            else:
                return {'departure_station': None, 'arrival_station': None}
        else:
            departure_station_name = self._validate_single_departure_station(
                value, dispatcher, tracker, domain
            )
            if departure_station_name is not None:
                return {'departure_station': departure_station_name}
            else:
                return {'departure_station': None, 'arrival_station': None}

    def _validate_single_departure_station(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Any:
        dispatcher.utter_message('Ich überprüfe schnell die von dir gewählte Abfahrtsstation.')

        (validation_result, matched_station_name) = validate_station_name(value)
        if validation_result == StationNameValidationResult.EXACT_MATCH:
            return value
        elif validation_result == StationNameValidationResult.LIST_OF_CANDIDATES:
            dispatcher.utter_message('Für die von dir gewählte Abfahrtsstation habe ich direkten Treffer, aber mehrere mögliche gefunden. Du musst die Abfrage leider noch einmal eingeben, da ich mir nicht sicher sein kann, welche Station gemeint ist. Die möglichen Treffer lauten: ' + (', '.join(matched_station_name)))
            return None
        elif validation_result == StationNameValidationResult.NO_MATCH:
            dispatcher.utter_message('Leider konnte ich für die von dir gewählte Abfahrtsstation keinen Treffer finden.')
            return None

    def validate_arrival_station(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        print('validating arrival station')
        print(value)
        arrival_station_name = self._validate_single_arrival_station(
            value, dispatcher, tracker, domain
        )
        return {'arrival_station': arrival_station_name}

    def _validate_single_arrival_station(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Any:
        dispatcher.utter_message('Ich überprüfe schnell die von dir gewählte Zielstation.')

        (validation_result, matched_station_name) = validate_station_name(value)
        if validation_result == StationNameValidationResult.EXACT_MATCH:
            return matched_station_name
        elif validation_result == StationNameValidationResult.LIST_OF_CANDIDATES:
            dispatcher.utter_message('Für die von dir gewählte Zielstation habe ich direkten Treffer, aber mehrere mögliche gefunden. Du musst die Abfrage leider noch einmal eingeben, da ich mir nicht sicher sein kann, welche Station gemeint ist. Die möglichen Treffer lauten: ' + (', '.join(matched_station_name)))
            return None
        elif validation_result == StationNameValidationResult.NO_MATCH:
            dispatcher.utter_message('Leider konnte ich für die von dir gewählte Zielstation keinen Treffer finden.')
            return None

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]
    ):
        dispatcher.utter_template('utter_lookup_single_connection_form', tracker)
        return []
