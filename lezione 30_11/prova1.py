
x=[0, 200, 0, 400, 0, 600]
y=[0, 400, 0, 600, 200, 0]
c=["g", "g", "g", "g", "g", "g"]

x1_change = -200
y1_change = 0
block=200
dis_width=800
dis_height=800

def change_color(c):
    if(c=="g"):
        return "b"
    if(c=="b"):
        return "y"
    else:
        return "b"
for ct in range(len(x)-1):
    r=0
    x[ct]+=x1_change
    y[ct]+=y1_change
    
    if x[ct]>=dis_width-block:
        x[ct]=dis_width-block
    if x[ct]<0:
        x[ct]=0
    if y[ct]>=dis_height-block:
        y[ct]=dis_height-block
    if y[ct]<0:
        y[ct]=0
    for ct1 in range(ct+1, len(x)-1):
        m=ct1+r
        if(x[ct]==x[m]) and (y[ct]==y[m]) and (c[ct]==c[m]):
            c[ct]=change_color(c[ct])
            del x[m]
            del y[m]
            del c[m]
            r-=1
        elif(x[ct]==x[m]) and (y[ct]==y[m]) and (c[ct]!=c[m]):
            x[m]+=x1_change
            y[m]+=y1_change
    
        
    print(x)