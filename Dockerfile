FROM python:3.11.2-slim


# create the app user
RUN addgroup --system app && adduser --system --group app

WORKDIR /code


COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY . /code/

# chown all the files to the app user
RUN chown -R app:app /code

# change to the app user
USER app

EXPOSE 8000

# `gunicorn` will run with the options defined in gunicorn.conf.py
CMD ["gunicorn"]