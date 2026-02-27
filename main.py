from person import Person
from group import Group
from inputData import inputPersonData, inputGroupData

# name, subject, zipCode, dateStart, dateEnd
persons = []
groups = []

def main():
    for i in range(3):
        persons.append(Person(inputPersonData()))
    for i in range(3):
        groups.append(Group(inputGroupData()))
        for j in range(groups[i].maxPersons):   
            groups[i].addPersons(input("Enter the name of the person you want to add to the group: "))
    
    if (input("Would you like to find a group? (Y/n): ") == 'Y'):

        # stores the index of the groups that match 
        # TODO
        for group in groups:
            print(group.name, group.subject, group.maxPersons, group.time, group.location)


    print("los tralaleritos")

if __name__ == "__main__": 
    main()