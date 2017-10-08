while True:
    print "Press 1 to continue"
    print "press 0 to exit"
    ch=input("enter your choice")
    if ch>1 or ch<0:
        print ("please press correct button")
        continue
    elif ch==1:
        while True:
         print"Menu"
         print"1.From celcius to fahrenheit"
         print"2.From fahrenheit to celcius"
         print"3.From celcius to kelvin"
         print"4.From kelvin to celcius"
         print"5.From kelvin to fahrenheit"
         print"6.From fahrenheit to kelvin"
         print"0.Exit"
         ch=input("enter your choice ")
         if ch<0 or ch>6:
          print"please enter correct choice"
          continue
         elif ch==1:
          t=input("temperature in celcius ")
          f=((9/5.0)*t)+32
          print "temperature in fahrenheit is ",f
         elif ch==2:
          t=input("temperature in fahrenheit ")
          c=((t-32.0)*(5/9.0))
          print "temperature in celcius is ",c
         elif ch==3:
          t=input("temperature in celcius ")
          k=t+273.0
          print "temperature in kelvin is ",k
         elif ch==4:
          t=input("temperature in kelvin ")
          c=t-273.0
          print "temperatur in celcius is ",c
         elif ch==5:
          t=input("temperature in kelvin ")
          f=((9/5.0)*t)+32
          print "temperature in fahrenheit is ",f
         elif ch==6:
          t=input("temperature in fahrenheit ")
          k=((t-32)*(5/9.0))+273
          print "temperature in kelvin is ",k
         else:
           break
    else:
        break
     
    
