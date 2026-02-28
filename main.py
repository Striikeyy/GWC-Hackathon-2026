from app import getFormData
from person import Person
from group import Group
from inputData import inputPersonData, inputGroupData

# name, subject, zipCode, dateStart, dateEnd
persons = []
groups = []

MATHCLASSES = ["algebra1", "algebra2", "geometry", "trigonometry", "precalculus", "apcalculusab", "apcalculusbc", "apstatistics"]

def main():
    personCount = int(input("How many people registered in the program? "))
    for i in range(personCount):
        persons.append(Person(*inputPersonData(MATHCLASSES)))
    
    groupCount = int(input("How many groups are registered in the program? "))
    for i in range(groupCount):
        groups.append(Group(*inputGroupData(MATHCLASSES)))
        for j in range(groups[i].maxPersons):   
            personName = input("Enter the name of the person you want to add to the group (type BLANK for blank): ")
            if personName != "BLANK":
                groups[i].addPerson(personName)
    
    if (input("Would you like to find a group? (Y/n): ").lower() == 'y'):
        persons.append(Person(*getFormData()))
        matches = persons[-1].findMatches(groups)
        if matches is not None:
            print("Here are the groups that match your criteria :) :")
            for match in matches:
                print(match.name)
        else:
            print("Sorry, there are no groups that match with you :(.")
    
    if (input("Would you like to make a group? (Y/n): ").lower() == 'y'):
            groups.append(Group(*inputGroupData(MATHCLASSES)))
            for j in range(groups[-1].maxPersons):   
                personName = input("Enter the name of the person you want to add to the group (type BLANK for blank): ")
                if personName != "BLANK":
                    groups[-1].addPerson(personName)

    print("los tralaleritos")

if __name__ == "__main__": 
    main()