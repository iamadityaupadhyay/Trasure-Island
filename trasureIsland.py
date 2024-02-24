name=input("Hello What is your name? ")
print(f"Hello {name} Welcome to Treasure Island Your mission is to find the treasure")
print("You are on a cross over which side do you want to go\n")
first_dir=input("Press left for LEFT and Press right for RIGHT")
if(first_dir=="right"):
  print("Oh No You fell ❄ into a whole.Game is Over")
else:
  option1=input("Do you want to swim or wait for a boat")
  if option1=="swim":
    print("\nAttacked by trout!! Game is over")
  else:
    door=input("Which door You want to open for e.g blue/red/yello")
    if door=="red":
      print("Burned by fire 🔥 Game is over")
    elif door=="blue":
      print("You are waten by beasts")
    elif door=="yellow":
      print("You Won!! ")
    else:
      print("Game is over")