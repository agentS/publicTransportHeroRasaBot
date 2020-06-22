from typing import Any, Dict, List, Text, Optional, Tuple, Union
from enum import Enum, auto, unique

from api.model.api_types import JourneyStop
from datetime import datetime, timedelta


@unique
class TicketKind(Enum):
    RIDE_CONSTRAINED = auto()
    HOUR_CONSTRAINED = auto()
    DAY_CONSTRAINED = auto()
    WEEK_CONSTRAINED = auto()


@unique
class TicketDistributionChannel(Enum):
    ONLINE = auto()
    MOBILE_APPLICATION = auto()
    VENDING_MACHINE = auto()
    CORNER_SHOP = auto()
    TICKET_COUNTER = auto()


class Ticket():
    def __init__(
        self,
        name: Text,
        kind: TicketKind,
        validity_duration: int,
        price: float,
        distribution_channels: List[TicketDistributionChannel],
        online_shop_url: Optional[Text]
    ):
        self.name = name
        self.kind = kind
        self.validity_duration = validity_duration
        self.price = price
        self.distribution_channels = distribution_channels
        self.online_shop_url = online_shop_url


TICKETS = {
    'single_ride': Ticket('1 Fahrt WIEN', TicketKind.RIDE_CONSTRAINED, 1, 2.40, [TicketDistributionChannel.ONLINE, TicketDistributionChannel.MOBILE_APPLICATION, TicketDistributionChannel.VENDING_MACHINE, TicketDistributionChannel.CORNER_SHOP, TicketDistributionChannel.TICKET_COUNTER], 'https://shop.wienerlinien.at/product/35/show'),
    'one_day': Ticket('1 Tag WIEN', TicketKind.DAY_CONSTRAINED, 1, 5.80, [TicketDistributionChannel.ONLINE, TicketDistributionChannel.MOBILE_APPLICATION, TicketDistributionChannel.TICKET_COUNTER], 'https://shop.wienerlinien.at/product/694/show'),
    'twentyfour_hours': Ticket('24 Stunden WIEN', TicketKind.HOUR_CONSTRAINED, 24, 8.00, [TicketDistributionChannel.ONLINE, TicketDistributionChannel.MOBILE_APPLICATION, TicketDistributionChannel.VENDING_MACHINE, TicketDistributionChannel.CORNER_SHOP, TicketDistributionChannel.TICKET_COUNTER], 'https://shop.wienerlinien.at/index.php/product/3/show/0/0/0/0'),
    'fortyeight_hours': Ticket('48 Stunden WIEN', TicketKind.HOUR_CONSTRAINED, 48, 14.10, [TicketDistributionChannel.ONLINE, TicketDistributionChannel.MOBILE_APPLICATION, TicketDistributionChannel.VENDING_MACHINE, TicketDistributionChannel.CORNER_SHOP, TicketDistributionChannel.TICKET_COUNTER], 'https://shop.wienerlinien.at/index.php/product/5/show/0/0/0/0/buy'),
    'seventytwo_hours': Ticket('72 Stunden WIEN', TicketKind.HOUR_CONSTRAINED, 72, 17.10, [TicketDistributionChannel.ONLINE, TicketDistributionChannel.MOBILE_APPLICATION, TicketDistributionChannel.VENDING_MACHINE, TicketDistributionChannel.CORNER_SHOP, TicketDistributionChannel.TICKET_COUNTER], 'https://shop.wienerlinien.at/index.php/product/6/show/0/0/0/0/buy'),
    'one_week': Ticket('Wochenkarte', TicketKind.WEEK_CONSTRAINED, 7, 17.10, [TicketDistributionChannel.ONLINE, TicketDistributionChannel.MOBILE_APPLICATION, TicketDistributionChannel.VENDING_MACHINE, TicketDistributionChannel.CORNER_SHOP, TicketDistributionChannel.TICKET_COUNTER], 'https://shop.wienerlinien.at/index.php/product/7/show/0/0/0/0'),
}
HOUR_CONSTRAINED_TICKETS = [
    TICKETS['twentyfour_hours'],
    TICKETS['fortyeight_hours'],
    TICKETS['seventytwo_hours'],
]


def find_best_tickets_for_journey(journey_stops: List[JourneyStop]) -> List[Ticket]:
    tickets = []

    price_single_rides = _calculate_price_single_rides(journey_stops)
    best_spanning_tickets = _find_best_spanning_tickets(journey_stops)
    price_best_spanning_tickets = 0.0
    for ticket in best_spanning_tickets:
        price_best_spanning_tickets = price_best_spanning_tickets + ticket.price

    if price_single_rides < price_best_spanning_tickets:
        return [TICKETS['single_ride']] * len(journey_stops)
    else:
        return best_spanning_tickets


def _calculate_price_single_rides(journey_stops: List[JourneyStop]) -> float:
    number_of_stops = len(journey_stops)
    return number_of_stops * TICKETS['single_ride'].price


def _find_best_spanning_tickets(journey_stops: List[JourneyStop]) -> List[Ticket]:
    tickets = []
    desired_date_times = [stop.desired_date_time for stop in journey_stops]
    current_start_date_time = min(desired_date_times)
    last_date_time = max(desired_date_times)
    for ticket_count in range(0, 10):
        best_spanning_ticket = _find_best_spanning_ticket(current_start_date_time, last_date_time)
        if best_spanning_ticket is not None:
            tickets.append(best_spanning_ticket)
            break
        else:
            tickets.append(TICKETS['seventytwo_hours'])
            current_start_date_time = current_start_date_time + timedelta(days = 3)

    return tickets


def _find_best_spanning_ticket(start_date_time: datetime, last_date_time: datetime) -> Optional[Ticket]:
    delta = last_date_time - start_date_time
    if delta.days == 0 and start_date_time.day == last_date_time.day:
        return TICKETS['one_day']
    for hour_constrained_ticket in HOUR_CONSTRAINED_TICKETS:
        if delta.days < (hour_constrained_ticket.validity_duration / 24):
            return hour_constrained_ticket
    _, start_date_time_week, _ = start_date_time.isocalendar()
    _, last_date_time_week, _ = last_date_time.isocalendar()
    if delta.days <= TICKETS['one_week'].validity_duration and start_date_time_week == last_date_time_week:
        return TICKETS['one_week']

    return None
