# Thais Lizeth Santos Acosta
# A01630056
# WSQ12

def mcd(a,b):
    if a == b:
        return a
    elif a > b:
        answer = mcd ((a-b),b)
    else:
        answer = mcd (a,(b-a))
    return answer

x = (int(input("Dame el primer numero:")))
y = (int(input("Dame el segundo numero:")))

h = mcd(x,y)

print ("El comun divisor es:",h)
