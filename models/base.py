from peewee import *
from playhouse.db_url import connect
from tornado.options import options
from playhouse.pool import PooledMySQLDatabase
print(options.env)
db = connect(f'mysql+pool://{options.DB_USERNAME}:{options.DB_PASSWORD}@'
             f'{options.DB_HOST}/{options.DB_NAME}?max_connections=100&stale_timeout=300')


class BaseModel(Model):
    id = IntegerField(primary_key=True)
    username = CharField(max_length=64)

    class Meta:
        database = db