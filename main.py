
x=int(input("digite el numero"))
def numero_primo (x):
     c =0
     r= True
     for i in range(1,x+1):
         if(x%i==0):
            c+=1
         if(c>2):
            r = False
            break
     return r
if (numero_primo(x)==True):
    print("Es primo")
else:
     print ("NO es primo")