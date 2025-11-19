from team import Team

#globale variabelen
ranking = []
#hoeveel punten je krijgt als er gelijkspel is (1) en hoeveel punten je krijgt als je wint (3)
points_draw = 1
points_win = 3

class Team:
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.wins = 0
        self.draws = 0
        self.losses = 0
        self.matches = 0

    def add_team(self, team):
        ranking.append(team)

    def find_team(self, team_name):
        if team_name in ranking:
            return team_name
        else:
            return None

    def add_draw(self, first_team_name, second_team_name):
        first_team = find_team(first_team_name)
        second_team = find_team(second_team_name)
        first_team.draws += 1
        second_team.draws += 1
        first_team.matches += 1
        second_team.matches += 1

    def add_victory(self, team_name):
        team = find_team(team_name)
        team.wins += 1
        team.matches += 1