from enum import Enum

class SoccerPlayer:
   # The position a player can play on the pitch.
   position = Enum("position", ["GK", #Goalkeeper
                               "DF", #Defender
                               "MF", #Midfield
                               "FW"  #Forward
                               ])

   def __init__(self, first_name, last_name, age, position):
       self.age = age
       self.first_name = first_name
       self.last_name = last_name
       self.position = position

   def __lt__(self, other):
       return self.get_name().casefold() == other.get_name().casefold()

   def __eq__(self, other):
       if self is other:
           return True
       if not isinstance(other, SoccerPlayer):
           return False
       return (
           self.age == other.age and
           self.first_name == other.first_name and
           self.last_name == other.last_name and
           self.position == other.position
       )

   def get_age(self):
       return self.age

   def get_name(self):
       return f'{self.first_name} {self.last_name}'

   def get_position(self):
       return self.position

   def __hash__(self):
       return hash((self.age, self.first_name, self.last_name, self.position))

   def __str__(self):
       return self.get_name()

class SoccerTeam:
   SIZE = 11
   def __init__(self, name: str):
       self.name = name
       self.players = []

   def add_player(self, player: SoccerPlayer) -> bool:
       if len(self.players) < 11 and player not in self.players:
           #minder dan 11 in het team, degene die wordt toegevoegd zit er ngo nie in
           self.players.append(player)
           return True
       return False

   def get_average_age(self) -> float:
       if not self.players: #als er nog geen spelers zijn toegevoegd
           return 0.0
       return sum(player.get_age() for player in self.players) / len(self.players)

   def get_formation(self) -> str:
       gk_count = 0
       df_count = 0
       mf_count = 0
       fw_count = 0
       for player in self.players:
           position = player.get_position()
           if position == SoccerPlayer.position.GK:
               gk_count += 1
           elif position == SoccerPlayer.position.DF:
               df_count += 1
           elif position == SoccerPlayer.position.MF:
               mf_count += 1
           elif position == SoccerPlayer.position.FW:
               fw_count += 1
       return f"{df_count}-{mf_count}-{fw_count}"
       return f"{df_count}-{mf_count}-{fw_count}"


   def get_name(self) -> str:
       return self.name

   def get_players(self) -> list:
       if len(self.players) == 0:
           return [None] * 11
       return self.players

   def get_players_at(self, position: SoccerPlayer.position) -> list:
       return [player for player in self.players if player.get_position() == position]

   def substitute(self, player_out: SoccerPlayer, player_in: SoccerPlayer) -> bool:
       if player_out in self.players and player_in not in self.players:
           if player_out.get_position() == SoccerPlayer.position.GK and player_in.get_position() == SoccerPlayer.position.GK:
               self.players.append(player_in)
               self.players.remove(player_out)
               return True
           if player_out.get_position() != SoccerPlayer.position.GK and player_in.get_position() != SoccerPlayer.position.GK:
               self.players.append(player_in)
               self.players.remove(player_out)
               return True
           return False
       return False