from create_event import create_event
from check_availability import check
from update_event import update
from delete_event import delete_event
from handle_time import process_time

def event_add(params):
    '''
    add an event to the calendar
    '''
    
    # extract name, date and time
    name = params['name']
    param_time = params['time']
    param_date = params['date']
    # process date and time inputs
    start, end = process_time(param_time, param_date, duration=1, z=True)
    # check if the selected time slot is available
    is_available = check(start, end)

    if is_available:
        event_id = create_event(start, end, name)
        answer = "Well received. The ID of your appointment is " + event_id
    else:
        answer = "This time slot is already reserved"

    return answer

def event_update(params):
    '''update an event in the calendar'''
    # extract name, date and time
    event_id = params['event_id']
    param_time = params['new_time']
    param_date = params['new_date']
    # process date and time inputs
    start, end = process_time(param_time, param_date, duration=1, z=True)
    # check if the selected time slot is available
    is_available = check(start, end)

    if is_available:
        answer = "There is no appointment in this time slot"
    else:
        event_id = update(event_id, start, end)
        answer = "Well received. The ID of your appointment is " + event_id

    return answer

def event_delete(params):
    '''delete an event from the calendar'''
    # extract the event_id
    event_id = params['event_id']
    # delete the event
    delete_event(event_id)

    answer = "Appointment canceled"

    return answer

def all_fields(params, intent='add_event'):
    '''
    Check if all parameters have been received by the server
    Returns True if so, False if not
    '''

    # parameters for the intent add_event
    if intent == 'add_event':
        if (params['date'] != '') & (params['time'] != '') & (params['name'] != ''): return True
        else: return False
    # parameters for the intent update_event
    elif intent == 'update_event':
        if (params['event_id'] != '') & (params['new_time'] != '') & (params['new_date'] != ''): return True
        else: return False
    # parameters for the intent delete_event
    elif intent == 'delete_event':
        if (params['event_id'] != ''): return True
        else: return False

    else: return False

def get_answer(intent, params):

    if all_fields(params, intent):
        if intent == 'add_event':
            answer = event_add(params)
        elif intent == 'update_event':
            answer = event_update(params)
        elif intent == 'delete_event':
            answer = event_delete(params)
        else:
            answer = "problem somewhere"

    return answer
