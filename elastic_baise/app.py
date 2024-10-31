from elasticsearch import Elasticsearch

CLOUD_URL = 'http://localhost:9200'
USER_NAME = 'elastic'
PASSWORD = 'fZBPZqGF'


es = Elasticsearch(
    CLOUD_URL,
    basic_auth=(USER_NAME, PASSWORD)
)

if es.indices.exists(index="products"):
    es.indices.delete(index="products")

es.indices.create(
    index="products",
    body={
        "mappings": {
            'dynamic': 'strict',
            "properties": {
                "name": {"type": "text"},
                "category": {"type": "text"}
            }
        },
    }
)

# הכנסת מסמכים
es.index(index='products', id=1, body={'name': 'apple', 'category': 'fruit'}, refresh='wait_for')
es.index(index='products', id=2, body={'name': '1', 'category': 'fruit'}, refresh='wait_for')
es.index(index='products', id=3, body={'name': 'carrot', 'category': 'vegetable'}, refresh='wait_for')

# חיפוש מסמך עם שם apple
result_basic = es.search(index='products', query={'match': {'name': 'apple'}})

print('Elasticsearch match')
for hit in result_basic['hits']['hits']:
    print(hit['_source'])

print(result_basic)



#חיפוש עם שגיאה
# result_basic = es.search(index= 'products', query={'fuzzy': {'name': 'appel'}})

# fuzziness - כמות שגיאות מותרת    prefix_length - כמה תווים ראשונים צריכים להיות זהים
# result_basic = es.search(index='products', query={'fuzzy': {'name': {'value': 'apple', 'fuzziness': 2, 'prefix_length': 0}}})


# print('Elasticsearch match')
# for hit in result_basic['hits']['hits']:
#     print(hit['_source'])


