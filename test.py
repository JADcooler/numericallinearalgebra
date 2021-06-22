print("GAUSS SEIDAL")
n=3 # or any other
a=[[5,-2,3],[-3,9,1],[2,-1,-7]]
b=[-1,2,3]
x=[0,0,0]
#xtemp=[0,0,0]
round_till=4
for g in range(10): # 10 iterations
    print("iteration ",g+1)
    #x=xtemp.copy()
    for i in range(n): # xi iteration
        print("x",i+1," = ",end='')
        sum=b[i]
        print("( ",b[i],end=' ')
        for j in range(n):
            if(i!=j):
                sum-=a[i][j]*x[j]
                if(a[i][j]<0):
                    print('+',end=' ')
                print(-a[i][j],end='*')
                print(x[j],end=' ')
        x[i]=sum/a[i][i]
        x[i]=round(x[i],round_till)
        print(" = ",round(sum,round_till),'/',a[i][i])

    for i in range(n):
        print("x",i+1," is ",x[i])

    #x[j]=(b[j]-)/a[j][j]
