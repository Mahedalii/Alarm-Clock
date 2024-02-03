import datetime
from playsound import playsound

alarmHour = int(input("Enter Hour: "))
alarmMin = int(input("Enter Minutes: "))
alarmAM = input("AM/PM: ")

print("Waiting for alarm",alarmHour, alarmMin, alarmAM)
if alarmAM == "PM":
    alarmHour += 12
    
while True:
    if alarmHour == datetime.datetime.now().hour and alarmMin == datetime.datetime.now().minute:
        print("Time to wake up")
        playsound("Danger.mp3")
        break 