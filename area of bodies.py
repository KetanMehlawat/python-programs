while True:
    print "Press 1 to continue"
    print "press 0 to exit"
    ch=input("enter your choice")
    if ch>1 or ch<0:
        print ("please press correct button")
        continue
    elif ch==1:
        while True:
          print "Menu"
          print "1.Area of circle"
          print "2.Area of right angled triangle"
          print "3.Area of rectangle"
          print "4.Area of square"
          print "0.Exit"
          ch=input("enter your choice ")
          if ch<0 or ch>4:
            print "Please enter a valid choice"
            continue
          elif ch==1:
           r=input("Enter radius of circle ")
           a=3.14*(r**2)
           print "Area of circle is ",a,"units"
          elif ch==2:
           b=input("enter base of triangle ")
           h=input("enter height of triangle ")
           a=0.5*b*h
           print "Area of right angled triangle is ",a,"units"
          elif ch==3:
           l=input("enter length of reactangle ")
           b=input("enter breadth of reactangle ")
           a=l*b
           print "Area of reactangle is ",a,"units"
          elif ch==4:
           s=input("enter side of square ")
           a=s*s
           print "Area of square is ",a,"units"
          else:
            break
    else:
        break



        
