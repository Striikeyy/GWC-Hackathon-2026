from datetime import datetime

class Person:
    def __init__(self, name, subject, zipCode, dateStart, dateEnd):
        self.name = name
        self.subject = subject
        self.zipCode = zipCode
        self.dateStart = datetime.strptime(dateStart, "%Y-%m-%d")
        self.dateEnd = datetime.strptime(dateEnd, "%Y-%m-%d")
    
    def findMatches(self, groups):
        matches = []
        print(f"Finding matches for {self.name} with Subject: {self.subject}, ZIP: {self.zipCode}, Dates: {self.dateStart} - {self.dateEnd}")
        for group in groups:
            print(f"Checking group: {group.name} with Subject: {group.subject}, ZIP: {group.zipCode}, Dates: {group.dateStart} - {group.dateEnd}")

            group_start = datetime.strptime(group.dateStart, "%Y-%m-%d")
            group_end = datetime.strptime(group.dateEnd, "%Y-%m-%d")

            if self.subject == group.subject and self.zipCode == group.zipCode:
                if self.dateStart <= group_end and self.dateEnd >= group_start:
                    print(f"Match found: {group.name}")
                    matches.append(group)
                else:
                    print(f"Dates do not overlap for {group.name}")
            else:
                print(f"No match for {group.name}: Subject or ZIP doesn't match.")
        
        return matches