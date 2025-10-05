import random
import dice

print("🎲 Welcome to Battle of Dices! 🎲")

#Function to end the game
gameover = False

round = 0
player1_roll_list = []
player2_roll_list = []
player_names = []
player_wins = []

winning_score = 3

player_rolls_history = []

#Getting number of players
number_of_players = int(input("Insert the number of players: "))

#Getting player names
for i in range(number_of_players):
    name = input(f"Name of player {i + 1}: ")
    player_names.append(name)

#Initializing score for each player
for i in range(number_of_players):
    player_wins.append(0)

for i in range(number_of_players):
    player_rolls_history.append([])

while gameover == False:

  print(f"Round {round + 1}:")
  current_rolls = []

  for i in range(number_of_players):
      roll1 = dice.rollD8()
      roll2 = dice.rollD12()
      roll_sum = roll1 + roll2
      current_rolls.append(roll_sum)
      player_rolls_history[i].append(roll_sum)
      print(f"Player {player_names[i]} rolled {roll1} and {roll2}, the sum was: {roll_sum}")

  input("\nPress ENTER to continue...")
  max_roll = max(current_rolls)

  winners = []
  for j in range(len(current_rolls)):
      if current_rolls[j] == max_roll:
          winners.append(player_names[j])
          player_wins[j] += 1

  print(f"Winners of this round are {winners}!")
  # So far so good right? But how to check who got the highest roll?


  for z in range(number_of_players):
    if player_wins[z] >= winning_score:
          print(f"\n{player_names[z]} is the newest Battle of Dices Champion!")
          gameover = True

  if gameover == False:
      print("This heated Battle of Dices is still going on! Who will win in the end? ")
  round += 1

filename = input("Enter the file name to save the results: ")
with open(filename, "w") as file:
    for round_number in range(round):
        file.write(f"Round {round_number + 1} ")
        rolls_str = ""
        for i in range(number_of_players):
            rolls_str += (f"{player_names[i]} roll sum was {player_rolls_history[i][round_number]}")
            if i < number_of_players - 1:
                rolls_str += ", "
        print(f"Saving {rolls_str}")

        file.write(rolls_str + "\n")
