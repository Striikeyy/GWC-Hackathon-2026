import datetime

# self, name, subject, zipCode, dateStart, dateEnd
def inputPersonData(tempMATHCLASSES):
    while True:
        name = input("Enter name of person(proper capitalization): ")
        if name.isalpha():
            break
        else:
            print("Invalid name. Enter a name with only letters .")

    while True:
        zipCode = input("Enter your zip code: ")
        if zipCode.isdigit() and len(zipCode) == 5:
            break
        else:
            print("Invalid zip code. Enter a 5-digit number.")

    while True:
        for i in tempMATHCLASSES:
            print(i)
        subject = input("Enter the math class you need help with: ")
        if subject.replace(" ", "").isalnum() and subject in tempMATHCLASSES:
            break
        else:
            print("Invalid subject. Enter a valid math class from the list above.")

    dateStart = getValidDate("Enter the earliest date willing to attend a study session (YYYY-MM-DD): ")

    while dateStart < datetime.datetime.now():
        print("Start date cannot be in the past.")
        dateStart = getValidDate("Enter earliest date (YYYY-MM-DD): ")
    dateEnd = getValidDate("Enter latest date willing to attend a study session (YYYY-MM-DD): ")

    while dateEnd < dateStart:
        print("End date cannot be before start date.")
        dateEnd = getValidDate("Enter latest date (YYYY-MM-DD): ")

    return name, subject, zipCode, dateStart, dateEnd

# self, groupName, subject, maxPersons, time, location
def inputGroupData(tempMATHCLASSES):
    while True:
        groupName = input("Enter group name: ")
        if groupName.isalpha():
            break
        else:
            print("Invalid name. Enter a name with only letters .")

    while True:
        for i in tempMATHCLASSES:
            print(i)
        subject = input("Enter the math class being discussed: ")
        if subject.replace(" ", "").isalnum() and subject.lower() in tempMATHCLASSES:
            break
        else:
            print("Invalid subject. Enter a valid math class from the list above.")

    while True:
        maxPersons = input("Enter the maximum number of people in the group: ")
        if maxPersons.isdigit() and int(maxPersons) > 0:
            maxPersons = int(maxPersons)
            break
        else:
            print("Maximum number of people must be a positive integer.")

    date = getValidDate("Enter the date of the session (YYYY-MM-DD): ")
    zip = input("Enter the zip code of the group: ")

    return groupName, subject, maxPersons, date, zip

def getValidDate(prompt):
    while True:
        dateInput = input(prompt)
        try:
            dateObject = datetime.datetime.strptime(dateInput, "%Y-%m-%d")
            return dateObject
        except ValueError:
            print("Use YYYY-MM-DD format.")