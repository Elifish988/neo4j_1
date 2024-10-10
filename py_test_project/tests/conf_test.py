import pytest
from pymongo import MongoClient
from pymongo.collection import Collection


@pytest.fixture
def init_db():
    client = MongoClient('localhost', 27017)
    test_db = client['test_db']
    yield test_db
    client.drop_database('test_db')
    client.close()


@pytest.fixture
def users_db(init_db):
    return init_db['users']


def test_users(users_db: Collection):
    users_db.insert_one({'name': 'eli'})
    users = users_db.find({'name': 'eli'})
    return users