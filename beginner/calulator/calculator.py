from art import logo
from replit import clear

#Calculator

#Add
def add(n1,n2):
  return n1 + n2

#subtract
def subtract(n1,n2):
  return n1 - n2

#Mulitiply
def multiply(n1,n2):
  return n1 * n2

#Division 
def divide(n1,n2):
  return n1 / n2


operations = {
  "+" : add,
  "-" : subtract,
  "*" : multiply,
  "/" : divide
}
def calculator():
  clear()
  print(logo)
  num1 = float(input("What is the first number: "))
  continue_calc = "y"
  while continue_calc == "y":
    
    for symbol in operations:
      print(symbol)
    
    operation_symbol = input("Pick an operation from the line above: ")
    
    num2 = float(input("What is the second number: "))
    answer = operations[operation_symbol](num1,num2)
    
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    
    continue_calc = input(f"the last answer was {answer} would you like to continue doing math on it? y or n\n").lower()
    if continue_calc == "n":
      calculator()
    num1 = answer

calculator()
