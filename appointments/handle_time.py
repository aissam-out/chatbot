from datetime import datetime, timedelta

def process_time(param_time, param_date, duration=1, z=True):
    '''
    convert rfc_3339 to useable time format
    input format : '2020-10-13T14:30:00+01:00'
    '''

    # isolate date and time
    date = param_date.split('T')[0]
    time = param_time.split('+')[0].split('T')[1]

    # convert date & time to 'dateTtime' object
    dt = date + 'T' + time
    datetime_object = datetime.fromisoformat(dt)

    # create end time & add Z to datetime object if needed
    if z:
        start = datetime_object.isoformat() + 'Z'
        end = (datetime_object + timedelta(hours=duration)).isoformat() + 'Z'
    else:
        start = datetime_object.isoformat()
        end = (datetime_object + timedelta(hours=duration)).isoformat()

    return start, end
