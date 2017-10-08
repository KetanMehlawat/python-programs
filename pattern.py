while True:
    print "Press 1 to continue"
    print "press 0 to exit"
    ch=input("enter your choice")
    if ch>1 or ch<0:
        print ("please press correct button")
        continue
    elif ch==1:
        n=input("enter a number ")
        for r in range(1,n+1):
          for c in range(1,r+1):
            print c,
          print
    else:
        break
    
