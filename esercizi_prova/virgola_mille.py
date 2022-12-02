err=1

while err==1:
    n=input("\nInserire un numero: ")
    if(n.isnumeric()==True):
        err=0
        
n1=""
c=0

for x in range(len(n), 0, -1):
    if((c%3==0) and (c!=0)):
        n1=","+n1
    n1=n[x-1]+n1
    c+=1
            
print(n1)