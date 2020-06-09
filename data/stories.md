## greet and ask for general help
* greet
  - utter_greet
  - utter_main_menu
* general_help
  - utter_general_help

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
* general_help
  - utter_general_help
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
* general_help
  - utter_general_help
* start_journey_planning
  - utter_start_journey_planning
  - journey_details_form
  - form{"name": "journey_details_form"}
  - form{"name": null}
  - utter_slots_values_journey_details
