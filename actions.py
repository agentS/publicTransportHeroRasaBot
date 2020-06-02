from typing import Dict, Text, Any, List, Union, Optional

from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction


class JourneyDetailsForm(FormAction):

    def name(self):
        return 'journey_details_form'

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ['time', 'arrival_station']

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]
    ):
        dispatcher.utter_template('utter_submit_journey_details', tracker)
        return []
