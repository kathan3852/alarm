import time,pyttsx3
from datetime import datetime
print("Hello, welcome to my alarming interface...")
print("It is based on 24 hours clock format...")
Name = input("Enter your name: ")
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Current Time is: ", current_time)
Time=input("Enter the time (HH24:MM): ")
while True:
    Standard_time=datetime.now().strftime("%H:%M")
    time.sleep(1)
    if Time==Standard_time:
        count=0
        while count<=10:
            count=count+1
            engine=pyttsx3.init()
            engine.say("Wake up"+Name)
            engine.runAndWait()
        print("Thankyou For using the Interface")
        break
