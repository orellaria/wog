import random
import requests

def get_exchange_rate():
    try:
        response = requests.get('https://api.exchangerate-api.com/v4/latest/USD')
        rates = response.json().get("rates", {})
        return rates.get("ILS", 0)
    except Exception as e:
        print(f"Error retrieving exchange rate: {e}")
        return 0

def get_money_interval(difficulty):
    usd_amount = random.randint(1, 100)
    rate = get_exchange_rate()
    interval = (usd_amount * rate) - (10 - difficulty), (usd_amount * rate) + (10 - difficulty)
    return usd_amount, interval

def get_guess_from_user(usd_amount):
    return float(input(f"Guess the value of {usd_amount} USD in ILS: "))

def compare_results(guess, interval):
    return interval[0] <= guess <= interval[1]

def play(difficulty):
    usd_amount, interval = get_money_interval(difficulty)
    user_guess = get_guess_from_user(usd_amount)
    if compare_results(user_guess, interval):
        print("You won!")
        return True
    else:
        print(f"You lost. The correct range was {interval[0]} - {interval[1]}.")
        return False


