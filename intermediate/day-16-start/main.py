

# import turtle
#
#
# timmy = turtle.Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("brown")
# ahmed = turtle.Turtle()
# ahmed.shape("circle")
# ahmed.forward(100)
# my_screen = turtle.Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()


from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Chamander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align["Pokemon Name"] = "c"


print(table)
