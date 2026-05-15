"""
sandbox/02_roster.py

Represents a 5-man starting lineup as a list of dicts.
Computes and prints team totals.

Second exercise in the HoopMind learning roadmap — practice with lists,
dictionaries, iteration, aggregation, and separation of concerns.
"""


# The roster lives at the module level as a constant.
# It's pure data — no need to wrap it in a function.
# Convention: ALL_CAPS for module-level constants.
ROSTER = [
    {"name": "John",    "position": "PG", "points": 32, "rebounds":  5, "assists": 2, "steals": 1},
    {"name": "Jane",    "position": "SG", "points": 15, "rebounds":  2, "assists": 3, "steals": 2},
    {"name": "Bob",     "position": "SF", "points": 10, "rebounds":  5, "assists": 2, "steals": 1},
    {"name": "Alice",   "position": "PF", "points":  8, "rebounds":  7, "assists": 1, "steals": 0},
    {"name": "Eve",     "position": "C",  "points": 12, "rebounds": 10, "assists": 1, "steals": 1},
]

# The stats we care about, in display order.
# Defining this once means we never repeat ourselves below.
STAT_NAMES = ["points", "rebounds", "assists", "steals"]

# Short labels for the box-score display.
STAT_LABELS = {"points": "PTS", "rebounds": "REB", "assists": "AST", "steals": "STL"}


def compute_team_total(roster: list[dict], stat_name: str) -> int:
    """Return the team's total for a single stat (e.g. 'points')."""
    # `sum()` with a generator expression: walks every player,
    # pulls their stat value, adds them all up. One clean line.
    return sum(player[stat_name] for player in roster)


def format_player(player: dict) -> str:
    """Format one player's stat line as a single string."""
    # Note the padding:
    #   {position:<3} = left-align in 3 chars (so 'C' and 'PG' both fit)
    #   {name:<8}     = left-align name in 8 chars (so columns line up)
    #   {points:>3}   = right-align number in 3 chars (so '8' and '32' line up)
    return (
        f"{player['position']:<3} {player['name']:<8} "
        f"{player['points']:>3} PTS | "
        f"{player['rebounds']:>3} REB | "
        f"{player['assists']:>3} AST | "
        f"{player['steals']:>3} STL"
    )


def format_team_totals(roster: list[dict]) -> str:
    """Format the team totals line."""
    # We loop over STAT_NAMES and call compute_team_total for each.
    # This is DRY: if we ever add 'blocks', we just add it to STAT_NAMES.
    parts = [
        f"{compute_team_total(roster, stat):>3} {STAT_LABELS[stat]}"
        for stat in STAT_NAMES
    ]
    # 'TEAM:' is padded to match the 'POS NAME' width above (3 + 1 + 8 + 1 = 13).
    return f"{'TEAM:':<13} " + " | ".join(parts)


def print_box_score(roster: list[dict]) -> None:
    """Print the full box score: header, each player, divider, team totals."""
    divider = "-" * 50
    print("Starting Lineup")
    print(divider)
    for player in roster:
        print(format_player(player))
    print(divider)
    print(format_team_totals(roster))


def main() -> None:
    print_box_score(ROSTER)


if __name__ == "__main__":
    main()