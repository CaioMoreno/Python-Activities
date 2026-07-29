class Game:
    def __init__(self):
        self.wins = 0
        self.losses = 0

    def won_level(self):
        self.wins += 1

    def lost_level(self):
        self.losses +=1

    @property
    def score(self):
        return self.wins - self.losses

g = Game()
print(g.wins)
g.won_level()
g.won_level()
print(g.wins)
print(g.score)
g.lost_level()
print(g.score)
