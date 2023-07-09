FROM python:3.11.2-slim

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY . /code/

EXPOSE 8000

# `gunicorn` will run with the options defined in gunicorn.conf.py
CMD ["gunicorn"]