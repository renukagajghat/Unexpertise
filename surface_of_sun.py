import math
 
def getAngle(a, b, c):
    ang = math.degrees(math.atan2(c[1]-b[1], c[0]-b[0]) - math.atan2(a[1]-b[1], a[0]-b[0]))
    return ang + 360 if ang < 0 else ang
 

if __name__ == "__main__":
    #accept the input
    #case2
    # cordination=[[[4,0],[4,-5],[7,-5],[7,0]],[[0.4,-2],[0.4,-5],[2.5,-5],[2.5,-2]]]
    # sun_cordination=[-3.5,1]
    #case1
    cordination=[[[4,0],[4,-5],[7,-5],[7,0]]]
    sun_cordination=[1,1]


    #sorting logic
    for i in range(len(cordination)):
        for j in range(i+1,len(cordination)):
            if cordination[i][0][0] > cordination[j][0][0]:
                temp=cordination[i]
                cordination[i]=cordination[j]
                cordination[j]=temp

    final_ans=0
    susun_angle=-1

    p0=cordination[0][0]
    p1=cordination[0][1]
    p2=cordination[0][2]
    height=abs(abs(p0[1])-abs(p1[1]))
    width=abs(abs(p2[0])-abs(p0[0]))
    ans=float(height+width)

    final_ans=final_ans+ans
    for i in range(len(cordination)-1):
        sun_angle=getAngle((sun_cordination[0], cordination[i][3][0]), sun_cordination, cordination[i][3])
        
        
        p1x=cordination[i][2][0]
        p2x=cordination[i+1][1][0]
        ans=abs(abs(p1x)-abs(p2x))
        ans=ans*math.tan(math.radians(sun_angle))
        diff=ans-abs(abs(cordination[i][2][1])-abs(cordination[i][3][1]))
        
        diff1=abs(abs(cordination[i+1][0][1])-abs(cordination[i+1][1][1]))
        diff2=abs(abs(cordination[i+1][0][0])-abs(cordination[i+1][3][0]))
        ans=abs(diff1-diff)+diff2
        final_ans=final_ans+ans

    print(final_ans)
