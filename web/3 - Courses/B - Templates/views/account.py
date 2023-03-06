from fastapi import APIRouter
from fastapi_chameleon import template

router = APIRouter()

@router.get('/account')                            # type: ignore
async def index():
    return {}
#:

@router.get('/account/login')                            # type: ignore
async def login():
    return {}
#:

@router.get('/account/register')                            # type: ignore
async def register():
    return {}
#: