from datetime import datetime, timedelta
from cal_setup import get_calendar_service

def update(event_id, start, end):
    # authentication
    service = get_calendar_service()
    # get event from primary calendar via event_id
    event = service.events().get(calendarId='primary', eventId=event_id).execute()
    # update event
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
    # print the updated fields of the event
    print("updated event")
    print("id: ", event_result['id'])
    print("summary: ", event_result['summary'])
    print("starts at: ", event_result['start']['dateTime'])
    print("ends at: ", event_result['end']['dateTime'])

    return event_result['id']

if __name__ == '__main__':
    # for test
    update('v1a2pqg9justfortestnclkdlq', '2020-10-13T14:30:00+01:00')
