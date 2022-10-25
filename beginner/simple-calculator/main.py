

#Calculator

#Add
def add(n1,n2):
  return n1 + n2

#Subtract
def sub(n1,n2):
  return n1 - n2

#Multiply
def mul(n1,n2):
  return n1 * n2

#Division
def dev(n1,n2):
  return n1 / n2

operations = {
  "+" : add,
  "-" : sub,
  "*" : mul,
  "/" : dev
}
def calculator():
  from art import logo
  print(logo)
  num1 = float(input("Enter your first number: "))
  list_of_answers = []
  continue_calc = True
  trials = 0
  while continue_calc:
    if trials > 0:
      print(logo)
      print(f"last Answer was {answer}")
    for key in operations:
      print(key)
    
    operation_symbol = input("pick an opertion from the line above: ")
    num = float(input("Enter The next number: "))
    if trials !=0:
      num1= list_of_answers[trials-1]
    answer = operations[operation_symbol](num1,num)
    list_of_answers.append(answer)
    print(f"{num1} {operation_symbol} {num} = {answer}")
    trials +=1
    exit_calc = input("Do you want continue with the next number?\n'yes' to continue \n'n' for starting new calculation \n'e' for exit").lower()
    
    if exit_calc == "n" :
      continue_calc = False
      calculator()
    elif exit_calc == 'e':
      continue_calc = False
    from replit import clear
    clear()
calculator()

