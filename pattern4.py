while True:
    print "Press 1 to continue"
    print "press 0 to exit"
    ch=input("enter your choice")
    if ch>1 or ch<0:
        print ("please press correct button")
        continue
    elif ch==1:
        n=input("Enter limit")
        a=1
        for i in range(1,n+1):
          for j in range(1,i+1):
            print a,
            a+=1
            if a==n+1:
              break
          print
    else:
        break
