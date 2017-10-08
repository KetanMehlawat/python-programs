while True:
    print "Press 1 to continue"
    print "press 0 to exit"
    ch=input("enter your choice")
    if ch>1 or ch<0:
        print ("please press correct button")
        continue
    elif ch==1:
        num1=input ("enter a three digit number ")
        slc=num1//100
        if slc>9 or num1<1:
          print ("the number is not three digit")
        else:
         num2=num1%10
         num3=num1%100
         num4=num3/10
         num5=num1/100
         ans=num2*num4*num5
         print "product of individual digits is",ans
