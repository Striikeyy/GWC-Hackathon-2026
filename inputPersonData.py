from datetime import datetime

# name, age, math, zipCode, searchRadiusMile, dateStart, dateEnd
def inputPersonData():
    name = input("Enter your name: ")
    # age = input("Enter your age: ")
    zipCode = input("Enter your zipCode")
    # searchRadiusMile = input("Enter how far you are willing to drive in mile")
    subject = input("Enter the subject you need help with: ")
    dateStart = input("Enter the earliest date you are willing to attend a study group: ")
    dateEnd = input("Enter the lastest date you are willing to attend a study group: ")
    
    return name, zipCode, subject, dateStart, dateEnd
