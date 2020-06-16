## start bot for first time
* start
  - utter_greet
  - utter_help

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

## explain arrival date journey planning
* start_journey_planning
  - journey_details_form
  - form{"name": "journey_details_form"}
  - slot{"requested_slot": "arrival_date"}
* explain
  - utter_explain_arrival_date
  - journey_details_form
  - form{"name": null}
  - utter_slots_values_journey_details

## explain first station journey planning
* start_journey_planning
  - journey_details_form
  - form{"name": "journey_details_form"}
  - slot{"requested_slot": "first_station"}
* explain
  - utter_explain_first_station
  - journey_details_form
  - form{"name": null}
  - utter_slots_values_journey_details

## out of scope intent
* out_of_scope
  - utter_out_of_scope
