from airflow import DAG
from airflow.models import Variable
from airflow.operators.bash import BashOperator

from processing import get_default_args

dag = DAG('consolidation-ETHEREUM_30',
          default_args=get_default_args(),
          schedule_interval='*/30 * * * *',
          concurrency=1,
          max_active_runs=1,
          catchup=False)

args = f'{Variable.get("ETHEREUM_30_ARGS")}'
command = f'cd /srv/git/expert-advisor/ea && python main.py ' + args
task = BashOperator(
    task_id='ea',
    bash_command=command,
    dag=dag
)

task
