from fastapi import APIRouter
from fastapi_chameleon import template

from common import base_viewmodel_with
from services import course_service 

router = APIRouter()

AVAILABLE_COURSES_COUNT = 5

@router.get('/courses')                            # type: ignore
@template()
async def courses():
    return courses_viewmodel()
#:

def courses_viewmodel():
    return base_viewmodel_with({
        'available_courses': course_service.available_courses(AVAILABLE_COURSES_COUNT)
    })
#:

@router.get('/courses/{course_id}')                            # type: ignore
@template()
async def course_details(course_id: int):
    return course_details_viewmodel(course_id)
#:

def course_details_viewmodel(course_id: int):
    course = next((c for c in course_service.available_courses() if c.id == course_id), None)
    if course: 
        return base_viewmodel_with({'course': course})
    return base_viewmodel_with({
        'error': True,
        'error_msg': 'Course not found'
    })
#:

