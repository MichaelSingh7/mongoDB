import pymongo
import os

MONGODB_URI = os.getenv("MONGO_URI")
DBS_NAME = "test"
COLLECTION_NAME = "myTestDB"


def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could Not Connect To MongoDB: %s") % e


def show_menu():
    print("")
    print("1. Add A Record")
    print("2. Find A Record By Name")
    print("3. Edit A Record")
    print("4. Delete A Record")
    print("5. Exit")

    option = input("Enter Option ")
    return option


def main_loop():
    while True:
        option = show_menu()
        if option == "1":
            print("Option 1 Selected")
        elif option == "2":
            print("Option 2 Selected")
        elif option == "3":
            print("Option 3 Selected")
        elif option == "4":
            print("Option 4 Selected")
        elif option == "5":
            conn.close()
            break

        else:
            print("Incorrect Option Selected")
        print("")


conn = mongo_connect(MONGODB_URI)

coll = conn[DBS_NAME][COLLECTION_NAME]

main_loop()
