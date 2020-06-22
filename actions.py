from typing import Dict, Text, Any, List, Union, Optional

from rasa_sdk import Tracker, Action
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction

from api.WienerLinienAPI import validate_station_name, StationNameValidationResult, lookup_routes
from api.model.api_types import JourneyStop, Route, MeansOfTransportType, create_journey_stop_from_json
from ticket_calculator.ticket import find_best_tickets_for_journey, TicketDistributionChannel, Ticket
from datetime import datetime, timedelta
import re


DATE_TIME_FORMAT_STRING = '%Y-%m-%dT%H:%M:%S.%f%z'

AIRPORT_STATION_NAME = 'Flughafen Wien'


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
        value: Union[Text, List[Text]],
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        if isinstance(value, list):
            departure_station_name = _validate_single_departure_station(
                value[0], dispatcher, tracker, domain
            )
            arrival_station_name = _validate_single_arrival_station(
                value[1], dispatcher, tracker, domain
            )
            if departure_station_name is not None and arrival_station_name is not None:
                return {
                    'departure_station': departure_station_name,
                    'arrival_station': arrival_station_name,
                }
            else:
                return {'departure_station': None, 'arrival_station': None}
        else:
            departure_station_name = _validate_single_departure_station(
                value, dispatcher, tracker, domain
            )
            if departure_station_name is not None:
                return {'departure_station': departure_station_name}
            else:
                return {'departure_station': None, 'arrival_station': None}

    def validate_arrival_station(
        self,
        value: Union[Text, List[Text]],
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        if isinstance(value, list):
            arrival_station_name = _validate_single_arrival_station(
                value[1], dispatcher, tracker, domain
            )
            departure_station_name = _validate_single_departure_station(
                value[0], dispatcher, tracker, domain
            )
            if departure_station_name is not None and arrival_station_name is not None:
                return {
                    'arrival_station': arrival_station_name,
                    'departure_station': departure_station_name,
                }
            else:
                return {'departure_station': None, 'arrival_station': None}
        else:
            arrival_station_name = _validate_single_arrival_station(
                value, dispatcher, tracker, domain
            )
            return {'arrival_station': arrival_station_name}

    def validate_departure_date_time(
        self,
        value: Union[Text, Dict[Text, Text]],
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ):
        if type(value) == str:
            return {'departure_date_time': value}
        elif type(value) == dict:
            return {'departure_date_time': value['from']}
        else:
            return {'departure_date_time': None}

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]
    ):
        dispatcher.utter_message(template='utter_lookup_single_connection_form')
        return []


def _validate_single_departure_station(
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


def _validate_single_arrival_station(
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


class ActionLookupSingleConnection(Action):
    def name(self) -> Text:
        return 'action_lookup_single_connection'

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        departure_date_time = datetime.strptime(
            tracker.get_slot('departure_date_time'),
            DATE_TIME_FORMAT_STRING
        )
        routes = lookup_routes(
            tracker.get_slot('departure_station'),
            tracker.get_slot('arrival_station'),
            departure_date_time
        )
        if len(routes) > 0:
            dispatcher.utter_message(f'Ich habe die folgenden Verbindungen von {routes[0].departure_station} nach {routes[0].arrival_station} gefunden:')
            # see https://github.com/RasaHQ/rasa/issues/4461
            dispatcher.utter_message(json_message={
                'text': _convert_routes_to_markdown(routes),
                'parse_mode': 'MarkdownV2'
            })
        else:
            dispatcher.utter_message('Leider konnte ich keine Routen zwischen den von dir genannten Stationen finden. Versuche es bitte mit einer neuen Anfrage.')
        return [
            SlotSet('departure_station', None),
            SlotSet('arrival_station', None),
            SlotSet('departure_date_time', None),
        ]


def _convert_routes_to_markdown(routes: List[Route]) -> Text:
    markdown_representation = ''
    for route_index, route in enumerate(routes):
        markdown_representation += f'*Verbindung {str(route_index + 1)}:*\n'
        for partial_route_index, partial_route in enumerate(route.partial_routes):
            if partial_route.means_of_transport.means_of_transport_type != MeansOfTransportType.WALK:
                markdown_representation += f'{str(partial_route_index + 1)}. {partial_route.means_of_transport.product_name} __{partial_route.means_of_transport.short_name}__ '
                markdown_representation += f'von __{partial_route.departure_station}__ (Abfahrtszeit __{_format_time(partial_route.departure_time)}__)'
                markdown_representation += f' nach __{partial_route.arrival_station}__ (Ankunftszeit __{_format_time(partial_route.arrival_time)}__)'
                markdown_representation += f' Richtung {partial_route.means_of_transport.destination}\n'
            else:
                markdown_representation += f'{str(partial_route_index + 1)}. Fußweg nach {partial_route.arrival_station}, '
                markdown_representation += f'Losgehzeit __{_format_time(partial_route.departure_time)}__, '
                markdown_representation += f'Ankunftszeit __{_format_time(partial_route.arrival_time)}__'
        markdown_representation += '\n'

    return _normalize_markdown(markdown_representation)


def _normalize_markdown(markdown_representation: Text) -> Text:
    return re.sub(
        r'(\[|\]|\(|\)|~|`|>|#|\+|-|=|\||\{|\}|\.|!)',
        _replace_special_character,
        markdown_representation
    )


def _replace_special_character(match_object):
    return '\\' + match_object.group(0)


def _format_time(date_time: datetime) -> Text:
    return date_time.strftime('%H:%M')

class JourneyDetailsForm(FormAction):

    def name(self):
        return 'journey_details_form'

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return [
            'arrival_date',
            'first_station',
        ]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {
            'arrival_date': [self.from_entity(entity='time')],
            'first_station': [self.from_entity(
                entity='station',
                intent=['select_arrival_station']
            )],
        }

    def validate_first_station(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ):
        dispatcher.utter_message('Ich überprüfe schnell die von dir angegebene Station.')
        (validation_result, first_station_name) = validate_station_name(
            value,
            ['Wien', 'Schwechat']
        )
        if validation_result == StationNameValidationResult.EXACT_MATCH:
            return {'first_station': first_station_name}
        elif validation_result == StationNameValidationResult.LIST_OF_CANDIDATES:
            dispatcher.utter_message('Für die von dir gewählte Station habe ich direkten Treffer, aber mehrere mögliche gefunden. Du musst die Abfrage leider noch einmal eingeben, da ich mir nicht sicher sein kann, welche Station gemeint ist. Die möglichen Treffer lauten: ' + (', '.join(first_station_name)))
            return {'first_station': None}
        elif validation_result == StationNameValidationResult.NO_MATCH:
            dispatcher.utter_message('Leider konnte ich für die von dir gewählte Abfahrtsstation keinen Treffer finden.')
            return {'first_station': None}

    def validate_arrival_date(
        self,
        value: Union[Text, Dict[Text, Text]],
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ):
        if type(value) == str:
            return {'arrival_date': value}
        elif type(value) == dict:
            return {'arrival_date': value['from']}
        else:
            return {'arrival_date': None}

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]
    ):
        return []


class ActionInitializeJourneyPlanning(Action):
    def name(self) -> Text:
        return 'action_initialize_journey_planning'

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        return [
            SlotSet('previous_arrival_station', tracker.get_slot('first_station')),
            SlotSet('journey_current_date', tracker.get_slot('arrival_date')),
            SlotSet('journey_routes', [])
        ]


class JourneyAddRouteForm(FormAction):
    def name(self):
        return 'journey_add_route_form'

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return [
            'journey_route_departure_station',
            'journey_route_arrival_station',
            'journey_route_departure_date_time',
        ]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {
            'journey_route_departure_station': [self.from_entity(
                entity='station',
                role='departure',
                intent=[
                    'specify_departure_and_arrival_station',
                ]
            )],
            'journey_route_arrival_station': [self.from_entity(
                entity='station',
                role='arrival',
            )],
            'journey_route_departure_date_time': [self.from_entity(entity='time')],
        }

    def validate_journey_route_departure_station(
        self,
        value: Union[Text, List[Text]],
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        if isinstance(value, list):
            departure_station_name = _validate_single_departure_station(
                value[0], dispatcher, tracker, domain
            )
            arrival_station_name = _validate_single_arrival_station(
                value[1], dispatcher, tracker, domain
            )
            if departure_station_name is not None and arrival_station_name is not None:
                return {
                    'journey_route_departure_station': departure_station_name,
                    'journey_route_arrival_station': arrival_station_name,
                }
            else:
                return {'journey_route_departure_station': None, 'journey_route_arrival_station': None}
        else:
            departure_station_name = _validate_single_departure_station(
                value, dispatcher, tracker, domain
            )
            if departure_station_name is not None:
                return {'journey_route_departure_station': departure_station_name}
            else:
                return {'journey_route_departure_station': None, 'journey_route_arrival_station': None}

    def validate_journey_route_arrival_station(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ):
        if tracker.get_slot('journey_route_arrival_station') is not None:
            return {'journey_route_arrival_station': tracker.get_slot('journey_route_arrival_station')}
        if isinstance(value, list):
            arrival_station_name = _validate_single_arrival_station(
                value[1], dispatcher, tracker, domain
            )
            departure_station_name = _validate_single_departure_station(
                value[0], dispatcher, tracker, domain
            )
            if departure_station_name is not None and arrival_station_name is not None:
                return {
                    'journey_route_arrival_station': arrival_station_name,
                    'journey_route_departure_station': departure_station_name,
                }
            else:
                return {'journey_route_departure_station': None, 'journey_route_arrival_station': None}
        else:
            arrival_station_name = _validate_single_arrival_station(
                value, dispatcher, tracker, domain
            )
            departure_station_name = tracker.get_slot('journey_route_departure_station')
            if departure_station_name is None:
                print('Using previous arrival station as departure station.')
                return {
                    'journey_route_arrival_station': arrival_station_name,
                    'journey_route_departure_station': tracker.get_slot('previous_arrival_station')
                }
            else:
                print(f'Using entered departure station {departure_station_name} as departure station.')
                return {'journey_route_arrival_station': arrival_station_name}

    def validate_journey_route_departure_date_time(
        self,
        value: Union[Text, Dict[Text, Text]],
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ):
        if type(value) == str:
            return {'journey_route_departure_date_time': value}
        elif type(value) == dict:
            return {'journey_route_departure_date_time': value['from']}
        else:
            return {'journey_route_departure_date_time': None}

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]
    ):
        dispatcher.utter_message(f'Ich suche dir schnell eine Verbindung zwischen {tracker.get_slot("journey_route_departure_station")} und {tracker.get_slot("journey_route_arrival_station")}')
        return []


class ActionAddJourneyRoute(Action):
    def name(self):
        return 'action_add_journey_route'

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        departure_date_time = datetime.strptime(
            tracker.get_slot('journey_route_departure_date_time'),
            DATE_TIME_FORMAT_STRING
        )
        journey_current_date = datetime.strptime(
            tracker.get_slot('journey_current_date'),
            DATE_TIME_FORMAT_STRING
        )
        departure_date_time = departure_date_time.replace(
            year=journey_current_date.year,
            month=journey_current_date.month,
            day=journey_current_date.day,
        )
        departure_station = tracker.get_slot('journey_route_departure_station')
        arrival_station = tracker.get_slot('journey_route_arrival_station')
        routes = lookup_routes(departure_station, arrival_station, departure_date_time)
        if len(routes) > 0:
            dispatcher.utter_message(f'Super, ich habe mindestens eine Verbindung von {routes[0].departure_station} nach {routes[0].arrival_station} gefunden und sie in die Reiseplanung miteinbezogen.')
            journey_routes = tracker.get_slot('journey_routes')
            journey_stop = JourneyStop(departure_station, arrival_station, departure_date_time, routes)
            journey_routes.append(journey_stop.to_serializable())
            return [
                SlotSet('previous_arrival_station', tracker.get_slot('journey_route_arrival_station')),
                SlotSet('journey_routes', journey_routes),
                SlotSet('journey_route_departure_station', None),
                SlotSet('journey_route_arrival_station', None),
                SlotSet('journey_route_departure_date_time', None),
            ]
        else:
            dispatcher.utter_message('Leider konnte ich keine Routen zwischen den von dir genannten Stationen finden. Versuche es bitte mit einer neuen Anfrage.')
            return [
                SlotSet('journey_route_departure_station', None),
                SlotSet('journey_route_arrival_station', None),
                SlotSet('journey_route_departure_date_time', None),
            ]


class ActionWaitForNextDay(Action):
    def name(self):
        return 'action_wait_for_next_day'

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        journey_current_date = datetime.strptime(
            tracker.get_slot('journey_current_date'),
            DATE_TIME_FORMAT_STRING
        )
        journey_current_date = journey_current_date + timedelta(days = 1)

        dispatcher.utter_message(f'Der aktuelle Tag auf den sich die Zeitangaben beziehen ist der {_format_date(journey_current_date)}')
        return [
            SlotSet('journey_current_date', _format_date_time(journey_current_date))
        ]


def _format_date_time(date_time: datetime) -> str:
    return date_time.strftime(DATE_TIME_FORMAT_STRING)


class ActionFinishJourneyPlanning(Action):
    def name(self):
        return 'action_finish_journey_planning'

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        journey_stops = tracker.get_slot('journey_routes')
        journey_stops = [create_journey_stop_from_json(stop) for stop in journey_stops]

        dispatcher.utter_message('Vielen Dank, dass du mir vertraust :) Ich habe die folgende Routenplanung für dich zusammengestellt:')
        for stop in journey_stops:
            route_display_text = _normalize_markdown(f'Für die Verbindung von {stop.departure_station} nach {stop.arrival_station} am {_format_date(stop.desired_date_time)} um {_format_time(stop.desired_date_time)} habe ich die folgenden Verbindungen gefunden:\n')
            route_display_text += _convert_routes_to_markdown(stop.routes)
            dispatcher.utter_message(json_message={
                'text': route_display_text,
                'parse_mode': 'MarkdownV2'
            })

        optimal_tickets = find_best_tickets_for_journey(journey_stops)
        if len(optimal_tickets) == 1:
            dispatcher.utter_message(f'Ich würde dir das folgende Ticket für deine Reise empfehlen: {optimal_tickets[0].name} zum Preis von €{optimal_tickets[0].price}')
        else:
            ticket_message = 'Ich würde dir die folgenden Tickets für deine Reise empfehlen:\n'
            for ticket in optimal_tickets:
                ticket_message += f'- {ticket.name} zum Preis von €{ticket.price}\n'
            dispatcher.utter_message(ticket_message)

        dispatcher.utter_message(json_message = {
            'text': _get_ticket_purchase_instructions(
                optimal_tickets,
                tracker.get_slot('first_station')
            ),
            'parse_mode': 'MarkdownV2'
        })

        return [
            SlotSet('first_station', None),
            SlotSet('arrival_date', None),
            SlotSet('previous_arrival_station', None),
            SlotSet('journey_current_date', None),
            SlotSet('journey_routes', None),
        ]


def _format_date(date_time: datetime) -> Text:
    return date_time.strftime('%d.%m')


def _get_ticket_purchase_instructions(optimal_tickets: List[Ticket], first_station: Text) -> Text:
    message = 'Du kannst die Tickets über die folgenden Vertriebswege kaufen:\n\n'
    if len(optimal_tickets) > 0:
        message += 'Alle Tickets erhältst du komfortabl über die [Wien-Mobil-Anwendung für Android](https://play.google.com/store/apps/details?id=at.wienerlinien.wienmobillab&hl=de_AT) oder die [Wien-Mobil-Anwendung für iOS](https://itunes.apple.com/at/app/wienmobil/id1107918142?mt=8)\n\n'
    for (index, ticket) in enumerate(optimal_tickets):
        message += f'Das Ticket *{ticket.name}* kannst du über die folgenden Vertriebskanäle kaufen:\n'
        if TicketDistributionChannel.ONLINE in ticket.distribution_channels:
            message += f'[Online über den Wiener-Linien-Ticketshop]({ticket.online_shop_url})\n'
        if TicketDistributionChannel.VENDING_MACHINE in ticket.distribution_channels:
            message += f'Am Fahrkartenautomaten an der Haltestelle\n'
        if TicketDistributionChannel.CORNER_SHOP in ticket.distribution_channels:
            message += f'An einer der Wiener Trafiken\n'
        if TicketDistributionChannel.TICKET_COUNTER in ticket.distribution_channels:
            message += f'[An einem Ticketschalter der Wiener Linien](https://www.wienerlinien.at/eportal3/ep/channelView.do?channelId=-46621&programId=66610#66609)\n'

        if index == 0 and first_station == AIRPORT_STATION_NAME:
            message += '*Wichtig*: Da du am Flughafen ankommst buche für dieses Ticket bitte die Option *Flughafentransfer* dazu, damit du weiter sparen kannst.'

        message += '\n'
    return _normalize_markdown_with_links(message)


def _normalize_markdown_with_links(markdown_representation: Text) -> Text:
    return re.sub(
        r'(/|~|`|>|#|\+|-|=|\||\{|\}|\.|!)',
        _replace_special_character,
        markdown_representation
    )
