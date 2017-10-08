while True:
    print "Press 1 to continue"
    print "press 0 to exit"
    ch=input("enter your choice")
    if ch>1 or ch<0:
        print ("please press correct button")
        continue
    elif ch==1:
       t=raw_input("enter a.m. or p.m. ")
       h1=input("enter hours ")
       m1=input("enter minutes ")
       h2=input("enter hours to be added ")
       m2=input("enter minutes to be added ")
       h3=h1+h2
       m3=m1+m2
       if m3>=60:
          h3+=1
          m3=m3-60
       if t=="a.m." and h3>12 and h3<24:
          h3=h3-12
          t="p.m."
       elif t=="p.m." and h3>12 and h3<24:
          t="a.m."
       if h3>=24:
          h3=h3-24
       print h3,":",m3,t
    else:
      break
