# Thais Lizeth Santos Acosta
# A01630056
# WSQ10

import statistics

def totalsum(list):
	sum=0
	for x in range (0,len(list)):
		sum+=list[x]
	return (sum)
def average(list):
	avrg=totalsum(list)/10
	return (avrg)
 
def standarddev(list):
	std= statistics.stdev(list)
	return (std)
 
list=[]

x=0

while(x<10):
    
	num=(float(input("Give me a number for the list:")))
	list.append(num) 
	x=x+1

a = totalsum(list)
b = average(list)
c = standarddev(list)
	
print("The sum is:",a)
print("The average is:",b)
print("The standard deviation is:",c)
