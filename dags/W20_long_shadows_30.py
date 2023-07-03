from airflow import DAG
from airflow.models import Variable
from airflow.operators.bash import BashOperator

from processing import get_default_args

with DAG('long-shadows-W20_30',
          default_args=get_default_args(),
         schedule_interval='*/30 8-17 * * 1-5',
          concurrency=1,
          max_active_runs=1,
          catchup=False) as dag:
    args = f'{Variable.get("W20_LONG_SHADOWS_30_ARGS")}'
    command = f'cd /srv/git/expert-advisor/ea && python candles_long_shadows_runner.py ' + args
    BashOperator(
        task_id='ea',
        bash_command=command,
        dag=dag
    )
