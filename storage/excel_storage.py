from openpyxl import Workbook
from models.car_item import CarItem
import datetime
import os 
def save_to_excel(car_list):
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    print(base_dir)
    dir=os.path.join(base_dir, 'excel_storage')
    if not os.path.exists(dir):
        os.makedirs(dir)

#  name file
    now = datetime.datetime.now()   
    filename = f'excars_{now.strftime("%Y%m%d_%H%M%S")}.xlsx'
    print(filename)
    filepatch=os.path.join(dir, filename)
    print(filepatch)

    wb = Workbook()
    ws = wb.active
    ws.title = 'Cars'
    # Заголовки
    ws.append(['Title', 'Price', 'Year', 'Mileage', 'Location', 'Link'])
    for car in car_list:
        ws.append([
            car.title,
            car.price,
            car.year if car.year else '',
            car.mileage,
            car.location,
            car.link
        ])

    wb.save(filepatch)