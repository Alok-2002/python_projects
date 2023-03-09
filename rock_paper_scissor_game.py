import random
def rps():
    options = ["Rock","Paper","Scissor"] 
    tie_matches = 0
    Round=0
    count_1 = 0
    count_2 = 0
    while True:
            print("Rock Paper Scissor Game: ")
            your_points,computer_points = 0,0  
            Round+=1
            print("Round",Round,"Start: ")
            print("Please select any one option: ")
            print("1.Rock","2.Paper","3.Scissor",sep="\n")  
            Your_choice=int(input())
            if Your_choice == 1:
                    print("You selected Rock ")
                    Your_choice="Rock"
            elif Your_choice == 2:
                    print("You selected Paper ")
                    Your_choice="Paper"
            elif Your_choice==3:
                    print("You selected Scissor ")
                    Your_choice="Scissor"
            else:
                    print("Invalid Choice")
                    break
            Computer_choice = random.choice(options)  
            print("Computer selected:",Computer_choice)

            if Your_choice == Computer_choice:    
                    your_points += 1
                    computer_points += 1
                    count_1+=1
                    count_2+=1
                    tie_matches+=1
                    print("This Round is Draw:")

            elif (Your_choice == "Paper" and Computer_choice == "Rock") or (Your_choice == "Rock" and Computer_choice == "Scissor") or(Your_choice == "Scissor" and Computer_choice == "Paper"):
                    your_points+=1
                    count_1+=1
                    print("You won this Round")
            else:
                    computer_points += 1
                    count_2+=1
                    print("Computer won this Round")

            if your_points > computer_points:
                    print("You Won the game.\nComputer Lost The Game.")
                    print("Score is:","\nYour score:",your_points,"\nComputer score:",computer_points,sep=" ")
            elif computer_points > your_points:
                    print("You Lost the game.\nComputer won the game:")
                    print("Score is:","\nYour score:",your_points,"\nComputer score:",computer_points,sep=" ")
            else:
                    print("Match Draw")
                    print("Score","\nYour score:",your_points,"\nComputer score:",computer_points,sep=" ")

            user_choice=input("Do You Want to Play again ? (Yes/Exit): ").upper()
            if user_choice=='YES' or user_choice == 'Y' :
                    continue             
            else:
                    print("\nTotal Matches Played ",Round)
                    print("\nTie Matches ",tie_matches)
                    print("\nYour Final Score is",count_1-tie_matches)
                    print("\nComputer Final Score is",count_2-tie_matches)
                    perc=((count_1-tie_matches)*100)/Round
                    print("\nYour Overall Performance: ",round(perc,2),"%")
                    break

                    
# rps()
                
