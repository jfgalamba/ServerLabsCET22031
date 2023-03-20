from datetime import date
from datetime import datetime
from decimal import Decimal as dec
from dataclasses import dataclass, field


@dataclass
class Course:
    id: int
    category: str
    price: dec
    name: str
    summary: str
    description: str
    trainer_id: int
    trainer_name: str
    schedule: str
    available_seats: int
#:

@dataclass
class Student:
    id: int
    name: str
    email: str
    password: str
    birth_date: date
    profile_image_url: str | None = None
    created_date: date = field(default_factory = date.today)
    last_login: datetime =  field(default_factory = datetime.now)
#:

@dataclass
class Trainer:
    id: int
    name: str
    expertise: str
    presentation: str
    twitter: str
    facebook: str
    instagram: str
    linkedin: str
#:

@dataclass
class Testimonial:
    user_id: int
    user_name: str
    user_occupation: str
    text: str
#:
