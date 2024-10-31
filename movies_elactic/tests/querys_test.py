from tests.conftest import movies_index


def test_title_has_m(bulk_movies_data, es_client):
   res = es_client.search(index=movies_index, body={
       "query": {
           "match": {
               "title": "m"
           }
       }
   })
   assert res.body['hits']['total']['value'] > 0



def test_multi_fields_has_a(bulk_movies_data, es_client):
   res = es_client.search(index=movies_index, body={
       "query": {
           "multi_match": {
               "query": "a",
               "fields": ["title", "genres"]
           }
       }
   })
   assert res.body['hits']['total']['value'] > 0


def test_multi_fields_has_phrase(bulk_movies_data, es_client):
   res = es_client.search(index=movies_index, body={
       "query": {
           "multi_match": {
               "query": "Dead Man",
               "fields": ["title", "genres"],
               "type": "phrase"
           }
       }
   })
   for row in res:
       print(res.body['hits']['hits'][0]['_source'])
   assert res.body['hits']['total']['value'] > 0



def test_match_phrase(bulk_movies_data, es_client):
   res = es_client.search(index=movies_index, body={
       "query": {
           "match_phrase": {
               "title": "The "
           }
       }
   })
   for row in res:
       print(res.body['hits']['hits'][0]['_source'])
   assert res.body['hits']['total']['value'] > 0


def test_wild_card(bulk_movies_data, es_client):
   res = es_client.search(index=movies_index, body={
       "query": {
           "wildcard": {
               "title": "*he"
           }
       }
   })
   for row in res:
       print(res.body['hits']['hits'][0]['_source'])
   assert res.body['hits']['total']['value'] > 0



def test_fuzzy(bulk_movies_data, es_client):
   res = es_client.search(index=movies_index, body={
       "query": {
           "fuzzy": {
               "title": {
                   "value": "matruךx",
                   "fuzziness": "AUTO"
               }
           }
       }
   })
   for row in res:
       print(res.body['hits']['hits'][0]['_source'])
   assert res.body['hits']['total']['value'] > 0

def test_movie_id_range(bulk_movies_data, es_client):
   res = es_client.search(index=movies_index, body={
       "query": {
           "range": {
               "movieId": {
                   "gt": 10,
                   "lt": 40
               }
           }
       }
   })
   for i in res.body['hits']['hits']:
       print(i['_source'])
   assert res.body['hits']['total']['value'] > 0



def test_should_match(bulk_movies_data, es_client):
   res = es_client.search(index=movies_index, body={
       "query": {
           "bool": {
               "should": [
                   {"match": {"genres": "Drama"}},
                   {"match": {"title": "Love"}}
               ]
           }
       }
   })
   for i in res.body['hits']['hits']:
       print(i['_source'])
   assert res.body['hits']['total']['value'] > 0


def test_should_wildcard(bulk_movies_data, es_client):
   res = es_client.search(index=movies_index, body={
       "query": {
           "bool": {
               "should": [
                   {"wildcard": {"genres": "*rama"}},
                   {"wildcard": {"title": "Lov*"}}
               ]
           }
       }
   })
   for i in res.body['hits']['hits']:
       print(i['_source'])
   assert res.body['hits']['total']['value'] > 0