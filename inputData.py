from datetime import datetime

# name, subject, zipCode, dateStart, dateEnd
def inputPersonData():
    name = input("Enter your name: ")
    # age = input("Enter your age: ")
    zipCode = input("Enter your zipCode: ")
    # searchRadiusMile = input("Enter how far you are willing to drive in mile")
    subject = input("Enter the subject you need help with: ")
    dateStart = input("Enter the earliest date you are willing to attend a study group: ")
    dateEnd = input("Enter the lastest date you are willing to attend a study group: ")
    
    return name, subject, zipCode, dateStart, dateEnd

# groupName, subject, maxPersons, time, location
def inputGroupData():
    groupName = input("Enter the name of the group: ")
    subject = input("Enter the subject of the group: ")
    maxPersons = input("Enter the maximum number of people in the group: ")
    time = input("Enter the time of the group: ")
    location = input("Enter the location of the group: ")

    return groupName, subject, maxPersons, time, location

