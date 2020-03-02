import random as r

def find():
    x=r.randrange(1,3)
    return x

print("Welcome to Rock-Paper-Scissor game\n1->for Rock\n2->Paper\n3->Scissor\n4->exit")
user=0
computer=0
user_score=0
computer_score=0
while(True):
    print("Input from user :")
    user=int(input())
    if user>4 or user<1:
        print("invalid option")
        break
    if user==4:
        break
    computer=find()
    print("Input from computer :\n",computer)
    if user != computer:   
        if(user==1 and computer==2):
            computer_score+=1
        if(user==1 and computer==3):
            user_score+=1
        if(user==2 and computer==1):
            user_score+=1
        if(user==2 and computer==3):
            computer_score+=1
        if(user==3 and computer==1):
            computer_score+=1
        if(user==3 and computer==2):
            user_score+=1
    print("Score= ",user_score," ",computer_score)
if user_score>computer_score:
    print("User Won")
elif user_score<computer_score:
    print("Computer Won")
else:
    if user_score==0:
        print("You quit so early!")
    else:
        print("Match Draw")
