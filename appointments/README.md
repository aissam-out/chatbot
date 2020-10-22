# Google Calendar API

Google Calendar is one of the most popular ways to manage your schedule. In this project we use the Google Calendar API to automate your calendar and link it to DialogFlow so that we'll be able to have a chatbot able to book appointments for you and/or your business.

## DialogFlow

First thing to do is to create a DialogFlow agent and train it to detect three intents : _add event_, _delete event_ and _update event_. Then we'll use Fulfillment to link it to our backend code.

- add_event : make sure you mark the three parameters (_date, time_ and _name_) as required

- update_event : you will also need to have three required parameters : _event_id, new_date and new_time_

- delete_event : make sure you put the _event_id_ a required parameter

## G-Calendar

* Google Developer Console
  * Go to [Google Developers console](https://console.developers.google.com/) and create a new project
  * Go to the dashboard and search for Calendar API in the search bar, then enable it
  
* Credentials
  * In the left-hand menu select **Credentials**, **Create Credentials** then **OAuth Client ID**
  * Select the **Web application** type and give it a name
  * In the **Authorized redirect URIs** section add http://localhost/ in our case, then **create**
  * Download the **OAuth credentials** as a **JSON** file, name it **credentials.json** 

* Google OAuth SDK for Python
  * Pip install the required packages: ```pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib```
  * Here is the list of the [Google Calendar scopes](https://developers.google.com/calendar/auth)

