import random

class PigGame:
    def __init__(self, num_players=4, winning_score=40):
        self.num_players = num_players
        self.winning_score = winning_score
        self.scores = [0] * num_players
        self.current_player = 0

    def roll_die(self):
        return random.randint(1, 6)

    def player_turn(self):
        turn_score = 0
        print(f"\nPlayer {self.current_player + 1}'s turn")
        while True:
            roll = self.roll_die()
            print(f"Player {self.current_player + 1} rolled: {roll}")
            if roll == 1:
                print("Rolled a 1! No points added this turn.")
                return 0
            else:
                turn_score += roll
                print(f"Current turn score: {turn_score}")
                choice = input("Roll again? (y/n): ").strip().lower()
                if choice != 'y':
                    return turn_score

    def play_game(self):
        print("Starting the Pig Game!\n")
        while max(self.scores) < self.winning_score:
            turn_score = self.player_turn()
            self.scores[self.current_player] += turn_score
            print(f"Player {self.current_player + 1}'s total score: {self.scores[self.current_player]}")
            if self.scores[self.current_player] >= self.winning_score:
                print(f"\nPlayer {self.current_player + 1} wins with {self.scores[self.current_player]} points!")
                break
            self.current_player = (self.current_player + 1) % self.num_players

# To play the game
if __name__ == "__main__":
    game = PigGame()
    game.play_game()
