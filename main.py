#1 for snake
#0 for water 
#-1 for gun
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
        elif(computer ==1 and you==-1):
            print("Congratulation , you win!")
        elif(computer==0 and you==1):
            print("Congratulation , you win!")
        elif(computer==0 and you==-1):
            print("Sorry , you lose!")
        elif(computer==-1 and you==1):
            print("Sorry , you lose!")
        elif(computer==-1 and you==0):
            print("Congratulation , you win!")
        else:
            print(" OOPS!! , it's a draw")


