from datetime import datetime, timedelta
from cal_setup import get_calendar_service
#from handle_time import process_time

def check(start, end):

    service = get_calendar_service()

    print("new start : ", start)
    print("new end : ", end)

    print('Getting List o 10 events 2.0')
    events_result = service.events().list(calendarId='primary', timeMin=start, timeMax=end).execute()
    events = events_result.get('items', [])

    if not events:
        print('No upcoming events found.')
        answer = True
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(start, event['summary'])
        answer = False

    print(answer)
    return answer

if __name__ == '__main__':
    check('2020-10-11T14:30:00+01:00')
    #check('2020-10-11 09:30:00')
