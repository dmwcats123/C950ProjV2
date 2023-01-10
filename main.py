import datetime

import csv
from Package import Package
from HashTable import Hashmap

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


def index_address(address):
    for row in csv_address:
        if address in row[2]:
            return int(row[0])

def distance_between(addressIndexOne, addressIndexTwo):
    distance = csv_distance[addressIndexOne][addressIndexTwo]
    if distance == '':
        distance = csv_distance[addressIndexTwo][addressIndexOne]
    return float(distance)


load_packages_to_hash("csv/Packages.csv")

class Main:
    print("WGUPS")
    print("Choose one of the following options:\n1. See status of all packages\n2. See status of a specific package\n")
    user_input = input("Enter 1 or 2: ")
    time_input = input("What time is it? Use HH:MM:SS: ")
    (h, m, s) = time_input.split(":")
    timedelta = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))

    if user_input == "1":
        for package_id in range(1,41):
            package = package_hashmap.lookup(str(package_id))

            package.check_delivered(timedelta)
            print(str(package))
    elif user_input == "2":
        package_input = input("Enter the package ID: ")
        package = package_hashmap.lookup(package_input)

        package.check_delivered(timedelta)
        print(str(package))





