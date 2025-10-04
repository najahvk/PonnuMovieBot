FROM python:3.10.8-slim-buster

RUN apt update && apt upgrade -y && apt install git -y
COPY requirements.txt /requirements.txt
RUN pip3 install -U pip && pip3 install -U -r /requirements.txt
RUN mkdir /FILTER-BOT
WORKDIR /FILTER-BOT
COPY . /FILTER-BOT
CMD ["python", "bot.py"]
