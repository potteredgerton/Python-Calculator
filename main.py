def calculate(operator, number1, number2):
    if (operator == "+"):
        return number1 + number2
    elif (operator == "-"):
        return number2 - number1
    elif (operator == "*" or operator == "x" or operator == "X"):
        return number1 * number2
    elif (operator == "/"):
        return number1 / number2

while True:
  operator = input("Enter your operator here: ")
  number1 = int(input("Enter number 1 here: "))
  number2 = int(input("Enter number 2 here: "))
  result = calculate(operator, number1, number2)
  print(result)
