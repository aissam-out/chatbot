from cal_setup import get_calendar_service

def check(start, end):
    '''check is a given datetime is available is not already taken'''

    # authentication
    service = get_calendar_service()

    # check for availability
    print('Getting events ...')
    events_result = service.events().list(calendarId='primary', timeMin=start, timeMax=end).execute()
    events = events_result.get('items', [])

    if not events:
        print('It is free')
        answer = True
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(start, event['summary'])
        answer = False

    return answer

if __name__ == '__main__':
    # for test
    check('2020-10-11T14:30:00+01:00')
