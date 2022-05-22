from controllers.movie import movie_controller
from starlette.endpoints import HTTPEndpoint
from starlette.requests import Request
from starlette.responses import JSONResponse


class Movie(HTTPEndpoint):
    async def get(self, request: Request):
        """
        responses:
        200:
            description: A list of movies.
            examples:
                [{"id": 1, "title": "The Shawshank Redemption", "year": 1994, "director": "Frank Darabont", "rating": 9.3, "votes": 914098, "runtime": 142, "genre": "Crime", "plot": "Two imprisoned"}]
        """
        movies = movie_controller.get_all()
        return JSONResponse(movies, status_code=200)

    async def post(self, request: Request):
        movie = await request.json()
        movie_controller.create(movie)
        return JSONResponse(movie, status_code=201)

    async def put(self, request: Request):
        id = request.query_params.get("id")
        movie = await request.json()
        movie_controller.update(id, movie)
        return JSONResponse(movie, status_code=200)

    async def delete(self, request: Request):
        id = request.query_params.get("id")
        id_deleted = movie_controller.delete(id)
        return JSONResponse({"id": id_deleted}, status_code=204)

    async def get_by_id(self, request: Request):
        id = request.query_params.get("id")
        movie = movie_controller.get_by_id(id)
        return JSONResponse(movie, status_code=200)
