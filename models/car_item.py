from dataclasses import dataclass

@dataclass
class CarItem:
    title: str
    price: str
    year: int
    mileage: str
    location: str
    link: str