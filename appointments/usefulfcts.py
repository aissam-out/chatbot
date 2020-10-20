from create_event import create_event
from check_availability import check
from update_event import update
from delete_event import delete_event
from handle_time import process_time

def event_add(params):
    name = params['name']
    param_time = params['time']
    param_date = params['date']

    start, end = process_time(param_time, param_date, duration=1, z=True)

    is_available = check(start, end)

    if is_available:
        event_id = create_event(start, end, name)
        answer = "Bien reçu. L'ID de votre RDV est " + event_id
    else:
        answer = "Ce créneau est déjà réservé"

    return answer

def event_update(params):
    event_id = params['event_id']
    param_time = params['new_time']
    param_date = params['new_date']

    start, end = process_time(param_time, param_date, duration=1, z=True)

    is_available = check(start, end)

    if is_available:
        event_id = update(event_id, start, end)
        answer = "Bien reçu. L'ID de votre RDV est " + event_id
    else:
        answer = "Ce créneau est déjà réservé"

    return answer

def event_delete(params):
    event_id = params['event_id']
    delete_event(event_id)

    answer = "Rendez-vous annulé"

    return answer

def all_fields(params, intent='add_event'):
    if intent == 'add_event':
        if (params['date'] != '') & (params['time'] != '') & (params['name'] != ''): return True
        else: return False

    elif intent == 'update_event':
        if (params['event_id'] != '') & (params['new_time'] != '') & (params['new_date'] != ''): return True
        else: return False

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
