from starlette.routing import Route
from starlette.schemas import SchemaGenerator

from .endpoints.movie import Movie

schemas = SchemaGenerator(
    {"openapi": "3.0.0", "info": {"title": "Movie API", "version": "1.0"}}
)

def openapi_schema(request):
    return schemas.OpenAPIResponse(request)

app_routes = [
    Route("/movies", Movie),
    Route("/schema", openapi_schema, include_in_schema=False),
]
