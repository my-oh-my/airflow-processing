from airflow import DAG
from airflow.models import Variable
from airflow.operators.bash import BashOperator

from processing import get_default_args

with DAG('engulfing-EURUSD_60',
          default_args=get_default_args(),
          schedule_interval='0 * * * *',
          concurrency=1,
          max_active_runs=1,
          catchup=False) as dag:
    args = f'{Variable.get("EURUSD_ENGULFING_60_ARGS")}'
    command = f'cd /srv/git/expert-advisor/ea && python engulfing_runner.py ' + args
    BashOperator(
        task_id='ea',
        bash_command=command,
        dag=dag
    )
