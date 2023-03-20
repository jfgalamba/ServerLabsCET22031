from fastapi import (
    FastAPI, 
    status,
    responses,
)
from fastapi.staticfiles import StaticFiles

from chameleon import PageTemplateFile
from fastapi_chameleon import global_init

from views import (
    home,
    courses,
    account,
)
from common.fastapi_utils import add_global_request_middleware
from common.auth import (
    HTTPUnauthorizedAccess,
    HTTPUnauthenticatedOnly,
)
from common.viewmodel import ViewModel


TEMPLATES_DIR_PATH = './templates'
TEMPLATES_ERROR_PATH = f'{TEMPLATES_DIR_PATH}/errors'

app = FastAPI()

def main():
    config()
    start_uvicorn()
#:

def config():
    print("[+] Configuring server")
    config_middleware()
    print("[+] ...middleware configured")
    config_templates()
    print("[+] ...templates configured")
    config_exception_handlers()
    print("[+] ...exception handlers configured")
    config_routes()
    print("[+] ...routes configured")
    print("[+] ...done configuring server")
#:

def config_middleware():
    add_global_request_middleware(app)
#:

def config_templates(): 
    global_init(TEMPLATES_DIR_PATH)
#:

def config_exception_handlers():
    async def unauthorized_access_handler(*_, **__):
        template = PageTemplateFile(f'{TEMPLATES_ERROR_PATH}/404.pt')
        content = template(**ViewModel())
        return responses.HTMLResponse(content, status_code = status.HTTP_404_NOT_FOUND)
    #:
    async def unauthenticated_only_area_handler(*_, **__):
        return responses.RedirectResponse(url = '/', status_code = status.HTTP_302_FOUND)
    #:
    app.add_exception_handler(HTTPUnauthorizedAccess, unauthorized_access_handler)
    app.add_exception_handler(status.HTTP_404_NOT_FOUND, unauthorized_access_handler)
    app.add_exception_handler(HTTPUnauthenticatedOnly, unauthenticated_only_area_handler)
#:

def config_routes():
    app.mount('/static', StaticFiles(directory='static'), name='static')
    for view in [home, courses, account]:
        app.include_router(view.router)
#:

def start_uvicorn():
    import uvicorn
    from docopt import docopt
    help_doc = """
FastAPI Web server for the course management Web App.

Usage:
  main.py [-p PORT] [-h HOST_IP] [-r]

Options:
  -p PORT, --port=PORT          Listen on this port [default: 8000]
  -h HOST_IP, --host=HOST_IP    Listen on this IP address [default: 127.0.0.1]
  -r, --reload                  Reload app
"""
    args = docopt(help_doc)

    uvicorn.run(
        'main:app',
        port = int(args['--port']), 
        host = args['--host'],
        reload = args['--reload'],
        reload_includes=[
            '*.pt',
            '*.css',
        ]
    )
#:

if __name__ == '__main__':
    main()
else:
    config()
#:
