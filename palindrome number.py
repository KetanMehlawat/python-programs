while True:
    print "Press 1 to continue"
    print "press 0 to exit"
    ch=input("enter your choice")
    if ch>1 or ch<0:
        print ("please press correct button")
        continue
    elif ch==1:
        n=input("Enter a number ")
        rev=0
        on=n
        while(n!=0):
           r=n%10
           rev=rev*10+r
           n=n/10
        if rev==on:
           print "It is a palindrome number"
        else:
           print "It is not a palindrome number"
    else:
        break
