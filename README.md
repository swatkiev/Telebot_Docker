# Telebot_Docker Конвертация курсов валют в Телеграмм боте
Создайте чат бота в телеграмме с помощью @BotFather с уникальным именем и идентификатором, который вставьте в переменную BOT_TOKEN в файле run.py
Установите на хосте Docker по официальной документации, выбрав необходимый дистрибутив: https://docs.docker.com/engine/install/
Выполните последовательно команды, находясь в директории с Dockerfile: "docker build -t telebot ." и "docker run --name telebot --restart="always" -d telebot"
Укажите в файле script.sh вашу директорию с месторасположением и добавьте скрипт в cron на выполнение каждый день утром, например: 00 10 * * * /home/dockerbot/script.sh
