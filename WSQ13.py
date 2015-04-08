# Thais Lizeth Santos Acosta
# A01630056
# WSQ13

def babylonian(x):
	c=x
	y=0
	while(y!=c):
		y=c
		c=(x/c+c)/2
	return c

a= int(input("Dame un numero:"))

b= babylonian(a)

print("La raiz cuadrada por el metodo Babilonico es:", b)
