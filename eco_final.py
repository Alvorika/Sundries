import random


#total
aa=20000*0.5
a=20000*0.5

d=0   # Dominant
h=0   # Hetero
r=0   # Recessive
rate=25

for year in range(1,50):

    #pick 2 gametes to compose an individual
    while(aa>1 and a>1):
        pick1=random.randint(0,1)
        pick2=random.randint(0,1)

        if pick1==pick2==0:
            r+=1
            a-=2
        else:
            if pick1==pick2==1:
                d+=1
                aa-=2
            else:
                h+=1
                a-=1
                aa-=1
        if (a==1 or aa==1):
            break

    #to prevent the case: only 1 "a" or "aa" left but you still pick 2 gametes out which would lead to "-1 left".
    if (aa>a and a==1):
        h+=1
        a-=1
        aa-=1
        d+=int(aa/2)
        aa=0
    if (aa<a and aa==1):
        h+=1
        a-=1
        aa-=1
        r+=int(a/2)
        a=0

    if (aa>a and a==0):
        d+=int(aa/2)
        aa=0
    if (aa<a and aa==0):
        r+=int(a/2)
        a=0


    if year==1:
        print(d+h,r)
    

    #natural selection
    for i in range (1,d):
        death=random.randint(1,100)
        if death>rate:
            d-=1

    for i in range (1,h):
        death=random.randint(1,100)
        if death>rate:
            h-=1

    for i in range (1,r):
        death=random.randint(1,100)
        if death<=rate:
            r-=1

    rate+=1


    #break individuals into 2 gametes and *1.5
    aa=(2*d+h)*2
    a=(h+2*r)*2

    print(d+h,r,aa,a)
    d=h=r=0
