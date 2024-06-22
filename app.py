import memory_game
import guess_game
import currency_roulette_game
from score import add_score
from utils import screen_cleaner


def welcome(name):
    print(f"Hi {name} and welcome to the World of Games: The Epic Journey")


def start_play():
    while True:
        print("\nPlease choose a game to play:")
        print("1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back.")
        print("2. Guess Game - guess a number and see if you chose like the computer.")
        print("3. Currency Roulette - try and guess the value of a random amount of USD in ILS")

        try:
            game_choice = int(input("Enter the number of the game you want to play: "))
            if game_choice not in [1, 2, 3]:
                raise ValueError("Invalid choice")
        except ValueError:
            print("Please enter a valid number between 1 and 3.")
            continue

        try:
            difficulty = int(input("Choose difficulty level between 1 and 5: "))
            if difficulty not in [1, 2, 3, 4, 5]:
                raise ValueError("Invalid difficulty level")
        except ValueError:
            print("Please enter a valid number between 1 and 5.")
            continue

        screen_cleaner()

        if game_choice == 1:
            if memory_game.play(difficulty):
                add_score(difficulty)
        elif game_choice == 2:
            if guess_game.play(difficulty):
                add_score(difficulty)
        elif game_choice == 3:
            if currency_roulette_game.play(difficulty):
                add_score(difficulty)

        again = input("Do you want to play another game? (yes/no): ").lower()
        if again != 'yes':
            break


