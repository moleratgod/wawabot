from datetime import datetime

weekdays = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
routines = {"Monday"    : "LEG DAY BRO do ur squats or else [Glutes, Quads, and Calves]",
            "Tuesday"   : "Core day today, Work to your CORE! [Abs, Obliques, and Back]",
            "Wednesday" : "ARMS DAY LETS FUCKING GOOO [Biceps, Triceps, and Delts]",
            "Thursday"  : "Leg day AGAIN. [Glutes, Quads, and Calves]",
            "Friday"    : "Cardio..",
            "Saturday"  : "ARMS DAY AGAIN. HAVE FUN [Biceps, Triceps, and Delts]",
            "Sunday"    : "Cardio again :/"
}



def workoutroutine():
    #The weekday function from the datetime module returns an integer 0-6, that gets used as the index of the weekdays tuple 
    dayofweek = weekdays[datetime.now().weekday()]
    routine = routines[dayofweek]
    return f"Today is {dayofweek}, so it's time for {routine}"

if __name__ == "__main__":
    print(workoutroutine())