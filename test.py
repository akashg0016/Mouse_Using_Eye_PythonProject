def findClosestPoints():
    n = int(input())
    r=[]
    xlist = []
    ylist =[]
    sum = []
    count = 0
    for i in range(n):
        x= int(input())
        y= int(input())
        xlist.append(x)
        ylist.append(y)

    smallx=0
    for i in range(n):
        sum.append(xlist[i])
        if(xlist[i]<=0):
            smallx=xlist[i]


    smally=0
    for i in range(n):
        sum.append(ylist[i])
        if(smally<=0):
            smally=ylist[i]

    # for i in range(2*n):
    #     print(sum[i])

    print(smallx)
    print(smally)
    res=0
    res = pow((smallx ** 2 + smally ** 2), (1 / 2))
    return res

























    #     res = pow((x**2 + y**2),(1/2))
    #     r.append(res)
    #     print(res)
    #
    # for i in range(n):
    #     if r[i] in r:
    #         print(r[i])
    #         count+=1;
    #
    # return count

findClosestPoints()







