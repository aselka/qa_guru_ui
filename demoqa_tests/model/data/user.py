import datetime
from dataclasses import dataclass
from datetime import date

@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    phone: str
    address: str
    birthday: datetime.date
    gender: str
    subject: str
    hobbies: str
    image: str
    state: str
    city: str


test_user = User(
    first_name='Test',
    last_name='Testov',
    email='test@test.com',
    phone='1234567890',
    address='Saratov',
    birthday=date(1995, 10, 10),
    gender='Female',
    subject='Computer Science',
    hobbies='Music',
    image='foto.jpg',
    state='NCR',
    city='Delhi')