#### This file contains tests to evaluate that your bot behaves as expected.
#### If you want to learn more, please see the docs: https://rasa.com/docs/rasa/user-guide/testing-your-assistant/

## greet and ask for general help alpha
* greet: Hallo!
  - utter_greet
  - utter_main_menu
* help: Was kann ich machen?
  - utter_help

## greet and lookup a single connection alpha
* greet: Guten Abend!
  - utter_greet
  - utter_main_menu
* lookup_single_connection: Ich möchte eine Verbindung nachschlagen
  - utter_lookup_single_connection
  - lookup_single_connection_form
  - form{"name": "lookup_single_connection_form"}
* specify_departure_and_arrival_station: Ich fahre vom [Hauptbahnhof]{"entity": "station", "role": "departure"} nach [Floridsdorf S+U]{"entity": "station", "role": "arrival"}
  - lookup_single_connection_form
  - form{"name": null}
  - action_lookup_single_connection
  - utter_main_menu

## greet and lookup a single connection bravo
* greet: Guten Abend!
  - utter_greet
  - utter_main_menu
* lookup_single_connection: Ich möchte eine Verbindung nachschlagen
  - utter_lookup_single_connection
  - lookup_single_connection_form
  - form{"name": "lookup_single_connection_form"}
* specify_departure_and_arrival_station: Ich fahre von der [Stranitzkygasse]{"entity": "station", "role": "departure"} nach [Michelbeuern-AKH]{"entity": "station", "role": "arrival"}
  - lookup_single_connection_form
  - form{"name": null}
  - action_lookup_single_connection
  - utter_main_menu

## greet and lookup a single connection with explanation
* greet: Guten Abend!
  - utter_greet
  - utter_main_menu
* lookup_single_connection: Ich möchte eine Verbindung nachschlagen
  - utter_lookup_single_connection
  - lookup_single_connection_form
  - form{"name": "lookup_single_connection_form"}
* explain: Hilfe
  - lookup_single_connection_form
* specify_departure_and_arrival_station: Ich fahre von der [Stranitzkygasse]{"entity": "station", "role": "departure"} nach [Michelbeuern-AKH]{"entity": "station", "role": "arrival"}
  - lookup_single_connection_form
  - form{"name": null}
  - action_lookup_single_connection
  - utter_main_menu

## greet and start journey planning
* greet: Hallo! :)
  - utter_greet
  - utter_main_menu
* start_journey_planning: Ich möchte einen Citytrip machen.
  - utter_start_journey_planning
  - journey_details_form
  - form{"name": "journey_details_form"}
* select_arrival_station: Ich komme am [Hauptbahnhof]{"entity": "station", "role": "arrival"} an
  - journey_details_form
  - form{"name": null}
  - action_initialize_journey_planning
  - utter_destinations_loop_journey_planning
  - utter_add_route_or_wait_for_next_day
* add_destination_journey_planning: "Ich möchte einen Halt hinzufügen"
  - journey_add_route_form
  - form{"name": "journey_add_route_form"}
* select_arrival_station: Ich fahre zum [Stephansplatz]{"entity": "station", "role": "arrival"}
  - journey_add_route_form
  - form{"name": null}
  - action_add_journey_route
  - utter_add_route_or_wait_for_next_day_or_finish_journey_planning
* add_destination_journey_planning: "Nächster Halt"
  - journey_add_route_form
  - form{"name": "journey_add_route_form"}
* specify_departure_and_arrival_station: Ich fahre vom [Karlsplatz]{"entity": "station", "role": "departure"} zum [Hauptbahnhof]{"entity": "station", "role": "arrival"}
  - journey_add_route_form
  - form{"name": null}
  - action_add_journey_route
  - utter_add_route_or_wait_for_next_day_or_finish_journey_planning
* finish_journey_planning: "Ich bin mit dem Planen fertig"
  - action_finish_journey_planning
  - utter_main_menu

## greet, ask for help, and start journey planning
* greet: Aloha! :)
  - utter_greet
  - utter_main_menu
* help: Was kann ich machen?
  - utter_help
* start_journey_planning: Ich möchte einen Citytrip machen.
  - utter_start_journey_planning
  - journey_details_form
  - form{"name": "journey_details_form"}
* select_arrival_station: Ich komme in [Hütteldorf S+U]{"entity": "station", "role": "arrival"} an
  - journey_details_form
  - form{"name": null}
  - action_initialize_journey_planning
  - utter_destinations_loop_journey_planning
  - utter_add_route_or_wait_for_next_day
* add_destination_journey_planning: "Ich möchte einen Halt hinzufügen"
  - journey_add_route_form
  - form{"name": "journey_add_route_form"}
* select_arrival_station: Ich fahre zum [Stephansplatz]{"entity": "station", "role": "arrival"}
  - journey_add_route_form
  - form{"name": null}
  - action_add_journey_route
  - utter_add_route_or_wait_for_next_day_or_finish_journey_planning
* add_destination_journey_planning: "Nächster Halt"
  - journey_add_route_form
  - form{"name": "journey_add_route_form"}
* specify_departure_and_arrival_station: Ich fahre vom [Karlsplatz]{"entity": "station", "role": "departure"} nach [Alterlaa U]{"entity": "station", "role": "arrival"}
  - journey_add_route_form
  - form{"name": null}
  - action_add_journey_route
  - utter_add_route_or_wait_for_next_day_or_finish_journey_planning
* add_destination_journey_planning: "Stop hinzufügen"
  - journey_add_route_form
  - form{"name": "journey_add_route_form"}
* select_arrival_station: Ich fahre in die [Stranitzkygasse]{"entity": "station", "role": "arrival"}
  - journey_add_route_form
  - form{"name": null}
  - action_add_journey_route
  - utter_add_route_or_wait_for_next_day_or_finish_journey_planning
* wait_for_next_day: "Ich möchte eine Pause einlegen"
  - utter_wait_for_next_day
  - action_wait_for_next_day
  - utter_add_route_or_wait_for_next_day_or_finish_journey_planning
* add_destination_journey_planning: "Ich möchte einen Halt hinzufügen"
  - journey_add_route_form
  - form{"name": "journey_add_route_form"}
* specify_departure_and_arrival_station: Ich fahre von [Meidling S+U]{"entity": "station", "role": "departure"} zum [Hauptbahnhof]{"entity": "station", "role": "arrival"}
  - journey_add_route_form
  - form{"name": null}
  - action_add_journey_route
  - utter_add_route_or_wait_for_next_day_or_finish_journey_planning
* finish_journey_planning: "Ich bin mit dem Planen fertig"
  - action_finish_journey_planning
  - utter_main_menu

## greet, ask for help, and start journey planning with explanations
* greet: Aloha! :)
  - utter_greet
  - utter_main_menu
* help: Was kann ich machen?
  - utter_help
* start_journey_planning: Ich möchte einen Citytrip machen.
  - utter_start_journey_planning
  - journey_details_form
  - form{"name": "journey_details_form"}
* explain: Hilfe?
  - journey_details_form
* select_arrival_station: Ich komme in [Hütteldorf S+U]{"entity": "station", "role": "arrival"} an
  - journey_details_form
  - form{"name": null}
  - action_initialize_journey_planning
  - utter_destinations_loop_journey_planning
  - utter_add_route_or_wait_for_next_day
* add_destination_journey_planning: "Ich möchte einen Halt hinzufügen"
  - journey_add_route_form
  - form{"name": "journey_add_route_form"}
* explain: Ich kenne mich nicht aus.
  - journey_add_route_form
* select_arrival_station: Ich fahre zum [Stephansplatz]{"entity": "station", "role": "arrival"}
  - journey_add_route_form
  - form{"name": null}
  - action_add_journey_route
  - utter_add_route_or_wait_for_next_day_or_finish_journey_planning
* add_destination_journey_planning: "Nächster Halt"
  - journey_add_route_form
  - form{"name": "journey_add_route_form"}
* specify_departure_and_arrival_station: Ich fahre vom [Karlsplatz]{"entity": "station", "role": "departure"} nach [Alterlaa U]{"entity": "station", "role": "arrival"}
  - journey_add_route_form
  - form{"name": null}
  - action_add_journey_route
  - utter_add_route_or_wait_for_next_day_or_finish_journey_planning
* add_destination_journey_planning: "Stop hinzufügen"
  - journey_add_route_form
  - form{"name": "journey_add_route_form"}
* select_arrival_station: Ich fahre in die [Stranitzkygasse]{"entity": "station", "role": "arrival"}
  - journey_add_route_form
  - form{"name": null}
  - action_add_journey_route
  - utter_add_route_or_wait_for_next_day_or_finish_journey_planning
* wait_for_next_day: "Ich möchte eine Pause einlegen"
  - utter_wait_for_next_day
  - action_wait_for_next_day
  - utter_add_route_or_wait_for_next_day_or_finish_journey_planning
* add_destination_journey_planning: "Ich möchte einen Halt hinzufügen"
  - journey_add_route_form
  - form{"name": "journey_add_route_form"}
* specify_departure_and_arrival_station: Ich fahre von [Meidling S+U]{"entity": "station", "role": "departure"} zum [Hauptbahnhof]{"entity": "station", "role": "arrival"}
  - journey_add_route_form
  - form{"name": null}
  - action_add_journey_route
  - utter_add_route_or_wait_for_next_day_or_finish_journey_planning
* finish_journey_planning: "Ich bin mit dem Planen fertig"
  - action_finish_journey_planning
  - utter_main_menu
