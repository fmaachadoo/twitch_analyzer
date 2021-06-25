# syntax=docker/dockerfile:1
FROM python:3.10-rc-buster

# set working directory
WORKDIR /var/www/twitch_analyzer
COPY . .

WORKDIR /var/www/twitch_analyzer/twitch_analyzer

ENV PYTHONUNBUFFERED=1

RUN pip install -r ../requirements.txt

ADD . .



