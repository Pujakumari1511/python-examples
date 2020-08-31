#Create a program that allows a user to choose one of
#up to 9 time zones from a menu. You can choose any
#zones you want from all timezones list.

#The program will then display the time in that timezone, as
#well as local time and UTC time.

#Entering 0 as the choice will quit the program.

#Display the dates and times in format suitable for the user
#of your program to understand  and include the
#timezone name when displaying the choosen time

import pytz
from pytz import all_timezones
import datetime

countriesName = {1:"Europe/Amsterdam",
                 2:"Europe/Paris",
                 3:"Asia/Calcutta",
                 4:"Europe/Tallinn",
                 5:"Europe/Madrid",
                 6:"America/Chicago",
                 0: "Quit"}


def printUserInput():
    for i,j in countriesName.items():
        print(i,":", j)

while True:
    printUserInput()
    selectCountryName = int(input("select one country name as per the write above: "))
    if selectCountryName == 0:
        print("Quit")
        break
    else:
        if selectCountryName in countriesName.keys():
            tz_to_display = pytz.timezone(countriesName.get(selectCountryName))
            worldTime = datetime.datetime.now(tz=tz_to_display)
            print("The time in {} is {} ".format(countriesName[selectCountryName], worldTime.strftime('%A, %x %X,%z'),worldTime.tzname()))
            print("The local time is {}".format(datetime.datetime.now().strftime('%A %x %X')))
            print("UTC time is {}".format(datetime.datetime.utcnow().strftime('%A %x %X')))
