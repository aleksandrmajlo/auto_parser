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