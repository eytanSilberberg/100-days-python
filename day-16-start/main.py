from turtle import Turtle, Screen
from prettytable import PrettyTable

# timmy = Turtle()
# my_screen = Screen()

table = PrettyTable()

table.add_column('Pokemon', ['Picachu', 'Chamander', 'Balbazaour'])
table.add_column('Type', ['Electric', 'Fire', 'Ground'])
table.align = 'l'
print(table)
