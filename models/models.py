from peewee import *
from settings.settings import db


class User(Model):
    id = IntegerField(primary_key=True)
    username = CharField(max_length=64)

    class Meta:
        database = db
        db_table = 'User'
