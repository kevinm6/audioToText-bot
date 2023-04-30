FROM alpine:latest
MAINTAINER kevin m

RUN apk -U upgrade
RUN apk add python3 wget git
RUN git clone "https://github.com/kevinm6/audioToText-bot.git" /home/bot
RUN cd /home/bot


# Environment
ENV PIP_DISABLE_PIP_VERSION_CHECK=on
ENV PIP_DEFAULT_TIMEOUT=100
ENV BOT_TOKEN "xxxx"

RUN echo "$PWD"
RUN mkdir /tmp/bot
# ADD . /bot
WORKDIR /home/bot

RUN python3 -m venv .
RUN . bin/activate
RUN bin/pip install -r requirements.txt
RUN chmod +x transcriptBot.py
RUN ls -al
