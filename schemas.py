import atexit

from peewee import *
from playhouse.sqlite_ext import SqliteExtDatabase


PATH = "database.db"
db = SqliteExtDatabase(
    PATH,
    pragmas={"jurnal_mode": "wal"},
)
atexit.register(lambda: db.close())


class BaseModel(Model):
    class Meta:
        database = db


class Event(BaseModel):
    id = UUIDField(primary_key=True)
    title = TextField()
    description = TextField()
    link = TextField()
    location = TextField()
    price = TextField(null=True)
    topics = TextField()
    start_date = TextField()
    end_date = TextField()


db.create_tables([Event])
