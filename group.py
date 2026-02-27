class Group:
    def __init__(self, groupName, subject, maxPersons, date, zipCode):
        self.name = groupName
        self.subject = subject
        self.maxPersons = maxPersons
        self.date = date
        self.location = zipCode
        self.personsInGroup = []

    def addPerson(self, person):
        if person not in self.personsInGroup:
            self.personsInGroup.append(person)
        else:
            print(f"{person} is already in the group!")

    def removePerson(self, person):
        if person in self.personsInGroup:
            self.personsInGroup.remove(person)
        else: 
            print(f"{person} is not in the group.")

    def getPersons(self):
        return self.personsInGroup