"""
sandbox/04_possessions.py

Generates 1,000 fake basketball possessions using a generator,
then uses list comprehensions and functional tools to slice, filter, and analyze them.
"""

import random
import time
from functools import wraps

PLAYER_NAMES = ["Curry", "James", "Wembanyama", "Jordan", "Edwards"]
NUM_POSSESSIONS = 1000


def timer(func):
    """Decorator that prints how long a function took to run."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        elapsed = end - start
        print(f"{func.__name__} took {elapsed:.4f} seconds.")
        return result
    return wrapper


def generate_possessions(num_possessions: int):
    """
    Generator that yields a given number of possessions.

    A possession consists of:
    1) shooter — a name (pick from a small list of 5 player names)
    2) shot_distance — an integer in feet (random, somewhere between 0 and 30)
    3) made — a boolean (longer shots miss more often)
    4) points — 0 (if missed), 2 (if made and shot_distance < 23), or 3
       (if made and shot_distance >= 23)
    5) time_remaining — seconds left on the shot clock when the shot went up (0 to 24)
    """
    for _ in range(num_possessions):
        shooter = random.choice(PLAYER_NAMES)
        shot_distance = random.randint(0, 30)
        make_probability = max(0.2, 0.7 - 0.02 * shot_distance)
        made = random.random() < make_probability
        points = 0 if not made else (3 if shot_distance >= 23 else 2)
        time_remaining = random.randint(0, 24)

        yield {
            "shooter": shooter,
            "shot_distance": shot_distance,
            "made": made,
            "points": points,
            "time_remaining": time_remaining,
        }


# We time the LIST construction, not the generator itself.
# Decorating the generator function would only measure how long it takes
# to create the generator object (~microseconds), not how long it takes
# to produce all values. So we wrap the list() call.
@timer
def generate_possessions_list(n: int) -> list[dict]:
    """Materialize n possessions into a list and time the whole thing."""
    return list(generate_possessions(n))


def main():
    """Main script that executes everything."""
    # CHUNK 3 — generate the data
    random.seed(42)
    possessions = generate_possessions_list(NUM_POSSESSIONS)

    # CHUNK 4 — three list comprehensions
    # 1) Pure filter: long-range shots
    long_range = [p for p in possessions if p["shot_distance"] > 20]
    print(f"Long-range shots (distance > 20): {len(long_range)}")
    print(f"  First 3: {long_range[:3]}")

    # 2) Pure transform: just the points
    points = [p["points"] for p in possessions]
    print(f"Points list length: {len(points)}")
    print(f"  First 10: {points[:10]}")

    # 3) Filter + transform: distances of made shots only
    made_shot_distance = [p["shot_distance"] for p in possessions if p["made"]]
    print(f"Made shots: {len(made_shot_distance)}")
    print(f"  First 10 distances: {made_shot_distance[:10]}")

    # CHUNK 5 — generator expressions with sum
    total_points = sum(p["points"] for p in possessions)
    print(f"Total points: {total_points}")

    total_made_shots = sum(1 for p in possessions if p["made"])
    print(f"Total made shots: {total_made_shots}")

    total_missed_shots = sum(1 for p in possessions if not p["made"])
    print(f"Total missed shots: {total_missed_shots}")

    # CHUNK 6 — lambda with max()
    # BUG FIX: we need to iterate over made possessions (dicts), not over
    # the integer count of made shots. Filter inline with a generator expression.
    longest_shot = max(
        (p for p in possessions if p["made"]),
        key=lambda p: p["shot_distance"],
    )
    print(f"Longest made shot: {longest_shot}")

    # Minimal summary
    fg_pct = 100 * total_made_shots / NUM_POSSESSIONS
    print("-" * 40)
    print(f"FG%: {fg_pct:.1f}% | Total points: {total_points}")


if __name__ == "__main__":
    main()
