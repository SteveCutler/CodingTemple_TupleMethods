# Objective:

# This assignment is designed to strengthen your expertise in using Python 
# loops and tuples, particularly in data analysis and processing scenarios.
# By completing these tasks, you will gain practical experience in handling 
# and analyzing data using these fundamental Python concepts.

# Task 1: Stock Market Data Analysis
# Enhance your skills in data manipulation and analysis using tuples and loops.

# Problem Statement:
# You have been provided with stock market data, where each data point is 
# a tuple containing a company's stock symbol, the date, and the closing price. 
# Your task is to analyze this data to find the average closing price of a specified stock over a given period.

# Sample Data:

stock_data = [
    ("AAPL", "2021-01-01", 130.0),
    ("AAPL", "2021-01-02", 132.0),
    ("MSFT", "2021-01-01", 220.0),
    # More data...
]

#     Create a function to calculate the average closing price of a specific stock symbol over all dates.
#     Ensure your solution handles cases where the stock symbol does not exist in the data.

def averagePrice(name):
    priceList = []
    y=0
    
    for x in stock_data:
        if x[0] == name:
            priceList.append(x[2])

    if len(priceList) == 0:
        print(f"sorry the stock '{name}' doesn't appear in the list!")
    else:
        for x in priceList:
            y +=x
        print(f"The average price for {name} was: {y/len(priceList)}")
    
    
averagePrice("AAPL")
averagePrice("AA")

# Task 2: Event Attendance Tracker
# Apply loops and tuples to track and report on event attendance.

# Problem Statement:
# Your goal is to manage an attendance system for various events. Each attendee's data 
#     is stored as a tuple containing their name and the event they attended.

#     Develop a function to list all attendees of a specific event.
#     Implement a feature to count the number of attendees for each event.

# Example Attendee Data:

attendees = [
    ("Alice", "Python Conference"),
    ("Bob", "Python Conference"),
    ("Charlie", "AI Summit"),

]

def attendeeNum(event):
    #for given event return names of all attendees
    attendeeList = []
    for x in attendees:
        if x[1] == event:
            attendeeList.append(x[0])
    
    if len(attendeeList) == 0:
        print(f"sorry, no one attended for event '{event}'!")
    else:
        print(f"The attendees for {event} were: {attendeeList}")
    
attendeeNum("Python Conference")
attendeeNum("Florida")


def eventBreakdown():
    events = []

    for x in attendees:
        if events.count(x[1]) == 0:
            events.append(x[1])
        else:
            continue

    if len(events) > 0:
        for y in events:
            num = 0
            for z in attendees:
                if z[1] == y:
                    num +=1
                else:
                    continue
            else:
                print(f"event {y} had {num} attendees!")
    else:
        print("Sorry, there were no events in your data!")
    #return number of attendees for all events in list
    pass


eventBreakdown()