# EE, conditionals notes

military_time= 900

if military_time < 600:
    print("It is the afternoon")
elif military_time < 900:
    print("Good Morning!") 
elif military_time < 1200:
    print("Good Mornig! You should be at school!")
elif military_time < 1700:
    print("Good Afternoon")
else:
    print("Good Evening")

# nesting conditionals
day="saturday" 
time=900

if time > 900 and time < 1600:
    if day != "saturday" or day != "sunday":
        print("You shpould be at school")
    else:
        if time > 1200:
            print("good Afternoon")
        else:
            print("Good Morning")
else:
    print("You are not required to be at school")