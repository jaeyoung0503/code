# from turtle import Turtle, Screen
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("coral")
# timmy.forward

# my_screen = Screen()
# print(my_screen.canyheight)
# my_screen.exitionclick()

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name", ["Picachu", "Squitle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"
print(table)
print(table)