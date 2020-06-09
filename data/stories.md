## greet and ask for general help
* greet
  - utter_greet
  - utter_main_menu
* help
  - utter_help

## greet and lookup a single connection
* greet
  - utter_greet
  - utter_main_menu
* lookup_single_connection
  - utter_lookup_single_connection
  - lookup_single_connection_form
  - form{"name": "lookup_single_connection_form"}
  - form{"name": null}
  - action_lookup_single_connection

## greet, ask for help, and lookup a single connection
* greet
  - utter_greet
  - utter_main_menu
* help
  - utter_help
* lookup_single_connection
  - utter_lookup_single_connection
  - lookup_single_connection_form
  - form{"name": "lookup_single_connection_form"}
  - form{"name": null}
  - action_lookup_single_connection

## greet and start journey planning
* greet
  - utter_greet
  - utter_main_menu
* start_journey_planning
  - utter_start_journey_planning
  - journey_details_form
  - form{"name": "journey_details_form"}
  - form{"name": null}
  - utter_slots_values_journey_details

## greet, ask for help, and start journey planning
* greet
  - utter_greet
  - utter_main_menu
* help
  - utter_help
* start_journey_planning
  - utter_start_journey_planning
  - journey_details_form
  - form{"name": "journey_details_form"}
  - form{"name": null}
  - utter_slots_values_journey_details

## explain departure station single connection lookup
* lookup_single_connection
  - lookup_single_connection_form
  - form{"name": "lookup_single_connection_form"}
  - slot{"requested_slot": "departure_station"}
* explain
  - utter_explain_departure_station_to_arrival_station_single_connection_lookup
  - lookup_single_connection_form
  - form{"name": null}

## explain arrival station single connection lookup
* lookup_single_connection
  - lookup_single_connection_form
  - form{"name": "lookup_single_connection_form"}
  - slot{"requested_slot": "arrival_station"}
* explain
  - utter_explain_departure_station_to_arrival_station_single_connection_lookup
  - lookup_single_connection_form
  - form{"name": null}
  - action_lookup_single_connection

## explain departure date time single connection lookup
* lookup_single_connection
  - lookup_single_connection_form
  - form{"name": "lookup_single_connection_form"}
  - slot{"requested_slot": "departure_date_time"}
* explain
  - utter_explain_departure_date_time_connection_lookup
  - lookup_single_connection_form
  - form{"name": null}
  - action_lookup_single_connection
