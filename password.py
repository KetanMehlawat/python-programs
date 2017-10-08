while True:
    print "Press 1 to continue"
    print "press 0 to exit"
    ch=input("enter your choice ")
    if ch>1 or ch<0:
        print ("please enter a correct choice")
        continue
    elif ch==1:
        print ("NOTE:For a strong password atleast one uppercase,one lowercase,one digit,one specialcase character,no space and atleast 8 characters should be there")
        password=raw_input("enter your password ")
        l=len(password)
        u=0
        lw=0
        d=0
        s=0
        sp=0
        if l>=8:
            for i in range(0,l):
                if password[i].isupper():
                    u+=1
                elif password[i].islower():
                    lw+=1
                elif password[i].isdigit():
                    d+=1
                elif password[i].isspace():
                    s+=1
                else:
                    sp+=1
            if u==0 or lw==0 or d==0 or sp==0 or s>=1:
                print "ERROR: Invalid password"
            else:
                print"Valid password"
        else:
            print"ERROR: Invalid password"
    else:
        break
            
        
