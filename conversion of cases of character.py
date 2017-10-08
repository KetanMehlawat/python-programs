while True:
    print "Press 1 to continue"
    print "press 0 to exit"
    ch=input("enter your choice")
    if ch>1 or ch<0:
        print ("please press correct button")
        continue
    elif ch==1:
        n=raw_input("enter a character or string ")
        x=' '
        for i in range(0,len(n)):
          if ord(n[i])>=65 and ord(n[i])<=90:
            x+=chr(ord(n[i])+32)
          elif ord(n[i])>=97 and ord(n[i])<=122:
             x+=chr(ord(n[i])-32)
          else:
            break
        print x
    else:
        break
   
        
