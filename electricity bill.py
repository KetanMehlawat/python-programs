while True:
    print "Press 1 to continue"
    print "press 0 to exit"
    ch=input("enter your choice")
    if ch>1 or ch<0:
        print ("please press correct button")
        continue
    elif ch==1:
      u=input("units=")
      l=input("enter load=")
      lc=0
      if u<=200:
        charges=u*4
      elif u>200 and u<=400:
        charges=800+(u-200)*5
      else:
        charges=(200*4)+(200*5)+(u-400)*6
      if l<=2:
        lc=40
      elif l>2 and l<=5:
        lc=100
      else:
        lc=30*l
      charges=charges+lc
      print "total amount to be paid is Rs.",charges
    else:
      break
  
