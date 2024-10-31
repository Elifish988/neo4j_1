from elastic_transport import SecurityWarning
from elasticsearch import Elasticsearch
import warnings
from elasticsearch.helpers import bulk
import pytest
from repository.csv_repository import read_movies_csv




warnings.filterwarnings("ignore", category=SecurityWarning)



@pytest.fixture(scope="module")
def es_client():
  client = Elasticsearch(
      ['http://localhost:9200'],
      basic_auth=("elastic", "fZBPZqGF"),
      verify_certs=False
  )
  yield client
  client.close()


movies_index = "movies"


@pytest.fixture(scope="module")
def init_movies_index(es_client):
    if es_client.indices.exists(index=movies_index):
        es_client.indices.delete(index=movies_index)

    es_client.indices.create(index=movies_index, body={
        "settings": {
            "number_of_shards": 2,
            "number_of_replicas": 2
        },
        "mappings": {
            "properties": {
                "movieId": {"type": "keyword"},
                "title": {"type": "text"},
                "genres": {"type": "text"}
            }
        }
    })
    yield
    es_client.indices.delete(index=movies_index)


@pytest.fixture(scope="module")
def bulk_movies_data(es_client, init_movies_index):
    data = [{
        '_id': f'movies{i}',
        '_index': movies_index,
        '_source': row
    } for i, row in enumerate(read_movies_csv())]

    bulk(es_client, data)



