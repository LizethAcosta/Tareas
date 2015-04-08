# Thais Lizeth Santos Acosta
# A01630056
# WSQ14

def e(a):
	x=a
	e=(1+1/x)**x
	return float(e)

    
h=(int(input("Number of decimal points of accuracy: ")))

k = e(h)


print("The estimate of the constant e is: ",k)
