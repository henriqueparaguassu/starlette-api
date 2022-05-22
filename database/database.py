from peewee import (
    CharField,
    DateField,
    FloatField,
    IntegerField,
    Model,
    SqliteDatabase,
)

db = SqliteDatabase("movie.db")


class Movie(Model):
    title = CharField()
    year = IntegerField()
    director = CharField()
    rating = FloatField()
    votes = IntegerField()
    runtime = IntegerField()
    genre = CharField()
    plot = CharField()

    class Meta:
        database = db
        table_name = "movies"


db.connect()
db.create_tables([Movie])
