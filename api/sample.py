import json
from datetime import datetime

from .models import Employee, ActivityPeriods

# datetime_object = datetime.strptime('Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p')


def get_date_time(date_time):
    datetime_object = datetime.strptime(date_time, '%b %d %Y %I:%M%p')
    return datetime_object


def get_source(source):
    # import ipdb;ipdb.set_trace()
    if source.endswith('.json'):
        file = open(source)
    else:
        val = source+".json"
        file = open(val)
    data = json.load(file)

    if data['ok']:
        for element in data['members']:

            employee_id = element['id']
            real_name = element['real_name']
            tz = element['tz']

            employee, e_flag = Employee.objects.get_or_create(
                employee_id=employee_id,
                real_name=real_name,
                tz=tz
            )

            for dates in element['activity_periods']:
                start_time = get_date_time(dates['start_time'])
                end_time = get_date_time(dates['end_time'])
                activity, a_flag = employee.activityperiods_set.get_or_create(
                    start_time=start_time,
                    end_time=end_time,
                )
    return True
