class Team:
    def __init__(self, name, points = 0):
        self.members = []
        self.name = name
        self.points = points

    def get_members(self):
        return self.members

    def get_name(self):
        return self.name

    def get_points(self):
        return self.points

    def add_points(self, amount):
        self.points += amount

    def set_name(self, newName):
        self.name = newName

    def add_member(self, name):
        #als de naam nog niet in de lijst zit!!!
        if name not in self.members:
            self.members.append(name)

    def contains_member(self, name):
        return name in self.members #zal TRUE / FALSE als output hebben

    def remove_member(self, name):
        if name in self.members:
            self.members.remove(name)

team1 = Team("YAY")
team1.add_member("Norah")
print(team1.get_members())
team1.add_member("papa")
print(team1.get_members())
team1.add_member("mama")
print(team1.get_members())
print(team1.contains_member("Norah"))
team1.remove_member("Norah")
print(team1.get_members())
team1.add_points(4)
print(team1.get_points())