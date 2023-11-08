from data import question_data  
from data import answers

def playGame():
    print("\nFive Questions will be presented to you and score will be calculated on a scale of 100\n")
    

print("\tWelcome to Quizzy")
print("A quiz game created by Bibhav Shrestha\n\n")

print("Start the game!!!\n")

flag = True

while(flag):
    print("\nType 'YES' or 'NO'\n")
    choice = input("-->")

    if choice == "YES":
       playGame()
       flag = False

    elif choice == "NO":
       flag = False

    else:
       print("\nPlease enter appropriate response")


print("\nThank you for your time!!!")