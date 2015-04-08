# Thais Lizeth Santos Acosta
# A01630056
# WSQ11

def invertir(inf):
 inf=str(inf)
 inf=inf[::-1]
 inf=int(inf)
 return(inf)


numerosenrango=[] 
lychrel=[]

inf=int(input("Dime el numero inferior:"))
sup=int(input("Dime el numero superior:"))

for i in range(sup-inf+1): 
 numerosenrango.append(inf) 
 inf=inf+1 

palindromos=0
nolychrel=0
candidatos=0

for i in numerosenrango:
 volteado=invertir(i)
 if i==volteado:
  palindromos=palindromos+1
 else: 
  iteracion1=volteado+i
  iteracion2=invertir(iteracion1)
  for i1 in range(30):
   if iteracion1==iteracion2:
    nolychrel=nolychrel+1
    break 
   else:
    iteracion1=iteracion1+iteracion2
    iteracion2=invertir(iteracion1)
    if (i1==29):
     candidatos=candidatos+1
     lychrel.append(i)

print("Hay ",palindromos,"palindromos")
print("Hay ",nolychrel,"que no son lychrel")
print("Hay ",candidatos," numero que son candidatos a lychrel")

if candidatos!=0: 
 print("Los numeros lychrel son:", lychrel)
