# Thais Lizeth Santos Acosta
# A01630056
# Mastery21


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

x =(int(input("Give me a number:")))

do_fac = factorial(x)

print ("The factorial number is:", do_fac)
