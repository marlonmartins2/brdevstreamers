from dotenv import dotenv_values
from peewee import *
from playhouse.migrate import *

from model.reward_model import Reward
from model.user_interaction_model import UserInteraction
from model.user_model import User

config = dotenv_values(".env")

db = PostgresqlDatabase(config['DB_NAME'], user=config['DB_USER'],
                           password=config['DB_PASS'], host=config['DB_HOST'], port=config['DB_PORT'])


def init_db():
    db.connect(reuse_if_open=True)
    db.create_tables([User, UserInteraction, Reward])
    db.close()
