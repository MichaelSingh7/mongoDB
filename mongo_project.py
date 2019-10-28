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


def get_record():
    print("")
    first = input("Enter First Name? ")
    last = input("Enter Last Name? ")

    try:
        doc = coll.find_one({'first': first.lower(), 'last': last.lower()})
    except:
        print("Access Denied Due To Processing Error")
    if not doc:
        print("")
        print("Access Denied, No Results Found")

    return doc


def add_record():
    print("")
    first = input("What Is Your First Name? ")
    last = input("What Is Your Last Name? ")
    dob = input("Enter Your DOB --/--/----? ")
    gender = input("Please Enter Your Gender? ")
    hair_colour = input("Enter Your Natural Hair Colour? ")
    occupation = input("What Is Your Current Occupation? ")
    nationality = input("What Is Your Nationality? ")
    food = input("What Is Your Favourite Food? ")
    drink = input("What Is Your Favourite Drink? ")

    new_doc = {'first': first.lower(), 'last': last.lower(),
               'dob': dob, 'gender': gender,
               'hair_colour': hair_colour, 'occupation': occupation,
               'nationality': nationality, 'food': food, 'drink': drink}

    try:
        coll.insert_one(new_doc)
        print("")
        print("Document Has Been Processed Into Database")
    except:
        print("Access Denied Due To Processing Error")


def find_record():
    doc = get_record()
    if doc:
        print("")
        for k, v in doc.items():
            if k != "_id":
                print(k.capitalize() + ": " + v.capitalize())


def main_loop():
    while True:
        option = show_menu()
        if option == "1":
            add_record()
        elif option == "2":
            find_record()
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
