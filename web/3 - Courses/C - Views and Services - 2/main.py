from fastapi import FastAPI
from fastapi_chameleon import global_init
from fastapi.staticfiles import StaticFiles
import uvicorn

from views import (
    home,
    courses,
    account,
)

app = FastAPI()

def main():
    config()
    start_uvicorn()
#:

def config():
    print("[+] Configuring server")
    config_routes()
    print("[+] ...routes configured")
    config_templates()
    print("[+] ...templates configured")
    print("[+] ...done configuring server")
#:

def config_templates(): 
    global_init('templates')
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
