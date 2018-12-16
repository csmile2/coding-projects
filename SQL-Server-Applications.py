#  project 3   -  MCS275  -  Danko Adrvic
#  create a SQLite database given a CSV file about cars
#  11/21/2018  -  Clayton A. Smiley

import sqlite3
import re


def create_db():
    print("Creating database, please wait... ")
    conn = sqlite3.connect("vehicles.db")
    cursor = conn.cursor()
    sql = "CREATE TABLE IF NOT EXISTS vehicles \
        (type text, status text, make text, model text, year int, color text, fuel text, wheelchair text, city text,\
        state text, zip int)"
    cursor.execute(sql)
    cursor.close()
    print("Database successfully created!")


def add_data():
    conn = sqlite3.connect("vehicles.db")
    cursor = conn.cursor()
    print("Adding data to the database, please wait... ")

    with open("Public_Passenger_Vehicle_Licenses.csv", 'r') as f:
        for line in f:
            if not line.startswith("Vehicle Type"):
                L = line.split(",")
                vehicle_type = L[0]
                vehicle_status = L[1]
                make = L[2]
                model = L[3]
                year = L[4]
                color = L[5]
                fuel = L[6]
                wheelchair = L[7]
                city = L[8]
                state = L[9]
                zip = int(L[10])
                sql = "INSERT INTO vehicles (type, status, make, model, year, color, fuel, wheelchair, city, state, zip)" \
                      "VALUES (:vehicle_type, :vehicle_status, :make, :model, :year, :color, :fuel, :wheelchair, :city, \
                      :state, :zip)"
                cursor.execute(sql, {"vehicle_type": vehicle_type, "vehicle_status": vehicle_status, "make": make,
                                     "model": model, "year": year, "color": color, "fuel": fuel, "wheelchair": wheelchair,
                                     "city": city, "state": state, "zip": zip})
                conn.commit()
    cursor.close()


# find the number of hybrid vehicles in this data set
def computeHybrids():
    conn = sqlite3.connect("vehicles.db")
    cursor = conn.cursor()
    sql = "select count(*) from vehicles where fuel == 'Hybrid'"
    hybridCount = cursor.execute(sql)
    hybrids = str(hybridCount.fetchall()).replace("[(","").replace(",)]","")
    hybrids = int(hybrids)
    sql2 = "select count(*) from vehicles"
    totalCount = cursor.execute(sql2)
    totalCount = str(totalCount.fetchall()).replace("[(","").replace(",)]","")
    totalCount = int(totalCount)
    print("2. Percentage of hybrids is: %f" % (round((hybrids/totalCount),8)*100))
    cursor.close()


def avgAge():

    conn = sqlite3.connect("vehicles.db")
    cursor = conn.cursor()

    sql = "select avg(year) from vehicles where status != 'INACTIVE'"
    years = cursor.execute(sql)
    yearList = list(years)
    average_age = yearList[0][0]
    # average_age = average_age.replace("[(","").replace(",)]","")
    print("3. The average age of the vehicles is %i years" % (2018.0-float(average_age)))  # note use regex to strip
    cursor.close()
    # print("3. The average of the cars is about %f years old" % (yearList[0]-2018))

def findNumberOfModels():

    conn = sqlite3.connect("vehicles.db")
    cursor = conn.cursor()

    sql = "SELECT distinct model from vehicles"
    vehicles = cursor.execute(sql)
    vehicles = list(vehicles)
    print("4. There are %i different models of vehicles." % len(vehicles))
    cursor.close()


def mostCommonVehicle():
    conn = sqlite3.connect("vehicles.db")
    cursor = conn.cursor()

    #  trying to maintain some semblance of sql query neatness lol
    sql = "select model, " \
          "COUNT(model) " \
          "AS number_of_vehicles " \
          "FROM vehicles " \
          "GROUP BY model " \
          "ORDER BY " \
          "number_of_vehicles DESC"
    most_common_vehicles = cursor.execute(sql)
    most_common_vehicles = list(most_common_vehicles)
    # print(most_common_vehicles)
    print("5. The most common vehicle is the %s with %s instances of that vehicle" % (most_common_vehicles[0][0],
                                                                                   most_common_vehicles[0][1]))
    cursor.close()


def mostCommonCities():

    conn = sqlite3.connect("vehicles.db")
    cursor = conn.cursor()
    sql = "select city, COUNT(city) AS \"city_count\" FROM vehicles GROUP BY city ORDER BY \"city_count\" DESC"
    common_cities = cursor.execute(sql)
    common_cities = list(common_cities)
    print("6. The second-most common city for registered vehicles is %s with %s registrants." % (common_cities[1][0],
                                                                                              common_cities[1][1]))
    cursor.close()


def findZipCodes():
    conn = sqlite3.connect("vehicles.db")
    cursor = conn.cursor()

    sql = "select zip, COUNT(zip) AS \"zip_count\" FROM vehicles GROUP BY zip ORDER BY \"zip_count\" DESC"
    zip_codes = cursor.execute(sql)
    zip_codes = list(zip_codes)
    # print(zip_codes)
    print("7. The most common zip code is %s, with %s registrants" % (zip_codes[0][0], zip_codes[0][1]))
    cursor.close()


def main():
    create_db()
    add_data()
    print("1. The size of the database is 837 kB")
    computeHybrids()
    avgAge()
    findNumberOfModels()
    mostCommonVehicle()
    mostCommonCities()
    findZipCodes()


main()
