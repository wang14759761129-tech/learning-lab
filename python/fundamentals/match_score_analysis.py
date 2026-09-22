"""A first table tennis score analysis.

This uses only basic Python so each step can be explained and checked.
The match data below is a small practice example.
"""


def summarize_match(game_scores):
    """Return simple totals for a list of (my_score, opponent_score) games."""
    games_won = 0
    games_lost = 0
    total_points_won = 0
    total_points_lost = 0

    for my_score, opponent_score in game_scores:
        total_points_won = total_points_won + my_score
        total_points_lost = total_points_lost + opponent_score

        if my_score > opponent_score:
            games_won = games_won + 1
        else:
            games_lost = games_lost + 1

    point_difference = total_points_won - total_points_lost

    return {
        "games_won": games_won,
        "games_lost": games_lost,
        "total_points_won": total_points_won,
        "total_points_lost": total_points_lost,
        "point_difference": point_difference,
    }


# A list stores several game scores in one value.
match_scores = [(11, 8), (7, 11), (11, 9), (9, 11), (11, 6)]
summary = summarize_match(match_scores)

print("Table tennis match summary")
print("Games won:", summary["games_won"])
print("Games lost:", summary["games_lost"])
print("Total points won:", summary["total_points_won"])
print("Total points lost:", summary["total_points_lost"])
print("Point difference:", summary["point_difference"])

# Variables hold values such as scores and totals.
# The loop processes each game instead of repeating the same calculation.
# The condition decides whether a game was won or lost.
# The function groups the calculation so it can be run on another score list.
