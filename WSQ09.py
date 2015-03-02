# Thais Lizeth Santos Acosta
# A01630056
# WSQ09

import sys

b= "yes"
while b == ("yes"):
    

    num= (input("Give me a positive integer number: "))
    if (num.isdigit() == False):
        print ("This is not what I ask :(")
        sys.exit()
    else:
            num=int(num)

            factorial = 1


    if num < 0:
        print("Sorry but factorial doesn't exist for negative numbers!")
    else:
            for i in range(1,num + 1):
                factorial = factorial*i
            print("The factorial number is",factorial)

    b= (input("You want to try again? "))

else:
    print("Have a nice day!")
    sys.exit()
