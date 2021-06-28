FROM python:3.8-slim-buster
ENV PYTHONUNBUFFERED 1


RUN mkdir /app

WORKDIR /app

COPY requirements.txt /app/
RUN pip3 install -r requirements.txt

COPY . /app/

RUN python3 manage.py makemigrations
RUN python3 manage.py migrate

CMD [ "python3", "manage.py" , "runserver", "0.0.0.0:7000"]
