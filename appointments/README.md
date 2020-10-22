# Google Calendar API

Google Calendar is one of the most popular ways to manage your schedule. In this project we use the Google Calendar API to automate your calendar and link it to DialogFlow so that we'll be able to have a chatbot able to book appointments for you and/or your business.

## DialogFlow

First thing to do is to create a DialogFlow agent and train it to detect three intents : _add event_, _delete event_ and _update event_. Then we'll use Fulfillment to link it to our backend code.

- add_event : make sure you mark the three parameters (_date, time_ and _name_) as required

- update_event : you will also need to have three required parameters : _event_id, new_date and new_time_

- delete_event : make sure you put the _event_id_ a required parameter
