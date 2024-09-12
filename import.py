from game_data import data
import random

def format_data(account):
  account_name = account["name"]
  account_description = account["description"]
  account_country = account["country"]
  return f"{account_name}, a{account_description}, from{account_country}"

def check_answer(user_guess, a_followers, b_followers):
  if a_followers > b_followers:
    return guess == "a"
  else:
    return guess == "b"

score = 0
game_should_continue = True
account_b = random.choice(data)

while game_should_continue: 

  account_a = account_b
  account_b = random.choice(data)
  
  if account_a == account_b:
    account_b = random.choice(data)
    
  print(f"compare a: {format_data(account_a)}")
  print(f"against b: {format_data(account_b)}")

  guess = input("Who has more followers? Type 'a' or 'b':").lower()
  print("\n" * 20)

  a_follower_count = account_a["follower_count"]
  b_follower_count = account_b["follower_count"]
  is_correct = check_answer(guess, a_follower_count, b_follower_count)

  if is_correct:
    score += 1
    print(f"You're right! current score {score}")
  else:
    print(f"That's wrong. Final score: {score}")
    game_should_continue =  False
