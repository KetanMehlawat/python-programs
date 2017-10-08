while True:
    print "Press 1 to continue"
    print "press 0 to exit"
    ch=input("enter your choice")
    if ch>1 or ch<0:
        print ("please press correct button")
        continue
    elif ch==1:
        n=input("Enter a number")
        f=0
        for i in range(2,n):
          if n%i==0:
           f=1
        if f==0:
           print "it is a prime number"
        else:
           print "it is not a prime number"
    else:
        break
