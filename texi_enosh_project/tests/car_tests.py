import pytest
from pymongo.collection import Collection
from repository.mongoDB_repository import MongoDBRepository


@pytest.fixture(scope="function")
def cars_collection(init_test_data):
   return init_test_data['cars']


def test_get_all(cars_collection: Collection):
   test_car_repo = MongoDBRepository(cars_collection)
   res = list(test_car_repo.get_all())
   assert len(res) == 30


