from elasticsearch import Elasticsearch

CLOUD_URL = 'http://localhost:9200'
USER_NAME = 'elastic'
PASSWORD = 'fZBPZqGF'



es = Elasticsearch(
    CLOUD_URL,
    basic_auth=(USER_NAME, PASSWORD)
)


if es.indices.exists(index="students"):
    es.indices.delete(index="students")


es.indices.create(
    index='students',
    body={
        'mappings': {
            'dynamic': 'strict',
            "properties": {
                "name": {"type": "text"},
                "age": {"type": "integer"},
                "class": {"type": "text"}
            }
        }
    }
)


es.index(index='students', id=1 , body={'name': 'shalom', 'age': 25 , 'class': 'madma"ch'})

result_1 = es.search(index='students', query={'match': {'id': 1}})

for hit in result_1['hits']['hits']:
    print(hit['_source'])


result_2 = es.update()

