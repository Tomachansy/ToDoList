FROM python:3.10-slim

WORKDIR /app
RUN apt-get update && apt-get install && apt-get upgrade -y gcc \
                                                            libpq-dev
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . ./
CMD python manage.py runserver 0.0.0.0:8000