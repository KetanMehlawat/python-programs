while True:
    print "Press 1 to continue"
    print "press 0 to exit"
    ch=input("enter your choice")
    if ch>1 or ch<0:
        print ("please press correct button")
        continue
    elif ch==1:
        n=input("Enter a number ")
        d=10
        on=n
        s=0.0
        r=0.0
        while(n!=0):
           r=n%d
           s+=(r**3)
           n=n/d
        if s==on:
          print "It is an armstrong number"
        else:
          print "It is not an armstrong number"
    else:
        break
