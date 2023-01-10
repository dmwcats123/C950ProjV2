import datetime

import csv
from Package import Package
from HashTable import Hashmap
from Truck import Truck

with open("CSV/Distances.csv") as csv_distance_data:
    csv_distance = csv.reader(csv_distance_data)
    csv_distance = list(csv_distance)

with open("CSV/Addresses.csv") as csv_address_data:
    csv_address = csv.reader(csv_address_data)
    csv_address = list(csv_address)

with open("CSV/Packages.csv") as csv_package_data:
    csv_package = csv.reader(csv_package_data)
    csv_package = list(csv_package)

package_hashmap = Hashmap()


# Loads the package data from the CSV into a hashmap using ID at the key
def load_packages_to_hash(file):
    with open(file) as package_data:
        package_list = csv.reader(package_data)
        for package in package_list:
            id = package[0]
            address = package[1]
            city = package[2]
            state = package[3]
            zip_code = package[4]
            deadline = package[5]
            weight = package[6]
            status = "At Hub"

            package_object = Package(id, address, city, state, zip_code, deadline, weight, status)
            package_hashmap.insert(id, package_object)


#manually load trucks
truck_one = Truck(16, 18, None, [1, 13, 14, 15, 16, 20, 29, 30, 31, 34, 37, 40], "4001 South 700 East",
                  datetime.timedelta(hours=8))
truck_two = Truck(16, 18, None, [3, 6, 12, 17, 18, 19, 21, 22, 23, 24, 26, 27, 35, 36, 38, 39],
                  "4001 South 700 East", datetime.timedelta(hours=10, minutes=20))

truck_three = Truck(16, 18, None, [2, 4, 5, 6, 7, 8, 9, 10, 11, 25, 28, 32, 33], "4001 South 700 East",
                    datetime.timedelta(hours=9, minutes=5))

trucks = [truck_one, truck_two, truck_three]


#Simulate delivery of the packages on the trucks
def deliver_packages():
    for truck in trucks:
        unsorted_copy = []
        for package_id in truck.packages:
            package = package_hashmap.lookup(str(package_id))
            unsorted_copy.append(package)
        truck.packages.clear()
        while len(unsorted_copy) > 0:
            distance_next=1000000
            next_package = None
            for package in unsorted_copy:
                if distance_between(index_address(truck.address), index_address(package.address)) <= distance_next:
                    next_package = package
                    distance_next = distance_between(index_address(truck.address), index_address(package.address))
            truck.packages.append(next_package.id)
            unsorted_copy.remove(next_package)
            truck.mileage += distance_next
            truck.address = next_package.address
            truck.time += datetime.timedelta(hours=distance_next / 18)
            next_package.delivered_time = truck.time


# index the addresses from the csv file by the id numbers
def index_address(address):
    for row in csv_address:
        if address in row[2]:
            return int(row[0])


# determine the distance between two addresses based on their index
def distance_between(addressIndexOne, addressIndexTwo):
    distance = csv_distance[addressIndexOne][addressIndexTwo]
    if distance == '':
        distance = csv_distance[addressIndexTwo][addressIndexOne]
    return float(distance)


load_packages_to_hash("csv/Packages.csv")
deliver_packages()


#CLI is implemented in Main
class Main:
    print("Total Mileage: " + str(truck_one.mileage + truck_two.mileage + truck_three.mileage))
    print("\nWGUPS\n")
    print("Choose one of the following options:\n1. See status of all packages\n2. See status of a specific package\n")
    user_input = input("Enter 1 or 2: ")
    time_input = input("What time is it? Use HH:MM:SS: ")
    (h, m, s) = time_input.split(":")
    timedelta = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))

    if user_input == "1":
        for package_id in range(1, 41):
            package = package_hashmap.lookup(str(package_id))

            package.check_delivered(timedelta)
            print(str(package))
    elif user_input == "2":
        package_input = input("Enter the package ID: ")
        package = package_hashmap.lookup(package_input)

        package.check_delivered(timedelta)
        print(str(package))
