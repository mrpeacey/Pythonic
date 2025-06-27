user=input("Rock,Paper,Scissor:").title();
import random
comp=random.choice(["Rock","Paper","Scissor"]);
print("the computer choice was: ",comp);
def program(x,y):

    if(x=="Paper" and y=="Rock"):
        print("You won");
    if(x=="Scissor" and y=="Paper"):
        print("You Won");
    if(x=="Rock" and y=="Scissor"):
        print('you won');
    if(x==y):
        print("Draw");
    else:
        print("You lost");
   
program(user,comp);