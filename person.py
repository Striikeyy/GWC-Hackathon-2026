class Person:
    def __init__(self, name, subject, zipCode, dateStart, dateEnd):
        self.name = name
        self.subject = subject
        self.zip = zipCode
        self.dateStart = dateStart
        self.dateEnd = dateEnd

    # returns a list of groups that match the person's criteria, or None if there are no matches
    def getMatchAlgorithm(self, similarityThreshhold, temproups = []):
        matches = []
        # similarity goes from 0 to 1, with 1 being a perfect match, and 0 being no match at all
        similarity = 0
        for group in groups:
            if self.subject == group.subject and self.zip == group.location and self.dateStart <= group.time <= self.dateEnd:
                matches.append(group)
        if len(matches) > 0:
            return matches
        return None