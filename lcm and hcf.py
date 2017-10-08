while True:
    print "Press 1 to continue"
    print "press 0 to exit"
    ch=input("enter your choice")
    if ch>1 or ch<0:
      print ("please press correct button")
      continue
    elif ch==1:
       def hcf(x,y):
        if y>x:
           x,y=y,x
        r=x%y
        while r!=0:
          x=y
          y=r
          r=x%y
        print "hcf is ",y
       def lcm(x,y):
         ctr=1
         while True:
           a=x*ctr
           ctr+=1
           d=a%y
           if d==0:
            break
         print "lcm is ",a
       while True:
           print "Menu"
           print "1.hcf"
           print "2.lcm"
           print "0.Exit"
           ch=input("enter your choice")
           if ch==1:
            x=input("enter first number ")
            y=input("enter second number ")
            hcf(x,y)
           elif ch==2:
            x=input("enter first number")
            y=input("enetr second number")
            lcm(x,y)
           elif ch==0:
            break
       else:
            print "Wrong choice"
    else:
      break





    
    
