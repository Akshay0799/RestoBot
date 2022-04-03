from copyreg import dispatch_table
from typing import Dict, Text, List, Any

from rasa_sdk import Tracker
from rasa_sdk.events import EventType
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk import Action, FormValidationAction
from rasa_sdk.types import DomainDict
from maps import fetch_restaurant, fetch_contact
from weather import fetch_weather
from rasa_sdk.events import SlotSet
from slugify import slugify

class ActionFetchWeather(Action):
    def name(self) -> Text:
        return "action_weather_api"

    def run (self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
    
        weather = fetch_weather()
        url = slugify(weather[3][2:])
        dispatcher.utter_template("utter_return_weather",tracker, temp = weather[0], feel_like = weather[1], condition = weather[2], icon = url)
        return []
        
class ActionFetchRestaurant(Action):

    def name(self) -> Text:
        return "action_maps_api"
    
    def run (self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        food_type = tracker.get_slot('food_type')
        temp = fetch_restaurant(food_type)
        dispatcher.utter_template("utter_restaurants_found",tracker)
        
        
        for i in range(5):
            dispatcher.utter_template("utter_restaurants", tracker, restaurant = temp[i][0], place = temp[i][1]) 
        return []

class ActionDetailsRestaurant(Action):

    def name(self) -> Text:
        return "action_faq_api"
    
    def run (self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        food_type = tracker.get_slot('food_type')
        rest = tracker.get_slot("restaurant_name")
        # print("before calling api")
        temp = fetch_restaurant(food_type)
        # print("after calling api")
        # print("output from api",temp[0])
        # print(temp)
        for i in temp:
            if rest == i[0]:
                rest_no = fetch_contact(i[4])
                return [SlotSet("distance", float(i[2])/1000), SlotSet("address", i[3]), SlotSet("restaurant_number", rest_no)]        
        return []

class ValidateForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_name_form"

    def validate_first_name(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[str, str]:
        if len(slot_value) == 0:
            dispatcher.utter_message(text="That must've been a typo.")
            return {"first_name": None}
        else:
            return {"first_name": slot_value}
        
    def validate_last_name(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `last_name` value."""
        if len(slot_value) == 0:
            dispatcher.utter_message(text="That must've been a typo.")
            return {"last_name": None}
        
        first_name = tracker.get_slot("first_name")
        if len(first_name) + len(slot_value) < 3:
            dispatcher.utter_message(text="That's a very short name. We fear a typo. Restarting!")
            return {"first_name": None, "last_name": None}
        return {"last_name": slot_value}

    def validate_no_of_seats(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `last_name` value."""
        if len(slot_value) == 0:
            dispatcher.utter_message(text="That must've been a typo.")
            return {"no_of_seats": None}
        else:
            return {"no_of_seats": slot_value}
    
    def validate_phone_no(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `last_name` value."""
        if len(slot_value) == 0:
            dispatcher.utter_message(text="That must've been a typo, Enter the number again")
            return {"phone_no": None}
        elif len(slot_value) > 10:
            dispatcher.utter_message(text="Please enter a valid phone number")
            return {"phone_no": None}
        else:
            return {"phone_no": slot_value}
        
    def validate_time(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `last_name` value."""
        if len(slot_value) == 0:
            dispatcher.utter_message(text="That must've been a typo...")
            return {"time": None}
        else:
            return {"time": slot_value}

    def validate_confirm_details(
        self,
        value: Text,
        dispatcher: "CollectingDispatcher",
        tracker: "Tracker",
        domain: "DomainDict",
    ) -> Dict[str, str]:
        intent_name = tracker.get_intent_of_latest_message()
        print(value)
        if value == "Yes":
            dispatcher.utter_message(template="utter_booking_confirmed")
            # dispatcher.utter_message(text="Do you have any queries ?")
        elif value == "qwert":
            dispatcher.utter_message(template="utter_booking_failed")
            dispatcher.utter_message(text="Booking is cancelled. Restarting the form...")
            return {"first_name": None, "last_name": None, "no_of_seats": None, "phone_no": None, "time": None}

        