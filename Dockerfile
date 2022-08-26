# pull official base image
FROM python:3.10-slim

# set work directory
WORKDIR /app/

# install psycopg2 dependencies
RUN apt-get update \
    && apt-get add postgresql-dev gcc python3-dev musl-dev

# install dependencies
RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .