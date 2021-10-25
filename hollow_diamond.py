n=6
for i in range(n,0,-1):
    x="* "*i+"  "*(n-i)+"  "*(n-i-1)
    if(i==n):
        x=x+"* "*(i-1)
    else:
        x=x+"* "*(i)
    print(x)
for i in range(2,n+1):
    x="* "*i+"  "*(n-i)+"  "*(n-i-1)
    if(i==n):
        x=x+"* "*(i-1)
    else:
        x=x+"* "*(i)
    print(x)


