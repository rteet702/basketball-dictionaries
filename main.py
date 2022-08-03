players = [
    {
        "name": "Kevin Durant", 
        "age":34, 
        "position": "small forward", 
        "team": "Brooklyn Nets"
    },
    {
        "name": "Jason Tatum", 
        "age":24, 
        "position": "small forward", 
        "team": "Boston Celtics"
    },
    {
        "name": "Kyrie Irving", 
        "age":32, 
        "position": "Point Guard", 
        "team": "Brooklyn Nets"
    },
    {
        "name": "Damian Lillard", 
        "age":33, 
        "position": "Point Guard", 
        "team": "Portland Trailblazers"
    },
    {
        "name": "Joel Embiid", 
        "age":32, 
        "position": "Power Foward", 
        "team": "Philidelphia 76ers"
    },
    {
        "name": "", 
        "age":16, 
        "position": "P", 
        "team": "en"
    }
]

kevin = {
        "name": "Kevin Durant", 
        "age":34, 
        "position": "small forward", 
        "team": "Brooklyn Nets"
}
jason = {
        "name": "Jason Tatum", 
        "age":24, 
        "position": "small forward", 
        "team": "Boston Celtics"
}
kyrie = {
        "name": "Kyrie Irving", 
        "age":32, "position": "Point Guard", 
        "team": "Brooklyn Nets"
}


class Player:
    def __init__(self, dict):
        self.name = dict["name"]
        self.age = dict["age"]
        self.position = dict["position"]
        self.team = dict["team"]

    @classmethod
    def get_team(cls, team_list):
        returnList = []
        for player in team_list:
            returnList.append(Player(player))
        
        return returnList


# Create your Player instances here!
new_team = []

player_jason = Player(jason)
player_kevin = Player(kevin)
player_kyrie = Player(kyrie)

for player in players:
    new_team.append(Player(player))

second_team = Player.get_team(players)

print(second_team)