import random

#Roll the dice
result = random.randint(1, 20)

#Pressing the enter key
if input() == ("") :

  #Show the result
  print("You rolled a d20, the result was", result)