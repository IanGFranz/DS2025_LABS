#Welcome message
print("Welcome to Python programming!")

#Basic arithmetic operations
#Adding two numbers
result_addition = 2 + 6
print("The result of the addition is: ", result_addition)

#Multiplying two numbers
result_multiplication = 5 * 3
print("The result of the multiplication is: ", result_multiplication)

#Printing a simple message
print("Hello World")

#Variable assignments
A = 10 #Assigning value 10 to variable A
B = 4 #Assigning value 4 to variable B

#Performing the printing results of arithmetic operations
print("The result of the addition is", A + B)
print("The result of the multiplication is", A + B)
print("The result of the division is", A + B)

#Using variables to store user information
name = "Bob" #Assigning a name to the variable
age = 28  #Assigning an age to the variable

#Printing user information
print("Hi! My name is", name, "and I am", age,"years old")
print(f"In 2 years i will be {age + 2} years old.")

#Conditional statement based on age
if age > 30:
  print(f"Access granted. Welcome {name}.")
else:
  print(f"Access recused. Common {name}, you can come back in {30 - age} years.")

#List of usernames
usernames = ["Mark", "Sara", "Ahmad", "Johanna"]

#Looping through the list and printing welcoming messages
for user in usernames:
  print(f"Welcome {user}")

#Looping to demonstrate range and multiplications
for i in range(0, 10):
  print(f"The double of {i} is {2 * i}")

#Experimenting with the print() function
#Printing a greeting message
print("Hello, Data Scientists!")

#Printing user's full name
print("Ian Gabriel da Luz Franz")

#Demonstrating input function
pseudoname = input("please enter your pseudoname: ")
print("Hello ", pseudoname)

#Demonstrate final variable values
print("The variable A is ", A)
print("The variable B is ", B)
print("The variable name is ", name)
print("The variable age is ", age)
print("The variable pseudoname is ", pseudoname)
print("The variable usernames is ", usernames)  