AGEND = {}


def get_contact():
    for contact in AGEND:
        print("Name:", contact)
        print("Telephone:", AGEND[contact]["telephone"])
        print("Email:", AGEND[contact]["email"])
        print("Adress:", AGEND[contact]["address"])
        print('-----------------')


def search_contact():
    search = input("Search contact: ")
    if search in AGEND:
        print("Name:", search)
        print("Telephone:", AGEND[search]["telephone"])
        print("Email:", AGEND[search]["email"])
        print("Adress:", AGEND[search]["address"])
        print('-----------------')
    else:
        print("Contact not found")


def add_contact():
    name = input("Name: ")
    telephone = input("Telephone: ")
    email = input("Email: ")
    address = input("Address: ")
    AGEND[name] = {
        "telephone": telephone,
        "email": email,
        "address": address,
    }


def remove_contact():
    name = input("Name: ")
    if name in AGEND:
        del AGEND[name]
    else:
        print("Contact not found")


def edit_contact():
    name = input("Name: ")
    if name in AGEND:
        print("1 - Edit telephone")
        print("2 - Edit email")
        print("3 - Edit address")
        option = input("Choose an option: ")
        if option == "1":
            telephone = input("Telephone: ")
            AGEND[name]["telephone"] = telephone
        elif option == "2":
            email = input("Email: ")
            AGEND[name]["email"] = email
        elif option == "3":
            address = input("Address: ")
            AGEND[name]["address"] = address
        else:
            print("Invalid option")
    else:
        print("Contact not found")


while True:
    print("1 - Add contact")
    print("2 - Remove contact")
    print("3 - Search contact")
    print("4 - Get all contacts")
    print("5 - Edit contact")
    print("6 - Exit")
    option = input("Choose an option: ")
    if option == "1":
        add_contact()
    elif option == "2":
        remove_contact()
    elif option == "3":
        search_contact()
    elif option == "4":
        get_contact()
    elif option == "5":
      edit_contact()
    elif option == "6":
        break
    else:
        print("Invalid option")
