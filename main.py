#1 for snake
#0 for water 
#-1 for gun

your_score=0
computer_score=0
draw_score=0
next_choice='y'
while next_choice== 'y':
    
    for i in range(0,5):
        import random

        computer= random.choice([1,0,-1])

        yourChoice=input("enter your character : ")
        youDict={'s':1 ,'w':0 , 'g':-1}
        revDict={1:'snake',0:'water', -1:'gun'}

        if yourChoice not in youDict:
            print("invalid input, try again")
        else:
            you=youDict[yourChoice]
            print(f'your choice : {revDict[you]}\ncomputers choice : {revDict[computer]}')

            if(computer==1 and you==0):
                print("Sorry , you lose!")
                computer_score+=1
            elif(computer ==1 and you==-1):
                print("Congratulation , you win!")
                your_score+=1
            elif(computer==0 and you==1):
                print("Congratulation , you win!")
                your_score+=1
            elif(computer==0 and you==-1):
                print("Sorry , you lose!")
                computer_score+=1
            elif(computer==-1 and you==1):
                print("Sorry , you lose!")
                computer_score+=1
            elif(computer==-1 and you==0):
                print("Congratulation , you win!")
                your_score+=1
            else:
                print(" OOPS!! , it's a draw")
                draw_score+=1
            print(f'your score : {your_score}')
            print(f"computer's score : {computer_score}")
            print(f'Draw score : {draw_score} ')
            
        if i!=4:
            print("..........Next round..........") 
        else:
            print("..........Result time.........")
    print(f"your total score : {your_score}")
    print(f"computer's total score : {computer_score}")
    print(f'total no. of draws : {draw_score}')
            
    if(your_score>computer_score):
        print(":)...you are the winner...:)")
    elif(computer_score>your_score):
            print(":)...computer is the winner...:)")
    else:
            print("It's a tie") 
    next_choice= input("Do you want to play (Y/N)?").lower()
print(".......thanks for playing........")
    

        


