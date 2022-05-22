from database.database import Movie


class MovieController:
    def to_json(self, movie):
        return {
            "id": movie.id,
            "title": movie.title,
            "year": movie.year,
            "director": movie.director,
            "rating": movie.rating,
            "votes": movie.votes,
            "runtime": movie.runtime,
            "genre": movie.genre,
            "plot": movie.plot,
        }

    def get_all(self):
        movies = Movie.select()
        movies_json = []

        for movie in movies:
            movies_json.append(self.to_json(movie))

        return movies_json

    def get_by_id(self, id):
        movie = Movie.get_by_id(id)
        return self.to_json(movie)

    def create(self, new_movie):
        movie = Movie.create(**new_movie)
        return movie.id

    def update(self, id, updated_movie):
        movie = Movie.get_by_id(id)
        movie.title = updated_movie["title"]
        movie.year = updated_movie["year"]
        movie.director = updated_movie["director"]
        movie.rating = updated_movie["rating"]
        movie.votes = updated_movie["votes"]
        movie.runtime = updated_movie["runtime"]
        movie.genre = updated_movie["genre"]
        movie.plot = updated_movie["plot"]
        movie.save()

        return self.to_json(movie)

    def delete(self, id):
        movie = Movie.get_by_id(id)
        movie.delete_instance()
        return movie.id

    def get_with_filter(
        self,
        title=None,
        min_year=None,
        max_year=None,
        min_rating=None,
        max_rating=None,
        min_votes=None,
        max_votes=None,
        min_runtime=None,
        max_runtime=None,
        genre=None,
        director=None,
    ):
        movies = Movie.select()

        if title:
            movies = movies.where(Movie.title == title)

        if min_year:
            movies = movies.where(Movie.year >= min_year)

        if max_year:
            movies = movies.where(Movie.year <= max_year)

        if min_rating:
            movies = movies.where(Movie.rating >= min_rating)

        if max_rating:
            movies = movies.where(Movie.rating <= max_rating)

        if min_votes:
            movies = movies.where(Movie.votes >= min_votes)

        if max_votes:
            movies = movies.where(Movie.votes <= max_votes)

        if min_runtime:
            movies = movies.where(Movie.runtime >= min_runtime)

        if max_runtime:
            movies = movies.where(Movie.runtime <= max_runtime)

        if genre:
            movies = movies.where(Movie.genre == genre)

        if director:
            movies = movies.where(Movie.director == director)

        movies_json = []

        for movie in movies:
            movies_json.append(self.to_json(movie))

        return movies_json


movie_controller = MovieController()
