# Objective:
# The goal of this assignment is to deepen your understanding of tuple packing 
# and unpacking in Python. You will apply these techniques in various practical 
# scenarios, enhancing your ability to work with flexible data structures and 
# improve data handling efficiency.

# Task 1: Customer Order Processing
# Refine your skills in tuple unpacking by managing customer orders.

# Problem Statement:
# You are given a list of tuples, each representing a customer's order. 
# Each tuple contains the customer's name, the product ordered, and the 
# quantity. Your task is to unpack each tuple and print the order details in a user-friendly format.

# Sample Order Data:

orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2),
    # More orders...
]

#     Write a function to iterate over the list of orders.
#     Unpack each tuple in the list and format the details for display.

def unpackOrder(orders):
    for tuple in orders:
        x,y,z = tuple
        print(f"{x} ordered {z} {y}")

unpackOrder(orders)

# Task 2: Sorting and Filtering Contact Information
# Implement tuple packing and unpacking in sorting and filtering tasks.

# Problem Statement:
# You have a list of contacts, where each contact is represented as a tuple 
# containing a name, email, and phone number. Your task is to:

#     Sort the contacts by name.
#     Filter and display contacts whose names start with a specific letter.

# Sample Contact Data:

contacts = [
    ("Alice", "alice@email.com", "123-456-7890"),
    ("Bob", "bob@email.com", "234-567-8901"),
    ("Aaron", "aaron@email.com", "654-664-3232")
]

#sort tuples by specific index value
def sortContacts(list):
    list.sort()
    print(f"sorted contact list = {list}")
    
print(f"original contact list = {contacts}\n")
sortContacts(contacts)


#filter and display contacts whose names start with a specific letter
def filterContacts(letter):
    filteredList = []
    for x in contacts:
        if x[0][0].lower() == letter.lower():
            filteredList.append(x[0])
    if len(filteredList) > 0:
        print(f"Names in your contact list beginning with {letter} were: {filteredList}")
    else:
        print(f"Sorry! No names starting with {letter} were found :(")

    pass


filterContacts("a")