import random
x=random.randint(1, 10)
print '\t','\t',"!!!!!!!!!!!!!!!!!!!!You have five chances to test your luck!!!!!!!!!!!!!!!!!!!!"
for i in range(1,6):

    print '\t','\t','\t',"Enter any number ranging between 1---10"
    a=input( "                                                              ::---            ")
    
    if a==x:
        print '\n','\t','\t','\t'," YOU WIN THE GAME!!!!!YIPPIE!!!!!!!!!"
        break
    elif a<x and a<10:
        print '\t','\t','\t'," Your luck is not with you"
        print '\n','\t','\t','\t',"!!!!!!!!!!!!!!!!LOW VALUE!!!!!!!!!!!!!!!!!"
    elif a>x and a<10:
        print '\t','\t','\t',"Your luck is not with you"
        print'\n','\t','\t','\t', "!!!!!!!!!!!!!!!!HIGH VALUE!!!!!!!!!!!!!!!!!"
    else:
        print'\n','\t','\t','\t',"Value Entered is out of range"
        
        

