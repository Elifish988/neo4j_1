import csv
from repository.csv_repository import es
from repository.mongo_repository import get_db

def read_csv(csv_path):
    with open(csv_path, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            yield row

def init_accidents(es_client=None):
    get_db().db.drop()
    users_db = get_db().db

    try:
        for row in read_csv(r"C:\Users\Eli Fishman\Data\Python\tweet_elastic_progect\data\training.1600000.processed.noemoticon.csv"):
            user_id = int(row[2]) if row[2].isdigit() else None  # המרה למספר אם אפשרי

            # ודא שהערכים נכונים לפני הוספה לאינדקס
            es.index(index='tweets_db', body={
                'sentiment': row[0],  # ודא שהערך הוא מספר
                'tweet_id': row[1],    # ודא שהערך הוא מספר
                'user_id': user_id,          # השתמש במשתנה המעודכן
                'tweet_date': row[3],
                'username': row[4],
                'tweet_content': row[5],
            }, refresh='wait_for')

            tweet = {
                'tweet_id': row[1],
                'username': row[4]
            }

            users_db.insert_one(tweet)

    except Exception as e:
        return f"An error occurred: {e}"

    return "Processing completed successfully"

def get_all():
    res = es.search(index='tweets_db', body={
        "query": {
            "match_all": {}
        }
    })
    for i in res['hits']['hits']:
        print(i['_source'])

print(init_accidents())
get_all()
