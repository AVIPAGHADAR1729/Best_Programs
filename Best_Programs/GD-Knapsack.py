##x=[10,5,15,7,6,18,3]
##y=[2,3,5,7,1,4,1]

#Profit
##x=[79,32,47,18,26,85,33,40,45,59]
###Weight
##y=[85,26,48,21,22,95,43,45,55,52]

##x=[30,40,45,77,90]
##y=[5,10,15,22,25]

##x=[10.35,4.95,14.65,11.55,22.35,1.95,7.85,10.15,6.35]
##y=[45,20,60,45,100,10,40,45,20]

print("Profit:)")
x=list(map(float,input().split()))
print("Weight:)")
y=list(map(float,input().split()))

if len(x) == len(y):
    data=list(map(lambda x,y: [x,y,x/y],x,y))
else:
    print("Please Enter Same lenght of Profit and Weight")
    data = []

##for x in data:
##    print(x)

    
##data=sorted(data,key=lambda x: x[2],reverse=True)
##print(data)

CAP=int(input("Capacity:)\n"))
#CAP=60
#PF=[]

##print(data)


def myfun(data,tp):
    PF=[]
    global CAP
    index=int()
    bvar=bool()
    if tp=='MinWT':
        index=1
        bvar=False
    elif tp=='MaxPT':
        index=0
        bvar=True

    elif tp=='P/W':
        index=2
        bvar=True
    else:
        print("!!!!  args in MinWt,MaxPT or P/W !!!!!")
        return

    data=sorted(data,key=lambda x: x[index],reverse=bvar)
    print(data)
    
    print('\t','========'*2,tp,'========'*2,'\t')
    print('Weight\tValue\tRemaining(CAP)\tsum')
    
    for i in range(len(data)):
        
        W=data[i][1]
        if(CAP>W):
            CAP-=W
            PF.append(data[i][0])
        
        else:
            PF.append(data[i][0]*CAP/W)
            break
        
        print(W,'\t',data[i][0],'\t',CAP,'\t\t',sum(PF))
        
    print("Total Profit :- ",sum(PF))



if __name__ == '__main__':
    myfun(data,"P/W")












##for i in range(len(data)):
##    W=data[i][1]
##    if(CAP>W):
##        CAP-=W
##        PF.append(data[i][0])
##        
##    else:
##        
##        PF.append(data[i][0]*CAP/W)
##        break
##        
##    print(W,CAP,sum(PF))



#print(sum(PF))
