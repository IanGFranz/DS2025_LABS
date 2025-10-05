import random
import dice

print("🎲 Welcome to Battle of Dices! 🎲")

# Variables to keep track of the score:
player1_wins = 0
player2_wins = 0
round = 0
player1_roll_list = []
player2_roll_list = []

while player1_wins < 3 and player2_wins < 3:

  input("\nPress ENTER to roll the dice for Player 1...")

  player1_roll = dice.rollD6()
  print("Player 1 rolled: ", player1_roll)
  player1_roll_list.append(player1_roll)

  input("\nPress ENTER to roll the dice for Player 2...")
  
  player2_roll = dice.rollD6()
  print("Player 2 rolled: ", player2_roll)
  player2_roll_list.append(player2_roll)

  input("\nPress ENTER to continue...")

  # So far so good right? But how to check who got the highest roll?

  if player1_roll > player2_roll:
      player1_wins = player1_wins + 1
      print("Player 1 wins this round!")
      print("Because ", player1_roll," is greater than ", player2_roll)
  elif player1_roll == player2_roll:
      print("Amaaazzinng! This round has a tie!")
  else:
      player2_wins = player2_wins + 1
      print("Player 2 wins this round!")
      print("Because ", player2_roll," is greater than ", player1_roll)

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

print("Rounds: ", end="")
for i in range(round):
    print(f"| {i+1} ", end="")
print("|")

print("P1:     ", end="")
for r in player1_roll_list:
    print(f"| {r} ", end="")
print("|")

print("P2:     ", end="")
for r in player2_roll_list:
    print(f"| {r} ", end="")
print("|")

filename = input("Enter the file name to save the results: ")
with open(filename, "w") as file:
    file.write("Rounds: ")
    for i in range(round):
        file.write(f"| {i+1} ")
    file.write("\n")

    file.write("P1:     ")
    for r in player1_roll_list:
        file.write(f"| {r} ")
    file.write("|\n")

    file.write("P2:     ")
    for r in player2_roll_list:
        file.write(f"| {r} ")
    file.write("|\n")
