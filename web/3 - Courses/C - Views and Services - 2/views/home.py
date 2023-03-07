from fastapi import APIRouter, Request
from starlette.requests import Request
from fastapi_chameleon import template

from services import course_service, student_service, trainer_service
from common import base_viewmodel_with

POPULAR_COURSES_COUNT = 3
SELECTED_COURSES_COUNT = 3
SELECTED_TRAINERS_COUNT = 3
TESTIMONIALS_COUNT = 5

router = APIRouter()

@router.get('/')                            # type: ignore
@template()
async def index(response: Request):
    return index_viewmodel()
#:

def index_viewmodel():
    return base_viewmodel_with({
        'num_courses': course_service.course_count(),
        'num_students': student_service.student_count(),
        'num_trainers': trainer_service.trainer_count(),
        'num_events': 159,
        'popular_courses': course_service.most_popular_courses(POPULAR_COURSES_COUNT),
        'selected_trainers': trainer_service.selected_trainers(SELECTED_TRAINERS_COUNT) 
    })
#:

@router.get('/about')                        # type: ignore
@template()
async def about(request: Request):
    return about_viewmodel()
#:

def about_viewmodel(): 
    return base_viewmodel_with({
        'num_courses': course_service.course_count(),
        'num_students': student_service.student_count(),
        'num_trainers': trainer_service.trainer_count(),
        'num_events': 159,
        'testimonials': student_service.get_testimonials(TESTIMONIALS_COUNT)
    })
#:


