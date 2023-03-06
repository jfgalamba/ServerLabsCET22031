from fastapi import APIRouter
from fastapi_chameleon import template

router = APIRouter()

@router.get('/')                            # type: ignore
@template()
async def index(course1: str = 'N/D'):
    return {
        'course1': course1,
        'course2': 'Biogenética Aplicada',
        'course3': 'Pesca de Grande Porte',
    }
#:

@router.get('/about')                        # type: ignore
@template()
async def about():
    return {}
#:
