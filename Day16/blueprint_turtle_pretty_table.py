# from turtle import Turtle,Screen
# timmy = Turtle()
# my_screen = Screen()
# print(my_screen.canvheight)
# timmy.shape("turtle")
# timmy.color("red","green")
# timmy.forward(100)
# my_screen.exitonclick()
#print (timmy)
#print(my_screen)

from prettytable import PrettyTable

x = PrettyTable()
x.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
x.add_row(["Adelaide", 1295, 1158259, 600.5])
x.add_row(["Brisbane", 5905, 1857594, 1146.4])
x.add_row(["Darwin", 112, 120900, 1714.7])
x.add_row(["Hobart", 1357, 205556, 619.5])
x.add_row(["Sydney", 2058, 4336374, 1214.8])
x.add_row(["Melbourne", 1566, 3806092, 646.9])
x.add_row(["Perth", 5386, 1554769, 869.4])
#print(x)

y = PrettyTable()
y.field_names =["Pokemon Name","Type"]
y.add_row(["Pikachu","Electric"])
y.add_row(["Squirtle","Water"])
y.add_row(["Charmender","Fire"])
print(y)
print()
print()

table = PrettyTable()
table.add_column("Pokemon Name",["Pikachu","Squirtle","Charmender"])
table.add_column("Type",["Electric","Water","Fire"])
table.align = "l"    ## For Alignment 
print(table)