# Car Parsers Project

Парсинг автомобилей с сайта auto.ru через undetected_chromedriver.

- Python 3.10+
- venv
- requirements.txt

Запуск:
python3 main.py


## loacal start
- python3 -m venv venv
- source venv/bin/activate   
- pip install -r requirements.txt
- python3 main.py

## docker start
- docker build -t auto_parser .
- docker run --rm -v $(pwd)/excel_storage:/app/excel_storage auto_parser

# Подойдёт любой Linux VPS (например, Ubuntu 20.04 / 22.04).

## 1
На сервере должны быть:
	•	установлен git
	•	установлен docker
	•	установлен docker-compose (по желанию, но лучше)

curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

sudo apt-get install -y docker-compose

## 2 Склонируй проект на сервер
git clone https://github.com/aleksandrmajlo/auto_parser.git
cd auto_parser

## 3 Проверь, что в проекте

## 4 Собери Docker-образ
docker build -t auto_parser .

docker-compose build

## 5 Запусти контейнер

docker run --rm -v $(pwd)/excel_storage:/app/excel_storage auto_parser

docker-compose up --build

## 6 Настрой автозапуск через cron
crontab -e

0 * * * * cd /path/to/auto_parser && docker run --rm -v $(pwd)/excel_storage:/app/excel_storage auto_parser >> cron.log 2>&1


