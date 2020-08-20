import math
 
def getAngle(a, b, c):
    ang = math.degrees(math.atan2(c[1]-b[1], c[0]-b[0]) - math.atan2(a[1]-b[1], a[0]-b[0]))
    return ang + 360 if ang < 0 else ang
 

if __name__ == "__main__":
    #accept the input
    #case2
    # co_orinates=[[[4,0],[4,-5],[7,-5],[7,0]],[[0.4,-2],[0.4,-5],[2.5,-5],[2.5,-2]]]
    # sun_co_orinates=[-3.5,1]
    #case1
    
    l=[];
    l=input().split(" ")
    n=len(l)
    co_orinates=[]
    k=0
    new_l=[]

    for i in range(0,int(n/2)):
        a=[]
        for j in range(0,2):
            a.append(float(l[k]))
            k=k+1
        new_l.append(a)
    co_orinates.append(new_l)

    x,y=input().split(" ")
    sun_co_orinates=[]
    sun_co_orinates.append(int(x))
    sun_co_orinates.append(int(y))

    #print(co_orinates)
    #print(sun_co_orinates)
        
    #co_orinates=[[[4,0],[4,-5],[7,-5],[7,0]]]
    #sun_co_orinates=[1,1]


    #sorting logic
    for i in range(len(co_orinates)):
        for j in range(i+1,len(co_orinates)):
            if co_orinates[i][0][0] > co_orinates[j][0][0]:
                temp=co_orinates[i]
                co_orinates[i]=co_orinates[j]
                co_orinates[j]=temp

    final_ans=0
    sun_angle=-1

    p0=co_orinates[0][0]
    p1=co_orinates[0][1]
    p2=co_orinates[0][2]
    height=abs(abs(p0[1])-abs(p1[1]))
    width=abs(abs(p2[0])-abs(p0[0]))
    ans=float(height+width)

    final_ans=final_ans+ans
    for i in range(len(co_orinates)-1):
        sun_angle=getAngle((sun_co_orinates[0], co_orinates[i][3][0]), sun_co_orinates, co_orinates[i][3])
        
        
        p1x=co_orinates[i][2][0]
        p2x=co_orinates[i+1][1][0]
        ans=abs(abs(p1x)-abs(p2x))
        ans=ans*math.tan(math.radians(sun_angle))
        diff=ans-abs(abs(co_orinates[i][2][1])-abs(co_orinates[i][3][1]))
        
        diff1=abs(abs(co_orinates[i+1][0][1])-abs(co_orinates[i+1][1][1]))
        diff2=abs(abs(co_orinates[i+1][0][0])-abs(co_orinates[i+1][3][0]))
        ans=abs(diff1-diff)+diff2
        final_ans=final_ans+ans

    print(final_ans)