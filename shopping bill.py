while True:
    print "Press 1 to continue"
    print "press 0 to exit"
    ch=input("enter your choice")
    if ch>1 or ch<0:
        print ("please press correct button")
        continue
    elif ch==1:
      n=input("input number of product varieties ") 
      tp=0.0
      d=0.0
      for i in range(1,n+1):
       name=raw_input("enter product name ")
       price=input("enter price ")
       q=input("enter quantity ")
       totalprice=q*price
       tp+=totalprice
       d+=q
      vat=tp*0.05
      grandtotal=tp+vat
      print "Vat on products=",vat
      print "Grand total=",grandtotal
      print "Total price\t Total items\t Vat\t"
      print grandtotal,"\t",d,"\t","\t",vat,"\t"
    else:
      break

