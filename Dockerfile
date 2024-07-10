FROM python:3.11.9-alpine

ENV PYTHONBUFFERED 1

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . /app/

# collect static file
RUN python manage.py collectstatic --no-input

COPY staticfiles /app/staticfiles

RUN python manage.py migrate