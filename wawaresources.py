from datetime import datetime

# nobody is allowed to comment on my workout routine
weekdays = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
routines = {"Monday"    : "LEG DAY [Glutes, Quads, and Calves]",
            "Tuesday"   : "CORE DAY [Abs, Obliques, and Back]",
            "Wednesday" : "ARMS DAY [Biceps, Triceps, and Delts]",
            "Thursday"  : "Leg day AGAIN [Glutes, Quads, and Calves]",
            "Friday"    : "Cardio..",
            "Saturday"  : "ARMS DAY AGAIN [Biceps, Triceps, and Delts]",
            "Sunday"    : "Cardio again..."
            }



def workoutroutine():
    #The weekday function from the datetime module returns an integer 0-6, that gets used as the index of the weekdays tuple 
    dayofweek = weekdays[datetime.now().weekday()]
    routine = routines[dayofweek]
    return f"Today is {dayofweek}, so it's time for {routine}"

if __name__ == "__main__":
    print(workoutroutine())