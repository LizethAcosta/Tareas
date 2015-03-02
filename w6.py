
# Thais Lizeth Santos Acosta
# A01630056
# WSQ06
 
from random import randint
 
print("Guess what number I'm thinking between 1 and 100!")
a = int(input("Number: "))
x = randint(1,100)
 
while (a != x):
        if (a>x):
            print ("I'm sorry but is to high.") 
        else:         
            print ("I'm sorry but is to low.")
        a = int(input(("Try again:")))

print("You got it!")


