while True:
    print "Press 1 to continue"
    print "press 0 to exit"
    ch=input("enter your choice")
    if ch>1 or ch<0:
        print ("please press correct button")
        continue
    elif ch==1:
        x=input ("enter the year ")
        a=x%400
        b=x%4
        if a==0:
         print "it is a leap year"
        elif b==0 and x%100!=0:
         print "it is a leap year"
        else:
         print "it is not a leap year"
    else:
        break
        
