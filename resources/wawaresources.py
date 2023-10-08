from datetime import datetime
import json

# This module is for displaying weekly tasks


weekdays = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

def dailyroutine():
    # This imports a json dictionary containing the user's daily schedule.
    # Schedule files are not included with wawabot since they contain personal information.

    routinefile = open('resources/routine.json',)
    routines = json.load(routinefile)

    #The weekday function from the datetime module returns an integer 0-6, that gets used as the index of the weekdays tuple 
    dayofweek = weekdays[datetime.now().weekday()]
    routine = routines[dayofweek]

    return f"Today is {dayofweek}, so it's time for {routine}"



if __name__ == "__main__":
    print(dailyroutine())