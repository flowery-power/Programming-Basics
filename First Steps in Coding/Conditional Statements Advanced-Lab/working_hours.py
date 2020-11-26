hours = int(input())
day_week = input()



if 10 <= hours <=18 and day_week == "Monday":
    print("open")
elif 10 <= hours <= 18 and day_week == "Tuesday":
    print("open")
elif 10 <= hours <= 18 and day_week == "Wednesday":
    print("open")
elif 10 <= hours <= 18 and day_week == "Thursday":
    print("open")
elif 10 <= hours <= 18 and "Friday" == day_week:
    print("closed")
elif 10 <= hours <= 18 and day_week == "Saturday":
    print("open")
else:
    print("closed")