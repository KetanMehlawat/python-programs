while True:
    print "Press 1 to continue"
    print "press 0 to exit"
    ch=input("enter your choice")
    if ch>1 or ch<0:
        print ("please press correct button")
        continue
    elif ch==1:
        n=input("enter a number ")
        for r in range(n,0,-1):
          for c in range(r,n+1,1):
             print c,
          print
    else:
        break
    
