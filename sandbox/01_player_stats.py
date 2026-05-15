"""
sandbox/01_player_stats.py

Stores a single player's stat line and prints it in a readable format.
First exercise in the HoopMind learning roadmap — practice with variables,
types, f-strings, and the basic function pattern.
"""


def format_stat_line(name: str, points: int, rebounds: int, assists: int, steals: int) -> str:
    """Return a one-line summary of a player's box-score stats."""
    return f"{name} — {points} PTS | {rebounds} REB | {assists} AST | {steals} STL"


def main() -> None:
    # Sample stat line (LeBron's average-ish game)
    name = "John"
    points = 20
    rebounds = 3
    assists = 4
    steals = 1

    print(format_stat_line(name, points, rebounds, assists, steals))


if __name__ == "__main__":
    main()