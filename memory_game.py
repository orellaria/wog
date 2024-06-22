import random
import time
from utils import screen_cleaner

def generate_sequence(difficulty):
    return [random.randint(1, 101) for _ in range(difficulty)]

def get_list_from_user(difficulty):
    print(f"Please enter the {difficulty} numbers you saw, separated by space:")
    user_input = input().split()
    return [int(num) for num in user_input]

def is_list_equal(list1, list2):
    return list1 == list2

def play(difficulty):
    sequence = generate_sequence(difficulty)
    print("Remember this sequence of numbers:")
    print(sequence)
    time.sleep(0.7)
    screen_cleaner()
    user_sequence = get_list_from_user(difficulty)
    if is_list_equal(sequence, user_sequence):
        print("You won!")
        return True
    else:
        print("You lost.")
        return False

