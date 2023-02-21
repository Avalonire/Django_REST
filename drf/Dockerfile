FROM python:3.10.7

RUN apt-get update \
&& apt-get install -y postgresql postgresql-contrib libpg-dev python-dev

RUN pip install --upgrade pip

COPY ./library/ ./
RUN pip install -r requirements.txt

COPY wait-for-postgres.sh .
RUN chmod +x wait-for-postgres.sh

RUN pip install gunicorn
