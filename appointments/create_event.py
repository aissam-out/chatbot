from datetime import datetime, timedelta
from cal_setup import get_calendar_service

def create_event(start, end, summary='pas de nom', description='pas de description'):
    # creates one hour event tomorrow 10 AM IST
    service = get_calendar_service()

    event_result = service.events().insert(calendarId='primary',
        body={
            "summary": summary,
            "description": description,
            "start": {"dateTime": start, "timeZone": 'Etc/GMT+1'},
            "end": {"dateTime": end, "timeZone": 'Etc/GMT+1'},
        }
    ).execute()

    print("created event")
    print("id: ", event_result['id'])
    print("summary: ", event_result['summary'])
    print("starts at: ", event_result['start']['dateTime'])
    print("ends at: ", event_result['end']['dateTime'])

    return event_result['id']

if __name__ == '__main__':
    create_event('2020-10-13T14:30:00+01:00', 1, 'not default summary', 'not default description')
