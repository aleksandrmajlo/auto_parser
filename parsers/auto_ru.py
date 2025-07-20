import undetected_chromedriver as uc
from bs4 import BeautifulSoup
from models.car_item import CarItem
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AutoRuParser:
    def __init__(self):

        options = uc.ChromeOptions()
        options.binary_location = '/usr/bin/chromium'  # путь к chromium в контейнере
        options.add_argument('--headless=new')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--disable-gpu')
        options.add_argument('--disable-software-rasterizer')
        options.add_argument('--remote-debugging-port=9222')

        self.driver = uc.Chrome(
            options=options,
            driver_executable_path='/usr/bin/chromedriver'  # путь к chromedriver в контейнере
)


    def parse(self, search_url):
        self.driver.get("https://auto.ru/")
        time.sleep(2)

        self.driver.add_cookie({
            'name': 'autoru_gdpr',
            'value': '1',
            'domain': '.auto.ru',
            'path': '/',
            'secure': True
        })  

        self.driver.get(search_url)

        # Дождаться, пока появятся элементы
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "ListingItem"))
        )
        html = self.driver.page_source



        with open('page/auto_ru.html', 'w', encoding='utf-8') as f:
            f.write(html)

        soup = BeautifulSoup(html, 'lxml')

        cars = []

        for item in soup.select('div.ListingItem'):
            title_tag = item.select_one('a.ListingItemTitle__link')
            price_tag = item.select_one('div.ListingItemPrice__content')
            year_tag = item.select_one('div.ListingItemYear__content')
            mileage_tag = item.select_one('div.ListingItemMileage__content')
            location_tag = item.select_one('div.ListingItemRegion__content')

            title = title_tag.get_text(strip=True) if title_tag else 'N/A'
            price = price_tag.get_text(strip=True) if price_tag else 'N/A'
            year = int(year_tag.get_text(strip=True)) if year_tag else None
            mileage = mileage_tag.get_text(strip=True) if mileage_tag else 'N/A'
            location = location_tag.get_text(strip=True) if location_tag else 'N/A'
            link = title_tag['href'] if title_tag else 'N/A'

            cars.append(CarItem(title, price, year, mileage, location, link))

        return cars

    def close(self):
        self.driver.quit()