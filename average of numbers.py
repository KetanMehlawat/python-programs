while True:
    print "Press 1 to continue"
    print "press 0 to exit"
    ch=input("enter your choice")
    if ch>1 or ch<0:
        print ("please press correct button")
        continue
    elif ch==1:
        n=input("enter the quantity of numbers=")
        s=0.0
        for i in range (1,n+1):
          a=input("enter no.")
          s=s+a
          a=s/n
        print "the average is ",a
    else:
        break
