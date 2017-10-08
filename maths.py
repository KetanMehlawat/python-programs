while True:
    print "Press 1 to continue"
    print "press 0 to exit"
    ch=input("enter your choice")
    if ch>1 or ch<0:
        print ("please press correct button")
        continue
    elif ch==1:
        x=input("enter a value ")
        n=input("enter limit ")
        s=0.0
        for p in range(1,n+1):
          s=s+((x**p)/float(p))
        print s
    else:
        break
