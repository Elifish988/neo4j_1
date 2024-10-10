import csv

from database.connect import taxi_db, drivers, cars
from repository.mongoDB_repository import MongoDBRepository


def read_csv(csv_path):
   with open(csv_path, 'r') as file:
       csv_reader = csv.DictReader(file)
       for row in csv_reader:
           yield row

car_repo = MongoDBRepository(cars)
driver_repo = MongoDBRepository(drivers)


def init_taxi_drivers():

   drivers.drop()
   cars.drop()


   for row in read_csv(r"C:\Users\Eli Fishman\Data\Python\texi_enosh_project\data\practice_data.csv"):
       car = {
           'license_id': row['CarLicense'],
           'brand': row['CarBrand'],
           'color': row['CarColor']
       }


       car_id = car_repo.add(car)


       address = {
           'city': row['City'],
           'street': row['Street'],
           'state': row['State']
       }


       driver = {
           'passport': row['PassportNumber'],
           'first_name': row['FullName'].split(' ')[0],
           'last_name': row['FullName'].split(' ')[1],
           'car_id': car_id,
           'address': address
       }


       driver_repo.add(driver)
