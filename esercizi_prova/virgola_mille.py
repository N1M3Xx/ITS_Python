err=1

while err==1:
    n=input("\nInserire un numero: ")
    if(n.isnumeric()==True):
        err=0
    else:
        print("\nErrore di inserimento")
        
n1=""

for x in range(0, len(n)):
    if((x%3==0) and (x!=0)):
        n1=","+n1
    n1=n[len(n)-x-1]+n1
            
print(n1)