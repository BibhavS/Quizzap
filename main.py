# A Simple Quiz Game made by Bibhav Shrestha Run the program to play
from operations import playGame

print("\n\tWelcome to Quizzap")
print("A Simple Quiz Game created by Bibhav Shrestha\n\n")

print("Start the game!!!\n")

flag = True

while(flag):
    print("\nType 'YES' or 'NO'\n")
    choice = input("--> ")

    if choice == "YES":
       playGame()
       flag = False

    elif choice == "NO":
       flag = False

    else:
       print("\nPlease enter appropriate response")


print("\nThank you for your playing my game\n")