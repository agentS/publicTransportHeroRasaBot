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
        dispatcher.utter_message('Ich überprüfe schnell die von dir gewählte Abfahrtsstation')

        (validation_result, matched_station_name) = validate_station_name(value)
        if validation_result == StationNameValidationResult.EXACT_MATCH:
            return {'departure_station': value}
        else:
            dispatcher.utter_message('Leider konnte ich für die von dir gewählte Abfahrtsstation keinen Treffer finden')
            return {'departure_station': None, 'arrival_station': None}

    def validate_arrival_station(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        dispatcher.utter_message('Ich überprüfe schnell die von dir gewählte Zielstation')

        (validation_result, matched_station_name) = validate_station_name(value)
        if validation_result == StationNameValidationResult.EXACT_MATCH:
            return {'arrival_station': value}
        else:
            dispatcher.utter_message('Leider konnte ich für die von dir gewählte Zielstation keinen Treffer finden')
            return {'arrival_station': None, 'departure_station': None}

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]
    ):
        dispatcher.utter_template('utter_lookup_single_connection_form', tracker)
        return []
