"""
sandbox/03_player_class.py

Contains the Player class representing a single player.
"""

class Player:
    """
    Contains all needed information on a single player.
    """
    def __init__(self, name, position, points, rebounds, assists, steals):
        self.name = name
        self.position = position
        self.points = points
        self.rebounds = rebounds
        self.assists = assists
        self.steals = steals

    def __repr__(self):
        return f"Player(name={self.name!r}, position={self.position!r}, points={self.points!r}, rebounds={self.rebounds!r}, assists={self.assists!r}, steals={self.steals!r})"

    def total_contribution(self):
        """
        Computes the player's total points, rebounds, assists and steals.
        """
        total = self.points + self.rebounds + self.assists + self.steals
        return total

    def stat_line(self):
        """
        Returns a formatted stat line about the player.
        """
        return f"{self.position} {self.name}  {self.points} PTS | {self.rebounds} REB | {self.assists} AST | {self.steals} STL"

class PointGuard(Player):
    """
    Pointguard class that inherits from the Player class.
    """
    def is_pass_first(self):
        """
        Determines if the pointguard is a pass first player.
        """
        return self.assists > self.points

class Center(Player):
    """
    Center class that inherits from the Player class.
    """
    def __init__(self, name, points, rebounds, assists, steals, wingspan_inches):
        super().__init__(name, position="C", points=points, rebounds=rebounds, assists=assists, steals=steals)
        self.wingspan_inches = wingspan_inches

    def is_double_double(self):
        """
        Calculates if the Center achieved a double double.
        """
        return self.points >= 10 and self.rebounds >= 10

def main():
    """
    Main script that executes everything.
    """
    john = PointGuard(name="John", position="PG", points=10, rebounds=3, assists=12, steals=2)
    print(john)                    # Uses inherited __repr__ — should still work
    print(john.total_contribution())  # Uses inherited method — should still work
    print(john.is_pass_first())    # Uses NEW method — should print True
    shaq = Center(name="Shaq", points=12, rebounds=11, assists=0, steals=0, wingspan_inches=90)
    print(shaq)
    print(shaq.is_double_double())
    print(shaq.total_contribution())

if __name__ == "__main__":
    main()
