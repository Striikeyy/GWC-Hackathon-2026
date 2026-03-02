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
            groups[i].addPerson(input("Enter the name of the person you want to add to the group: "))
            
    
    if (input("Would you like to find a group? (Y/n): ").lower() == 'y'):

        # stores the index of the groups that match 
        # TODO
        for group in groups:
            print(group.name, group.subject, group.maxPersons, group.time, group.zipCode)
    
    if (input("Would you like to make a group? (Y/n): ").lower() == 'y'):
        for person in persons:
            print(person.name, person.subject, person.zipCode, person.dateStart, person.dateEnd)


    print("los tralaleritos")

if __name__ == "__main__": 
    main()