from data import question_data
from data import answers

def playGame():
    print("\nFive Questions will be presented to you and score will be calculated on a scale of 100\n")
    flag = True

    while(flag):
        user_answers = []
        score = 0
        for index, question in enumerate(question_data):
          print(f"\nQuestion no. {index+1}\n")
          print(f"{question[0]}\n")
          for option in question[1]:
            print(f"{option}\t")
        
          while(True):
            user_answer = input("\nType your answer (A or B or C or D) ---> ")
            if user_answer == 'A' or user_answer == 'B' or user_answer == 'C' or user_answer == 'D':
                user_answers.append(user_answer)
                break
            
            else:
                print("\nEnter A or B or C or D only\n")
        
        print("\n")

        for i in range(len(answers)):
            if answers[i] == user_answers[i]:
               score += (100/(len(answers)))
     
        print(f"\nCongratulations! Your Score is {score}")

        while(True):
            print("\nDo you want to play again?(Type 'YES' or 'NO')\n")
            play_again = input("---> ")

            if play_again == 'YES':
               flag = True
               break
        
            elif play_again == 'NO':
               flag = False
               break
            
            else:
                print("\nPlease enter appropriate response")




    