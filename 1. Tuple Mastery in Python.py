# Objective:
# The aim of this assignment is to deepen your understanding of tuples 
# in Python, along with their interaction with lists, dictionaries, 
# and basic Python functionalities like functions, input handling, 
# and string formatting. By completing this assignment, you will enhance 
# your skills in data structuring, manipulation, and application of tuples 
# in practical scenarios.

# Task 1: Formatting Flight Itineraries
# Create a Python function that takes a list of tuples as an argument. 
# Each tuple contains information about a flight itinerary: (traveler_name, origin, destination). 
# The function should format and return a string that lists each itinerary. For example, 
# if the input is [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")], 
# the output should be a string formatted as:

# "Itinerary 1: Alice - From New York to London
#  Itinerary 2: Bob - From Tokyo to San Francisco"

#######

#create function that accepts tuples
def flightItin(details):
    x = 0

    while x < len(details):
        flightplanDetails = (list(details[x]))
        print(f"Itinerary {x+1}: {flightplanDetails[0]} - From {flightplanDetails[1]} to {flightplanDetails[2]}")

        x += 1
        # for info in flightplanDetails:
        #      print(f"info = {flightplanDetails[info]}")
        #      #print(f"Itinerary 0: {info[0]} - From {info[1]} to {info[2]}")


flightDetails =[("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")]

flightItin(flightDetails)

