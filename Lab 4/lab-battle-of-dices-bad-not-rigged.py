import random

print("🎲 Welcome to Battle of Dices! 🎲")

# Variables to keep track of the score:
player1_wins = 0
player2_wins = 0

# Round 1
input("\nPress ENTER to roll the dice...")

player1_round1_roll = random.randint(1, 8)
player2_round1_roll = random.randint(1, 8)

print("Player 1 rolled: ", player1_round1_roll)

print("Player 2 rolled: ", player2_round1_roll)

input("Pre\nss ENTER to continue...")

# So far so good right? But how to check who got the highest roll?

if player1_round1_roll > player2_round1_roll:
    player1_wins += 1
    print("Player 1 wins this round!")
    print("Because ", player1_round1_roll," is greater than ", player2_round1_roll)
elif player1_round1_roll == player2_round1_roll:
    print("Amaaazzinng! This round has a tie!")
else:
    player2_wins = player2_wins + 1
    print("Player 2 wins this round!")
    print("Because ", player2_round1_roll," is greater than ", player1_round1_roll)

# We can print the game score:
print("The game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")

# Now we need to check if either player won.
if player1_wins == 3:
    print("Player 1 is the newest Battle of Dices Champion! ")
elif player2_wins == 3:
    print("Player 2 is the newest Battle of Dices Champion! ")
else:
    print("This heated Battle of Dices is still going on! Who will win in the end? ")

# Round 2
input("\nPress ENTER to roll the dice...")

player1_round2_roll = random.randint(1, 8)
player2_round2_roll = random.randint(1, 8)

print("Player 1 rolled: ", player1_round2_roll)

print("Player 2 rolled: ", player2_round2_roll)

input("Pre\nss ENTER to continue...")

# So far so good right? But how to check who got the highest roll?

if player1_round2_roll > player2_round2_roll:
    player1_wins += 1
    print("Player 1 wins this round!")
    print("Because ", player1_round2_roll," is greater than ", player2_round2_roll)
elif player1_round2_roll == player2_round2_roll:
    print("Amaaazzinng! This round has a tie!")
else:
    player2_wins = player2_wins + 1
    print("Player 2 wins this round!")
    print("Because ", player2_round2_roll," is greater than ", player1_round2_roll)

# We can print the game score:
print("The game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")

# Now we need to check if either player won.
if player1_wins == 3:
    print("Player 1 is the newest Battle of Dices Champion! ")
elif player2_wins == 3:
    print("Player 2 is the newest Battle of Dices Champion! ")
else:
    print("This heated Battle of Dices is still going on! Who will win in the end? ")

# Round 3
input("\nPress ENTER to roll the dice...")

player1_round3_roll = random.randint(1, 8)
player2_round3_roll = random.randint(1, 8)

print("Player 1 rolled: ", player1_round3_roll)

print("Player 2 rolled: ", player2_round3_roll)

input("Pre\nss ENTER to continue...")

# So far so good right? But how to check who got the highest roll?

if player1_round3_roll > player2_round3_roll:
    player1_wins += 1
    print("Player 1 wins this round!")
    print("Because ", player1_round3_roll," is greater than ", player2_round3_roll)
elif player1_round3_roll == player2_round3_roll:
    print("Amaaazzinng! This round has a tie!")
else:
    player2_wins = player2_wins + 1
    print("Player 2 wins this round!")
    print("Because ", player2_round3_roll," is greater than ", player1_round3_roll)

# We can print the game score:
print("The game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")

# Now we need to check if either player won.
if player1_wins == 3:
    print("Player 1 is the newest Battle of Dices Champion! ")
elif player2_wins == 3:
    print("Player 2 is the newest Battle of Dices Champion! ")
else:
    print("This heated Battle of Dices is still going on! Who will win in the end? ")

# Round 4
input("\nPress ENTER to roll the dice...")

player1_round4_roll = random.randint(1, 8)
player2_round4_roll = random.randint(1, 8)

print("Player 1 rolled: ", player1_round4_roll)

print("Player 2 rolled: ", player2_round4_roll)

input("Pre\nss ENTER to continue...")

# So far so good right? But how to check who got the highest roll?

if player1_round4_roll > player2_round4_roll:
    player1_wins += 1
    print("Player 1 wins this round!")
    print("Because ", player1_round4_roll," is greater than ", player2_round4_roll)
elif player1_round4_roll == player2_round4_roll:
    print("Amaaazzinng! This round has a tie!")
else:
    player2_wins = player2_wins + 1
    print("Player 2 wins this round!")
    print("Because ", player2_round4_roll," is greater than ", player1_round4_roll)

# We can print the game score:
print("The game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")

# Now we need to check if either player won.
if player1_wins == 3:
    print("Player 1 is the newest Battle of Dices Champion! ")
elif player2_wins == 3:
    print("Player 2 is the newest Battle of Dices Champion! ")
else:
    print("This heated Battle of Dices is still going on! Who will win in the end? ")

# Round 5
input("\nPress ENTER to roll the dice...")

player1_round5_roll = random.randint(1, 8)
player2_round5_roll = random.randint(1, 8)

print("Player 1 rolled: ", player1_round5_roll)

print("Player 2 rolled: ", player2_round5_roll)

input("Pre\nss ENTER to continue...")

# So far so good right? But how to check who got the highest roll?

if player1_round5_roll > player2_round5_roll:
    player1_wins += 1
    print("Player 1 wins this round!")
    print("Because ", player1_round5_roll," is greater than ", player2_round5_roll)
elif player1_round5_roll == player2_round5_roll:
    print("Amaaazzinng! This round has a tie!")
else:
    player2_wins = player2_wins + 1
    print("Player 2 wins this round!")
    print("Because ", player2_round5_roll," is greater than ", player1_round5_roll)

# We can print the game score:
print("The game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")

# Now we need to check if either player won.
if player1_wins == 3:
    print("Player 1 is the newest Battle of Dices Champion! ")
elif player2_wins == 3:
    print("Player 2 is the newest Battle of Dices Champion! ")
else:
    print("This heated Battle of Dices is still going on! Who will win in the end? ")
print("Rounds: | 1 | 2 | 3 | 4 | 5 |")
print(f"P1:     | {player1_round1_roll} | {player1_round2_roll} | {player1_round3_roll} | {player1_round4_roll} | {player1_round5_roll} |")
print(f"P2:     | {player2_round1_roll} | {player2_round2_roll} | {player2_round3_roll} | {player2_round4_roll} | {player2_round5_roll} |")