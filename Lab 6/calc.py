import math

print("*** Welcome to Basic Calculator ***")
print("Choose a mathematical operation: ")
userChoice = int(input("(1) Add two numbers\n(2) Subtract two numbers\n(3) Multiply two numbers\n(4) Divide two numbers\n"))

numberlist = []
try:
  number = int(input("Add a number (type ! to stop): "))
  numberlist.append(number)
  while number != "!":
    number = int(input("Add a number: "))
    numberlist.append(number)
except:
  def addition():
    return sum(numberlist)
  def subtraction():
    result = numberlist[0]
    for i in numberlist[1:]:
        result -= i
    return result
  def multiplication():
    result = 1
    for n in numberlist:
        result *= n
    return result
  def division():
    return [n / 2 for n in numberlist]
  match userChoice:
    case 1:
      total = addition()
      print(f"The addition of {numberlist} is {total}")
    case 2:
      total = subtraction()
      print(f"The subtraction of {numberlist} is {total}")
    case 3:
      total = multiplication()
      print(f"The multiplication of {numberlist} is {total}")
    case 4:
      total = division()
      print(f"The division of {numberlist} is {total}")
    case _:
      print("Invalid menu choice.")
    