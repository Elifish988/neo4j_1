import pytest
from pymongo.collection import Collection


def test_user(users_db: Collection):
    users_db.insert_many([
        {'name': 'eli'},
        {'name': 'jack'}
    ])

    # כאן אין צורך בפרמטר השני כי ברירת המחדל היא להחזיר את כל השדות
    assert all('name' in user for user in list(users_db.find({})))


# @pytest.fixture
# def side_effects():
#     print('hello!!!')
#     yield
#     print('bye!!!')
#
#
# def test_greeting(side_effects):
#     print('eli')
#
#
# @pytest.fixture
# def get_user():
#     return {'name': 'eli'}
#
#
#
#
# def test_user(get_user):
#     print(get_user)
#     assert 'name' in get_user
#     assert get_user['name']
#
#
# def test_dog():
#     print('dog')
#     dog = {'breed': 'doberman'}
#     assert dog['breed'] == 'doberman'
#     assert dog