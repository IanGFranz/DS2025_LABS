print("Welcome to your travel list!")
endProgram = False
cities = []

while endProgram == False:
  print("Please choose one of the following options:")

  option = int(input("(1) Add a new city to the list of visited cities\n(2) View your list of visited cities.\n(3) Sort the list of visited cities.\n" \
  "(4) Shows the number of visited cities\n(5) Remove a given city from the list of visited cities\n(6) Remove all cities from the list of visited cities\n" \
  "(7) Save the list of visited cities to a file.\n(8) Stop the Program\n"))

  match option:
    case 1:
      addedCity = input("What city do you want to add? ")
      cities.append(addedCity)
    case 2:
      print(cities)
    case 3:
      cities.sort()
      print("The list is sorted.")
    case 4:
      print(f"You have visited {len(cities)} cities.")
    case 5:
      removedCity = input("Which city do you want to remove?")
      cities.remove(removedCity)
    case 6:
      cities.clear()
    case 7:
      with open("Visited Places", "w") as file:
        file.write(f"Visited Cities: {cities}")
    case 8:
      endProgram = True

  input("\nPress ENTER to continue...")