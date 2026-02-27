class Person:
    def __init__(self, name, subject, zipCode, dateStart, dateEnd):
        self.name = name
        self.subject = subject
        self.zip = zipCode
        self.dateStart = dateStart
        self.dateEnd = dateEnd

    def findMatches(self, groups):
        matches = []
        for group in groups:
            if (self.subject == group.subject and self.zip == group.zip and self.dateStart <= group.date <= self.dateEnd and group.maxPersons > len(group.getPersons())):
                matches.append(group)
            if matches == []:
                return None
            return matches