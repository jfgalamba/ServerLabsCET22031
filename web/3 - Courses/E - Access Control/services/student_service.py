from datetime import date
from random import randrange
from typing import List

from data.models import (
    Student,
    Testimonial, 
)
from common.common import (
    is_valid_email,
    find_in,
)


_students = []

def student_count() -> int:
    return 2315
#:

def create_account(
        name: str,
        email: str,
        password: str,
        birth_date: date,
):
    student = Student(
        randrange(10_000, 100_000),  # id
        name,
        email,
        hash_password(password),
        birth_date,
    )
    _students.append(student)
    return student
#:

def update_account(
        id: int,
        current_password: str,
        email: str | None = None,
        new_password: str | None = None,
) -> Student:
    if not (student := get_student_by_id(id)):
        raise ValueError(f'Invalid id {id}.')
    if not password_matches(student, current_password):
        raise ValueError(f"Password doesn't match.")
    student.email = email if email else student.email
    student.password = hash_password(new_password) if new_password else student.password
    return student
#:

def get_student_by_email(email: str) -> Student | None:
    if not is_valid_email(email):
        raise ValueError(f'Invalid email address: {email}')
    return find_in(_students, lambda student: student.email == email)
           # em JS: _students.find(student => student.email === email)
#:

def get_student_by_id(student_id: int) -> Student | None:
    return find_in(_students, lambda student: student.id == student_id)
#:

def authenticate_student_by_email(email: str, password: str) -> Student | None:
    if not is_valid_email(email):
        raise ValueError(f'Invalid email address: {email}')
    if student := get_student_by_email(email):
        if password_matches(student, password):
            return student
    return None
#:

def password_matches(student: Student, password: str) -> bool:
    return student.password == hash_password(password)
#:

def get_testimonials(count: int) -> List[Testimonial]:
    return [
        Testimonial(
            user_id = 239,
            user_name = 'Saul Goodman',
            user_occupation = 'CEO & Founder',
            text = 'Quidem odit voluptate, obcaecati, explicabo nobis corporis perspiciatis nihil doloremque eius omnis officia voluptates, facere saepe quas consequatur aliquam unde. Ab numquam reiciendis sequi.',
        ),
        Testimonial(
            user_id = 1001,
            user_name = 'Sara Wilson',
            user_occupation = 'Designer',
            text = 'Export tempor illum tamen malis malis eram quae irure esse labore quem cillum quid cillum eram malis quorum velit fore eram velit sunt aliqua noster fugiat irure amet legam anim culpa.',
        ),
        Testimonial(
            user_id = 704,
            user_name = 'Jena Karlis',
            user_occupation = 'Store Owner',
            text = 'Enim nisi quem export duis labore cillum quae magna enim sint quorum nulla quem veniam duis minim tempor labore quem eram duis noster aute amet eram fore quis sint minim.',
        ),
        Testimonial(
            user_id = 1002,
            user_name = 'Matt Brandon',
            user_occupation = 'Freelancer',
            text = 'Fugiat enim eram quae cillum dolore dolor amet nulla culpa multos export minim fugiat minim velit minim dolor enim duis veniam ipsum anim magna sunt elit fore quem dolore labore illum veniam.',
        ),
        Testimonial(
            user_id = 1589,
            user_name = 'John Larson',
            user_occupation = 'Entrepreneur',
            text = 'Quis quorum aliqua sint quem legam fore sunt eram irure aliqua veniam tempor noster veniam enim culpa labore duis sunt culpa nulla illum cillum fugiat legam esse veniam culpa fore nisi cillum quid.',
        ),
    ][:count]
#:

def hash_password(password: str) -> str:
    return password + '-hashpw'
#:
