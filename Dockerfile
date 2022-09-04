FROM apache/airflow:latest-python3.10

USER root

RUN apt-get update \
  && apt-get install -y --no-install-recommends \
         vim \
         git \
  && apt-get autoremove -yqq --purge \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

RUN mkdir /srv/git && chown -R "${AIRFLOW_UID}:0" /srv/git

USER airflow

RUN pip install --upgrade pip

RUN pip install git+https://github.com/my-oh-my/xtbwrapper.git

RUN cd /srv/git && \
    ((cd expert-advisor && git fetch --all && git reset --hard origin/master) || git clone https://github.com/my-oh-my/expert-advisor.git)

ENV PYTHONPATH="/srv/git/expert-advisor/"

COPY requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt
