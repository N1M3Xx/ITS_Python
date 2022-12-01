def istogramma(n):
    print("\n\n")
    m=n[0]
    for x in range(len(n)-1):
        if((m>n[x+1]) and ((n[x+1]<0) or (m<0))):
            m=n[x+1]
        elif(m<=n[x+1]):
            continue
        else:
            m=0
    for x in range(len(n)):
        a=""
        if(n[x]>=m):
            if(n[x]>0):
                for z in range((m*-1)):
                    a=a+" "
                for y in range(n[x]):
                    a=a+"*"
            else:
                for z in range(n[x]+(m*-1)):
                    a=a+" "
                for y in range(n[x]*-1):
                    a=a+"*"
        print(a)
        
c=0
ct=0
l=[]

while(c==0):
    ct+=1
    print("\n\nInserisci il ", ct,"° numero: ")
    n=input("")
    if((n.isnumeric()==True) or ((n[1:].isnumeric()) and n[0]=="-")):
        n=int(n)
        if(n==0):
            c=1
        else:
            l.append(n)
    else:
        print("\nErrore di inserimento\n")
        
istogramma(l)