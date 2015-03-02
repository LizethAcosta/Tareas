# Thais Lizeth Santos Acosta
# A01630056
# WSQ08

def suma(x,y):
    answer = x + y
    return answer

def resta(x,y):
    answer = x - y
    return answer

def multi(x,y):
    answer = x * y
    return answer

def div(x,y):
    answer = x // y
    return answer

def rem(x,y):
    answer = x % y
    return answer

num1 =int(input(" Give me the fist number: "))
num2 =int(input(" Give me the second number: "))

do_sum = suma(num1,num2)
do_resta = resta(num1,num2)
do_multi = multi(num1,num2)
do_div = div(num1,num2)
do_rem = rem(num1,num2)

print (" The sum of the numbers is: ", do_sum)
print (" The difference of the numbers is: ", do_resta)
print (" The product of the numbers is: ", do_multi)
print (" The integer division of the numbers is: ", do_div)
print (" The remainder of the numbers is: ", do_rem)
