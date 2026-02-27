class Group:
    def __init__(self, groupName, time, location):
        self.name = name
        self.groupName = groupName
        self.time = time
        self.location = location
        self.users = []

    def add_user(self, user):
        if user not in self.users:
            self.users.append(user)

    def remove_user(self, user):
        if user in self.users:
            self.users.remove(user)
        else: 
            print(f"{user} is not in the group.\n")

    def get_users(self):
        return self.users