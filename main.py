#intro
from main import pokemon
print("Welcome to the Pokemon Battle Simulator!")
firstP=str(input("Will you select 1. Charmander, 2. Squirtle, or 3. Bulbasaur? "))
if int(firstP)==1:
    party1=pokemon("Charmander", 5, 20, "Fire", "None", "Ember", "Scratch", "Empty", "Empty")
elif int(firstP)==2:
    party1=pokemon("Squirtle", 5, 20, "Water", "None", "Bubble", "Tackle", "Empty", "Empty")    