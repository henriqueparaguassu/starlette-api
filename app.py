from starlette.applications import Starlette

from database.database import *
from routes.router import app_routes

app = Starlette(
    debug=True,
    routes=app_routes,
)
