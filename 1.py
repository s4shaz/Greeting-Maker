#Program to take input from the user and greet him according to his local time

#from suntime import Sun (Maybe if I ever want to implement it with a sunset indicator)
from datetime import datetime
name=input("Hi, what is your name?: ")
name=name.capitalize()
time= datetime.now().strftime("%H")
time=int(time)
fix_time = datetime.now().strftime("%H, %M")
if (time<12):
    print("Good Morning " + name)
elif (17>time>=12):
    print("Good Afternoon " + name)
elif (time>=18):
    print("Good Evening " + name)