import dice
import copy

print("🎲 Welcome to Battle of Dices! 🎲")

#Function to end the game
gameover = False

round = 0
players = []
player_wins = []
winning_score = 3
player_info = {
    "name": "",
    "email": "",
    "country": "",
    "wins": 0,
    "rolls": [],
}
#Getting number of players
number_of_players = int(input("Insert the number of players: "))
for i in range(number_of_players):
    player = copy.deepcopy(player_info)
    player["name"] = input(f"What is the name of player {i + 1}?")
    player["email"] = input(f"What is the email of player {i + 1}?")
    player["country"] = input(f"What is the country of player {i + 1}?")
    players.append(player)
player_rolls_history = []

while gameover == False:

  print(f"Round {round + 1}:")
  current_rolls = []

  for each_player in players:
      roll = dice.rollD6()
      each_player["rolls"].append(roll)
      current_rolls.append(roll)
      print(f"Player {each_player["name"]} rolled: {roll}")

  input("\nPress ENTER to continue...")
  max_roll = max(current_rolls)

  winners = []
  for each_player in players:
      if each_player["rolls"][-1] == max_roll:
          each_player["wins"] += 1
          print(f"Player {each_player["name"]} won in round {round}")
          winners.append(each_player["name"])

  print(f"Winners of this round are {winners}!")
  # So far so good right? But how to check who got the highest roll?


  for each_player in players:
    if each_player["wins"] >= winning_score:
          print(f"\n{each_player['name']} is the newest Battle of Dices Champion!")
          gameover = True

  if gameover == False:
      print("This heated Battle of Dices is still going on! Who will win in the end? ")
  round += 1

filename = input("Enter the file name to save the results: ")
with open(filename, "w") as file:
    file.write("Player Information:\n")
    for each_player in players:
        file.write(
          f"Name: {each_player['name']}\n"
          f"* E-mail: {each_player['email']}\n"
          f"* Country {each_player['country']}\n"
          f"* Wins: {each_player['wins']}\n"
        )
    file.write("\nGame Rounds:\n")
    for r in range(round):
        rolls_str = ""
        
        for i, each_player in enumerate(players):
            rolls_str += f"{each_player['name']} rolled {each_player['rolls'][r]}"
            if i < len(players) - 1:
                rolls_str = ""
        file.write(f"Round {r + 1}:\n {rolls_str}\n")
    print("\nGame Over! Results saved sucessfully!")
