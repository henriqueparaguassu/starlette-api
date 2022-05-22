from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.routing import Route


async def homepage(request: Request):
    body = await request.json()
    return JSONResponse({'req': body})


routes = [
    Route("/", homepage)
]

app = Starlette(debug=True, routes=routes)
