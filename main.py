from parsers.auto_ru import AutoRuParser
from storage.excel_storage import save_to_excel

def main():
    search_url = 'https://auto.ru/cars/all/?utm_referrer=https%3A%2F%2Fauto.ru%2Fcars%2Fall%2F'
    parser = AutoRuParser()
    cars = parser.parse(search_url)
    if  cars:
        save_to_excel(cars)
    parser.close()

if __name__ == "__main__":
    main()