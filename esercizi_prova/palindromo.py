def rendi_palindromo(a):
    for y in range(int(len(a)/2)):
        for x in range(y, int(len(a)/2)-y):
            if(a[x]!=a[len(a)-1-x]):
                if(a[x]>a[len(a)-1-x]):
                    n=a[x]-a[len(a)-1-x]
                    a.insert(x+1, n)
                    a[x]=a[len(a)-1-x]
                else:
                    n=a[len(a)-1-x]-a[x]
                    a.insert(x+1, n)
                    a[len(a)-1-x]=a[x]
    return a

a=[1, 2, 3, 4, 5, 6, 7, 8, 9]
palindromo=True

print(a)

for x in range(int(len(a)/2)):
    if(a[x]!=a[len(a)-1-x]):
        palindromo=False
        
if(palindromo==True):
    print("\nL'array è palindromo")
else:
    a=rendi_palindromo(a)
    print("\nL'array convertito è ", a)
