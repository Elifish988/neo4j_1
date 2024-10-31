import csv
import os


filename = os.path.join(os.path.dirname(__file__), '..', 'data', 'movies.csv')




def read_movies_csv():
   with open(filename, 'r', encoding='utf-8') as f:
       reader = csv.DictReader(f)
       for row in reader:
           yield row


