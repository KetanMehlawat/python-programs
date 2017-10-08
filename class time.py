class Time:
    def __init__(self):
        self.h=0
        self.m=0
        self.s=0
    def getTime(self):
        self.h=input("Enter hours ")
        self.m=input("Enter minutes ")
        self.s=input("Enter seconds ")
    def dispTime(self):
        print "Total hours= ",self.h
        print "Total minutes= ",self.m
        print "Total seconds= ",self.s
    def addTime(self,t1,t2):
        t3=Time( )
        t3.h=t1.h+t2.h
        t3.m=t1.m+t2.m
        t3.s=t1.s+t2.s
        if t3.s>=60:
            t3.m+=1
            t3.s-=60
        if t3.m>=60:
            t3.h+=1
            t3.m-=60
        if t3.h>=24:
            t3.h-=24
        return t3
t1=Time( )
t2=Time( )
t3=Time( )
t1.getTime( )
t2.getTime( )
t3=t3.addTime(t1,t2)
t3.dispTime( )
