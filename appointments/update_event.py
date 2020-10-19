from datetime import datetime, timedelta
from cal_setup import get_calendar_service
#from handle_time import process_time

def update(event_id, start, end):
    # update the event to tomorrow 9 AM IST
    service = get_calendar_service()

    event = service.events().get(calendarId='primary', eventId=event_id).execute()

    event_result = service.events().update(
        calendarId='primary',
        eventId = event_id,
        body={
            "summary": event["summary"],
            "description": event["description"],
            "start": {"dateTime": start, "timeZone": 'Etc/GMT+1'},
            "end": {"dateTime": end, "timeZone": 'Etc/GMT+1'},
        },
    ).execute()

    print("updated event")
    print("id: ", event_result['id'])
    print("summary: ", event_result['summary'])
    print("starts at: ", event_result['start']['dateTime'])
    print("ends at: ", event_result['end']['dateTime'])

    return event_result['id']

if __name__ == '__main__':
    update('ssme0vsr1prhqm1a3pqg8iqspo', '2020-10-11 09:30:00')
