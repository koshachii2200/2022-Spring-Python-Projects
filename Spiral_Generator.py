# File: Spiral.py

# Input: n is an odd integer between 1 and 100
# Output: returns a 2-D list representing a spiral
#         if n is even add one to n

def create_spiral(n):

    rows,cols=(n,n)
    side=int((rows/2)-0.5)

    ar=[[0 for i in range(cols)]for j in range(rows)]

    value=1
    ud=side
    lr=side
    ar[ud][lr]=value
    value+=1

    counter=1
    for r in range(0,side):
        lr+=1
        ar[ud][lr]=value
        value+=1
        x=0
        while(x<counter):
            ud+=1
            ar[ud][lr]=value
            value+=1
            x+=1
        counter+=1
        x=0
        while(x<counter):
            lr-=1
            ar[ud][lr]=value
            value+=1
            x+=1
        x=0
        while(x<counter):
            ud-=1
            ar[ud][lr]=value
            value+=1
            x+=1
        x=0
        while(x<counter):
            lr+=1
            ar[ud][lr]=value
            value+=1
            x+=1
        counter+=1

    lis=[]
    while 1:
        try:
            inp=int(input())
            lis.append(inp)
        except:break

    for x in range(len(lis)):sum_adjacent_numbers(ar,lis[x])

    
# Input: spiral is a 2-D list and n is an integer
# Output: returns an integer that is the sum of the
#         numbers adjacent to n in the spiral
#         if n is outside the range return 0

def sum_adjacent_numbers(spiral, n):
    if(n>(len(spiral)**2)or n<1):print("Index not Found")
    else:
        ud,lr=(0,0)
        for i in range(len(spiral)):
            for j in range(len(spiral)):
                if(spiral[i][j]==n):ud,lr=(i,j)
        ind=spiral[ud][lr]

        a,b,c,d,e,f,g,h=(-1,-1,-1,-1,-1,-1,-1,-1)
        if(ud==0):a,b,c=(0,0,0)
        if(ud==len(spiral)-1):f,g,h=(0,0,0)
        if(lr==0):a,d,f=(0,0,0)
        if(lr==len(spiral)-1):c,e,h=(0,0,0)

        if(a!=0):a=spiral[ud-1][lr-1]
        if(b!=0):b=spiral[ud-1][lr]
        if(c!=0):c=spiral[ud-1][lr+1]
        if(d!=0):d=spiral[ud][lr-1]
        if(e!=0):e=spiral[ud][lr+1]
        if(f!=0):f=spiral[ud+1][lr-1]
        if(g!=0):g=spiral[ud+1][lr]
        if(h!=0):h=spiral[ud+1][lr+1]

        sum=a+b+c+d+e+f+g+h
        print(sum)

def main():

    create_spiral(int(input()))

if __name__ == "__main__":
    main()