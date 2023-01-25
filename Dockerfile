FROM python:latest
ENV PYTHONUNBUFFERED 1
ENV DJANGO_ENV dev
ENV DOCKER_CONTAINER 1

COPY ./requirements.txt /code/requirements.txt
RUN pip install Django==3.2.6
RUN pip install -U channels["daphne"]
RUN pip install -r /code/requirements.txt



COPY . /code/
WORKDIR /code/

EXPOSE 8000
EXPOSE 5555