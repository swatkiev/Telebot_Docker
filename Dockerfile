FROM python:3.9-alpine

RUN pip install requests && pip install pyTelegramBotAPI

WORKDIR /opt/telebot

COPY run.py /opt/telebot

CMD ["python", "run.py"]
