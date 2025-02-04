from enum import unique

from dotenv import dotenv_values
from peewee import *

config = dotenv_values(".env")

db = PostgresqlDatabase(config['DB_NAME'], user=config['DB_USER'],
                           password=config['DB_PASS'], host=config['DB_HOST'], port=config['DB_PORT'])

class UserInteraction(Model):
    user_login= CharField(null=False)
    target_user = CharField(null=True)
    date = DateField(null=False)
    type = CharField(null=False)
    interaction_fingerprint = CharField(null=False)

    class Meta:
        database = db