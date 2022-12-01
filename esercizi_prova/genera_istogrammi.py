def istogramma(n):
    print("\n\n")
    for x in range(len(n)):
        a=""
        for y in range(n[x]):
            a=a+"*"
        print(a)
        
c=0
ct=0
l=[]

while(c==0):
    ct+=1
    print("\n\nInserisci il ", ct,"° numero positivo: ")
    n=input("")
    if(n.isnumeric()==True):
        n=int(n)
        if(n>0):
            l.append(n)
        elif(n<0):
            print("\nErrore di inserimento\n")
        else:
            c=1
    else:
        print("\nErrore di inserimento\n")
        
istogramma(l)