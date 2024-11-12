
import random
def pao_ying_chub():
  print("let's play pao ying chub")
  games = list(range(1,9999))
  number_games = int(input("How many games you want to play?: "))
  while number_games not in games:
    print("please enter a number")
    number_games = input("How many games you want to play?: ")

  hands = ["hammer","scissor","paper"]
  score_human = 0
  score_computer = 0
  while score_human+score_computer < number_games:
    print("please choose your hand: [hammer,scissor,paper]")
    a_hand = random.choice(hands)
    user_hand = input("choose your hand: ")
    while user_hand not in hands:
      print("please choose again")
      user_hand = input("choose your hand: ")

    if user_hand in hands:
      print(a_hand,user_hand)
      if a_hand == "hammer":
        if user_hand == "scissor":
          print("you lose")
          score_computer += 1
          print("computer score: "+str(score_computer))
          print("your score: "+str(score_human))
        elif user_hand == "paper":
          print("you win")
          score_human += 1
          print("computer score: "+str(score_computer))
          print("your score: "+str(score_human))
        else:
          print("draw")
          print("computer score: "+str(score_computer))
          print("your score: "+str(score_human))
          
      elif a_hand == "scissor":
        if user_hand == "hammer":
          print("you win")
          score_human += 1
          print("computer score: "+str(score_computer))
          print("your score: "+str(score_human))
        elif user_hand == "paper":
          print("you lose")
          score_computer += 1
          print("computer score: "+str(score_computer))
          print("your score: "+str(score_human))
        else:
          print("draw")
          print("computer score: "+str(score_computer))
          print("your score: "+str(score_human))
      elif a_hand == "paper":
        if user_hand == "hammer":
          print("you lose")
          score_computer += 1
          print("computer score: "+str(score_computer))
          print("your score: "+str(score_human))
        elif user_hand == "scissor":
          print("you win")
          score_human += 1
          print("computer score: "+str(score_computer))
          print("your score: "+str(score_human))
        else:
          print("draw")
          print("computer score: "+str(score_computer))
          print("your score: "+str(score_human))
  
  if score_human > score_computer:
    print(f"you win: with your score{score_human} / computer score {score_computer}")
  elif score_human < score_computer:
    print(f"you lose: with your score = {score_human} / computer score = {score_computer}")
  else:
    print(f"draw: with your score{score_human} / computer score {score_computer}")
  

pao_ying_chub()
