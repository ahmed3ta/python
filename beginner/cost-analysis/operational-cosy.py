#This script askes User for a name, priority, cost 
#and arrange them for the user, for an estimate 
#cost analysis based on the set priority


dictionary_of_cost = {}
end = False
item = 0
while end != True:
    name=input("please enter the name of the cost:  ")
    priority = int(input("It's very Important to get a Priority to anything that you spend\nplease enter the priority of the cost, '1' for Highest, '2', or '3' for lowest Priority"  ))
    cost = float(input("please enter the ammount of the cost  "))
    dictionary_of_cost[name] = [cost,priority]
    print(f"successfulle added ' {name} ' with ammount of \({cost}\)")
    print("your list now is as follows:")
    print("""    --------------------------------
    name\t|\tcost\t|\tpriotiy""")
    for i in dictionary_of_cost:
        print(f"""    --------------------------------
    {i}\t|\t{dictionary_of_cost[i][0]}\t|\t{dictionary_of_cost[i][1]}""")
    another_item = input(f"You have added {item+1} items\nDo you need to add another item? 'y' or 'n'  ")
    item +=1
    if another_item == "n":
        end = True
print("Here's You Item List to keep it near")
print(dictionary_of_cost)
print("Remember, comittment and Displine are the only way of Financial well being")
tough = 0 
normal = 0
good = 0
print("""    --------------------------------
    name\t|\tcost\t|\tpriotiy""")
for i in dictionary_of_cost:
    print(f"""    --------------------------------
    {i}\t|\t{dictionary_of_cost[i][0]}\t|\t{dictionary_of_cost[i][1]}""")
    if dictionary_of_cost[i][1] == 1:
        tough += dictionary_of_cost[i][0]
        normal += dictionary_of_cost[i][0]
        good += dictionary_of_cost[i][0]
    elif dictionary_of_cost[i][1] == 2:
        normal += dictionary_of_cost[i][0]
        good += dictionary_of_cost[i][0]
    elif dictionary_of_cost[i][1] == 3:
        good += dictionary_of_cost[i][0]
print(f"In Tough Times, you only have to spend {tough}$\nIn Normal Times {normal}$\nAnd in Good Old times {good}$")
print("Bye!, See you")
