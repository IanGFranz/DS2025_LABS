print("Welcome to the inventory")
stopProgram = False

inventory = {
  "apple": 50,
  "banana": 30,
  "orange": 20,
  "strawberry": 10,
  "cherry": 5,
}

print(f"Here's the inventory:\n{inventory}")

while stopProgram == False:

  choice = int(input("Choose an option\n(1)Add item/ Add quantity for an item\n(2)Remove quantity from an item\n(3)Check quantity from an item\n" \
  "(4)See the current stock for every item\n(5)Stop program\n"))

  match choice:
    case 1:
      itemAddChoice = input("What item do you want to add\n")
      itemAddQuantity = int(input("How much do you want to add?\n"))
      if itemAddChoice in inventory:
        inventory[itemAddChoice] += itemAddQuantity
      else:
        inventory[itemAddChoice] = itemAddQuantity
    case 2:
      itemRemoveChoice = input("What item do you want to remove from?\n")
      itemRemoveQuantity = int(input("How much do you want to remove?\n"))
      if itemRemoveChoice in inventory:
        inventory[itemRemoveChoice] -= itemRemoveQuantity
      else:
        print("This item is not in stock!")
    case 3: 
      itemCheckChoice = input("What item do you want to check?\n")
      if itemCheckChoice in inventory:
        print(inventory[itemCheckChoice])
      else:
        print("This item is not in stock!")
    case 4:
      print(f"Here's the inventory:\n{inventory}")
    case 5:
      stopProgram = True