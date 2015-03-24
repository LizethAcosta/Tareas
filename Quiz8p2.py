# Thais Lizeth Santos Acosta
# A01630056
# Quiz 8

def find_threes (x):
    sum = 0
    for element in (x):
        if (element%3 == 0):
            sum = sum + element

    return sum

x = [0,4,2,6,9,8,3,12]


y = find_threes(x)

print ("De la lista [0,4,2,6,9,8,3,12] la suma de los divisibles entre tres es:",y)
