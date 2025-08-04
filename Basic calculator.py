# Ask the user for two numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

#Ask the user for the operation
print("Choose an operation: +, -, *, /")
operation = input ("Enter operation")

if operation == "+":
   result = number1 + number2
   print(f"{number1 + number2} = {result}")

elif operation == "-":
     result = number1 - number2
     print(f"{number1 - number2} = {result}")

elif operation == "*":
     result = number1 * number2
     print(f" {number1 * number2} = {result}")

elif operation == "/":
     result = number1 / number2
     print(f"{number1 / number2} = {result}")

else:
     result = ("Invalid operation!")


