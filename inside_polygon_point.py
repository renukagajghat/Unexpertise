def area(x1,y1,x2,y2,x3,y3):
    return abs((x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2))/2.0)

def isinside(x1,y1,x2,y2,x3,y3,x,y):
    a=area(x1,y1,x2,y2,x3,y3)
    a1=area(x,y,x2,y2,x3,y3)
    a2=area(x1,y1,x,y,x3,y3)
    a3=area(x1,y1,x2,y2,x,y)
    return (a==a1+a2+a3)

if __name__=="__main__":
    
    l=input().split(" ")
n=len(l)
cordinator=[]
k=0
for i in range(0,int(n/2)):
    a=[]
    for j in range(0,2):
        a.append(float(l[k]))
        k=k+1
    cordinator.append(a)

x,y=input().split(" ")
point=[]
point.append(int(x))
point.append(int(y))

count=0
   
for i in range(1,len(cordinator)-1):
    x1=cordinator[0][0]
    y1=cordinator[0][1]
    x2=cordinator[i][0]
    y2=cordinator[i][1]
    x3=cordinator[i+1][0]
    y3=cordinator[i+1][1]
    x=point[0]
    y=point[1]
    if isinside(x1,y1,x2,y2,x3,y3,x,y):
        count=count+1
if count % 2 == 0:
    print(False)
else:
    print(True)
            