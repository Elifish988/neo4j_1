from elasticsearch import Elasticsearch
import csv

CLOUD_URL = 'http://localhost:9200'
USER_NAME = 'elastic'
PASSWORD = 'fZBPZqGF'

es = Elasticsearch(
    CLOUD_URL,
    basic_auth=(USER_NAME, PASSWORD)
)

def create_index():
    # אם האינדקס קיים, מוחקים אותו
    if es.indices.exists(index="tweets_db"):
        es.indices.delete(index="tweets_db")

    # יוצרים אינדקס חדש
    es.indices.create(
        index='tweets_db',
        body={
            'mappings': {
                'dynamic': 'strict',
                "properties": {
                    "sentiment": {"type": "text"},
                    "tweet_id": {"type": "text"},
                    "user_id": {"type": "text"},
                    "tweet_date": {
                        "type": "text"
                    },
                    "username": {"type": "keyword"},
                    "tweet_content": {"type": "text"}
                }
            }
        }
    )