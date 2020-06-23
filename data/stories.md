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
  - utter_main_menu

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
  - utter_main_menu

## explain departure station single connection lookup
* lookup_single_connection
  - lookup_single_connection_form
  - form{"name": "lookup_single_connection_form"}
  - slot{"requested_slot": "departure_station"}
* explain
  - utter_explain_departure_station_to_arrival_station_single_connection_lookup
  - lookup_single_connection_form
  - form{"name": null}
  - action_lookup_single_connection
  - utter_main_menu

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
  - utter_main_menu

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
  - utter_main_menu

## greet and start single day journey planning
* greet
  - utter_greet
  - utter_main_menu
* start_journey_planning
  - utter_start_journey_planning
  - journey_details_form
  - form{"name": "journey_details_form"}
  - form{"name": null}
  - action_initialize_journey_planning
  - utter_destinations_loop_journey_planning
  - utter_add_route_or_wait_for_next_day
* add_destination_journey_planning
  - journey_add_route_form
  - form{"name": "journey_add_route_form"}
  - form{"name": null}
  - action_add_journey_route
  - utter_add_route_or_wait_for_next_day_or_finish_journey_planning
* add_destination_journey_planning
  - journey_add_route_form
  - form{"name": "journey_add_route_form"}
  - form{"name": null}
  - action_add_journey_route
  - utter_add_route_or_wait_for_next_day_or_finish_journey_planning
* finish_journey_planning
  - action_finish_journey_planning
  - utter_main_menu

## greet, ask for help, and start single day journey planning
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
  - action_initialize_journey_planning
  - utter_destinations_loop_journey_planning
  - utter_add_route_or_wait_for_next_day
* add_destination_journey_planning
  - journey_add_route_form
  - form{"name": "journey_add_route_form"}
  - form{"name": null}
  - action_add_journey_route
  - utter_add_route_or_wait_for_next_day_or_finish_journey_planning
* add_destination_journey_planning
  - journey_add_route_form
  - form{"name": "journey_add_route_form"}
  - form{"name": null}
  - action_add_journey_route
  - utter_add_route_or_wait_for_next_day_or_finish_journey_planning
* finish_journey_planning
  - action_finish_journey_planning
  - utter_main_menu

## greet and start two day journey planning with initial layover
* greet
  - utter_greet
  - utter_main_menu
* start_journey_planning
  - utter_start_journey_planning
  - journey_details_form
  - form{"name": "journey_details_form"}
  - form{"name": null}
  - action_initialize_journey_planning
  - utter_destinations_loop_journey_planning
  - utter_add_route_or_wait_for_next_day
* wait_for_next_day
  - utter_wait_for_next_day
  - action_wait_for_next_day
  - utter_add_route_or_wait_for_next_day_or_finish_journey_planning
* add_destination_journey_planning
  - journey_add_route_form
  - form{"name": "journey_add_route_form"}
  - form{"name": null}
  - action_add_journey_route
  - utter_add_route_or_wait_for_next_day_or_finish_journey_planning
* add_destination_journey_planning
  - journey_add_route_form
  - form{"name": "journey_add_route_form"}
  - form{"name": null}
  - action_add_journey_route
  - utter_add_route_or_wait_for_next_day_or_finish_journey_planning
* add_destination_journey_planning
  - journey_add_route_form
  - form{"name": "journey_add_route_form"}
  - form{"name": null}
  - action_add_journey_route
  - utter_add_route_or_wait_for_next_day_or_finish_journey_planning
* finish_journey_planning
  - action_finish_journey_planning
  - utter_main_menu

## greet and start two day journey planning
* greet
  - utter_greet
  - utter_main_menu
* start_journey_planning
  - utter_start_journey_planning
  - journey_details_form
  - form{"name": "journey_details_form"}
  - form{"name": null}
  - action_initialize_journey_planning
  - utter_destinations_loop_journey_planning
  - utter_add_route_or_wait_for_next_day
* add_destination_journey_planning
  - journey_add_route_form
  - form{"name": "journey_add_route_form"}
  - form{"name": null}
  - action_add_journey_route
  - utter_add_route_or_wait_for_next_day_or_finish_journey_planning
* wait_for_next_day
  - utter_wait_for_next_day
  - action_wait_for_next_day
  - utter_add_route_or_wait_for_next_day_or_finish_journey_planning
* add_destination_journey_planning
  - journey_add_route_form
  - form{"name": "journey_add_route_form"}
  - form{"name": null}
  - action_add_journey_route
  - utter_add_route_or_wait_for_next_day_or_finish_journey_planning
* add_destination_journey_planning
  - journey_add_route_form
  - form{"name": "journey_add_route_form"}
  - form{"name": null}
  - action_add_journey_route
  - utter_add_route_or_wait_for_next_day_or_finish_journey_planning
* add_destination_journey_planning
  - journey_add_route_form
  - form{"name": "journey_add_route_form"}
  - form{"name": null}
  - action_add_journey_route
  - utter_add_route_or_wait_for_next_day_or_finish_journey_planning
* add_destination_journey_planning
  - journey_add_route_form
  - form{"name": "journey_add_route_form"}
  - form{"name": null}
  - action_add_journey_route
  - utter_add_route_or_wait_for_next_day_or_finish_journey_planning
* finish_journey_planning
  - action_finish_journey_planning
  - utter_main_menu

## greet and start three day journey planning with initial layover
* greet
  - utter_greet
  - utter_main_menu
* start_journey_planning
  - utter_start_journey_planning
  - journey_details_form
  - form{"name": "journey_details_form"}
  - form{"name": null}
  - action_initialize_journey_planning
  - utter_destinations_loop_journey_planning
  - utter_add_route_or_wait_for_next_day
* wait_for_next_day
  - utter_wait_for_next_day
  - action_wait_for_next_day
  - utter_add_route_or_wait_for_next_day_or_finish_journey_planning
* add_destination_journey_planning
  - journey_add_route_form
  - form{"name": "journey_add_route_form"}
  - form{"name": null}
  - action_add_journey_route
  - utter_add_route_or_wait_for_next_day_or_finish_journey_planning
* add_destination_journey_planning
  - journey_add_route_form
  - form{"name": "journey_add_route_form"}
  - form{"name": null}
  - action_add_journey_route
  - utter_add_route_or_wait_for_next_day_or_finish_journey_planning
* wait_for_next_day
  - utter_wait_for_next_day
  - action_wait_for_next_day
  - utter_add_route_or_wait_for_next_day_or_finish_journey_planning
* add_destination_journey_planning
  - journey_add_route_form
  - form{"name": "journey_add_route_form"}
  - form{"name": null}
  - action_add_journey_route
  - utter_add_route_or_wait_for_next_day_or_finish_journey_planning
* add_destination_journey_planning
  - journey_add_route_form
  - form{"name": "journey_add_route_form"}
  - form{"name": null}
  - action_add_journey_route
  - utter_add_route_or_wait_for_next_day_or_finish_journey_planning
* add_destination_journey_planning
  - journey_add_route_form
  - form{"name": "journey_add_route_form"}
  - form{"name": null}
  - action_add_journey_route
  - utter_add_route_or_wait_for_next_day_or_finish_journey_planning
* finish_journey_planning
  - action_finish_journey_planning
  - utter_main_menu

## greet and start three day journey planning
* greet
  - utter_greet
  - utter_main_menu
* start_journey_planning
  - utter_start_journey_planning
  - journey_details_form
  - form{"name": "journey_details_form"}
  - form{"name": null}
  - action_initialize_journey_planning
  - utter_destinations_loop_journey_planning
  - utter_add_route_or_wait_for_next_day
* add_destination_journey_planning
  - journey_add_route_form
  - form{"name": "journey_add_route_form"}
  - form{"name": null}
  - action_add_journey_route
  - utter_add_route_or_wait_for_next_day_or_finish_journey_planning
* add_destination_journey_planning
  - journey_add_route_form
  - form{"name": "journey_add_route_form"}
  - form{"name": null}
  - action_add_journey_route
  - utter_add_route_or_wait_for_next_day_or_finish_journey_planning
* add_destination_journey_planning
  - journey_add_route_form
  - form{"name": "journey_add_route_form"}
  - form{"name": null}
  - action_add_journey_route
  - utter_add_route_or_wait_for_next_day_or_finish_journey_planning
* wait_for_next_day
  - utter_wait_for_next_day
  - action_wait_for_next_day
  - utter_add_route_or_wait_for_next_day_or_finish_journey_planning
* add_destination_journey_planning
  - journey_add_route_form
  - form{"name": "journey_add_route_form"}
  - form{"name": null}
  - action_add_journey_route
  - utter_add_route_or_wait_for_next_day_or_finish_journey_planning
* add_destination_journey_planning
  - journey_add_route_form
  - form{"name": "journey_add_route_form"}
  - form{"name": null}
  - action_add_journey_route
  - utter_add_route_or_wait_for_next_day_or_finish_journey_planning
* add_destination_journey_planning
  - journey_add_route_form
  - form{"name": "journey_add_route_form"}
  - form{"name": null}
  - action_add_journey_route
  - utter_add_route_or_wait_for_next_day_or_finish_journey_planning
* add_destination_journey_planning
  - journey_add_route_form
  - form{"name": "journey_add_route_form"}
  - form{"name": null}
  - action_add_journey_route
  - utter_add_route_or_wait_for_next_day_or_finish_journey_planning
* wait_for_next_day
  - utter_wait_for_next_day
  - action_wait_for_next_day
  - utter_add_route_or_wait_for_next_day_or_finish_journey_planning
* add_destination_journey_planning
  - journey_add_route_form
  - form{"name": "journey_add_route_form"}
  - form{"name": null}
  - action_add_journey_route
  - utter_add_route_or_wait_for_next_day_or_finish_journey_planning
* add_destination_journey_planning
  - journey_add_route_form
  - form{"name": "journey_add_route_form"}
  - form{"name": null}
  - action_add_journey_route
  - utter_add_route_or_wait_for_next_day_or_finish_journey_planning
* add_destination_journey_planning
  - journey_add_route_form
  - form{"name": "journey_add_route_form"}
  - form{"name": null}
  - action_add_journey_route
  - utter_add_route_or_wait_for_next_day_or_finish_journey_planning
* finish_journey_planning
  - action_finish_journey_planning
  - utter_main_menu

## explain arrival date journey planning
* start_journey_planning
  - journey_details_form
  - form{"name": "journey_details_form"}
  - slot{"requested_slot": "arrival_date"}
* explain
  - utter_explain_arrival_date
  - journey_details_form
  - form{"name": null}
  - action_initialize_journey_planning
  - utter_destinations_loop_journey_planning
  - utter_add_route_or_wait_for_next_day

## explain first station journey planning
* start_journey_planning
  - journey_details_form
  - form{"name": "journey_details_form"}
  - slot{"requested_slot": "first_station"}
* explain
  - utter_explain_first_station
  - journey_details_form
  - form{"name": null}
  - action_initialize_journey_planning
  - utter_destinations_loop_journey_planning
  - utter_add_route_or_wait_for_next_day

## explain journey route arrival station
* add_destination_journey_planning
  - journey_add_route_form
  - form{"name": "journey_add_route_form"}
  - slot{"requested_slot": "journey_route_arrival_station"}
* explain
  - utter_explain_journey_route_arrival_station
  - journey_add_route_form
  - form{"name": null}
  - action_add_journey_route
  - utter_add_route_or_wait_for_next_day_or_finish_journey_planning

## explain journey route departure date time
* add_destination_journey_planning
  - journey_add_route_form
  - form{"name": "journey_add_route_form"}
  - slot{"requested_slot": "journey_route_departure_date_time"}
* explain
  - utter_explain_journey_route_departure_date_time
  - journey_add_route_form
  - form{"name": null}
  - action_add_journey_route
  - utter_add_route_or_wait_for_next_day_or_finish_journey_planning

## out of scope intent
* out_of_scope
  - utter_out_of_scope
