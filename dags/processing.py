from datetime import datetime, timedelta

import pendulum

local_tz = pendulum.timezone('Europe/Warsaw')
START_DATE_TIME = datetime.now(tz=local_tz) - timedelta(hours=1)


def get_default_args(**custom_args):
    default_args = {
        'owner': 'airflow',
        'start_date': START_DATE_TIME,
        'email_on_failure': False,
        'email_on_retry': False,
        'retries': 3,
        'retry_delay': timedelta(minutes=1),
        'execution_timeout': timedelta(minutes=5),
        'priority_weight': 10
    }
    return {**default_args, **custom_args}