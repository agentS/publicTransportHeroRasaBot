#### This file contains tests to evaluate that your bot behaves as expected.
#### If you want to learn more, please see the docs: https://rasa.com/docs/rasa/user-guide/testing-your-assistant/

## greet and ask for general help alpha
* greet: Hallo!
  - utter_greet
  - utter_main_menu
* general_help: Was kann ich machen?
  - utter_general_help

## greet and lookup a single connection alpha
* greet: Schönen Abend!
  - utter_greet
  - utter_main_menu
* lookup_single_connection: Ich möchte eine Verbindung nachschlagen
  - utter_lookup_single_connection

## greet and start journey planning
* greet: Hallo! :)
  - utter_greet
  - utter_main_menu
* start_journey_planning: Ich möchte einen Citytrip nach Wien machen.
  - utter_start_journey_planning

## greet, ask for help, and start journey planning
* greet: Heya! :)
  - utter_greet
  - utter_main_menu
* general_help: Was kann ich machen?
  - utter_general_help
* start_journey_planning: Ich möchte nach Wien reisen. 
  - utter_start_journey_planning
