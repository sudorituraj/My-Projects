import random

def roll():
    min_value = 1
    max_value = 6
    return random.randint(min_value, max_value)

# Validate number of players
while True:
    players = input("Enter the number of players (2-4): ").strip()
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Please enter a valid number of players (2-4).")

print("Great! There are", players, "players in the game.")

max_score = 30
players_score = [0 for _ in range(players)]

# Main game loop
while max(players_score) < max_score:
    for player_idx in range(players):
        print("\nPlayer", player_idx + 1, "'s turn has started.")
        print("Your current total score is:", players_score[player_idx], "\n")

        current_score = 0
        while True:
            should_roll = input("Would you like to roll? (y) ").lower()
            if should_roll != 'y':
                break

            value = roll()
            print("You rolled a:", value)

            if value == 1:
                print("You rolled a 1! Turn done!")
                current_score = 0
                break
            else:
                current_score += value
                print("Current score this turn:", current_score)

        players_score[player_idx] += current_score
        print("Player", player_idx + 1, "total score is:", players_score[player_idx])

# Determine the winner
max_score = max(players_score)  # Highest score in the game
winning_idx = players_score.index(max_score)  # Find the player with that score
print("\nPlayer", winning_idx + 1, "is the winner with a score of:", max_score)
