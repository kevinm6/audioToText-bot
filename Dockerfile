FROM alpine:latest
MAINTAINER kevin m

# Bootstrap
RUN apk -U upgrade
RUN apk add --no-cache git wget python3 ffmpeg
RUN git clone "https://github.com/kevinm6/audioToText-bot.git" /home/bot
WORKDIR /home/bot
RUN cd /home/bot

# Environment
ENV PATH="/home/bot/bin:/bin:/usr/bin:/usr/local/bin"
ENV PIP_DISABLE_PIP_VERSION_CHECK=on
ENV PIP_DEFAULT_TIMEOUT=100
ENV BOT_TOKEN "xxxx"

# Activate Environment
RUN python3 -m venv /home/bot
RUN source bin/activate

# Start
RUN pip install -r requirements.txt
RUN chmod +x transcriptBot
CMD ./transcriptBot
