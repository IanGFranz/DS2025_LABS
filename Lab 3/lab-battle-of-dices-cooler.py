import random
import dice

print("🎲 Welcome to Battle of Dices! 🎲")

# Variables to keep track of the score:
player1_wins = 0
player2_wins = 0
round = 0

while player1_wins < 3 and player2_wins < 3:
  
  player1_roll1 = dice.rollD20()
  player2_roll1 = dice.rollD20()
  player1_roll2 = dice.rollD8()
  player2_roll2 = dice.rollD8()

  input("\nPress ENTER to roll the dice...")

  print("Player 1 rolled a D20, the result was: ", player1_roll1)

  print("Player 2 rolled a D20, the result was: ", player2_roll1)

  print("Player 1 rolled a D8, the result was: ", player1_roll2)

  print("Player 2 rolled a D8, the result was: ", player2_roll2)

  #Sum of points
  player1_sum = player1_roll1 + player1_roll2
  player2_sum = player2_roll1 + player2_roll2

  print(f"Player 1 got {player1_sum} points")
  print(f"Player 2 got {player2_sum} points")

  input("\nPress ENTER to continue...")

  # So far so good right? But how to check who got the highest roll?

  if player1_sum > player2_sum:
      player1_wins = player1_wins + 1
      print("Player 1 wins this round!")
      print("Because ", player1_sum," is greater than ", player2_sum)
  elif player1_sum == player2_sum:
      print("Amaaazzinng! This round has a tie!")
  else:
      player2_wins = player2_wins + 1
      print("Player 2 wins this round!")
      print("Because ", player2_sum," is greater than ", player1_sum)

  # We can print the game score:
  print("The game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")

  #Counts the rounds
  round = round + 1

  # Now we need to check if either player won.
  if player1_wins == 3:
      print(f"Player 1 is the newest Battle of Dices Champion! It took him {round} rounds")
  elif player2_wins == 3:
      print(f"Player 2 is the newest Battle of Dices Champion! It took him {round} rounds ")
  else:
      print("This heated Battle of Dices is still going on! Who will win in the end? ")
