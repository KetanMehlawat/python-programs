class Banking:
    totalbalance=0
    def __init__(self):
        __accno=None
        __cname=None
        __balance=None
    def getdetails(self):
        self.__accno=input("Input account number ")
        self.__cname=raw_input("Enter customer name ")
        self.__balance=input("Enter amount ")
        Banking.totalbalance+=self.__balance
    def dispdetails(self):
        print self.__accno
        print self.__cname
        print self.__balance
    @staticmethod
    def totalbance( ):
        print "Total Balance: ",Banking.totalbalance
    def depwith(self,c):
        if c==1:
            amt=input("Enter amount to be deposited ")
            self.__balance+=amt
            Banking.totalbalance+=amt
        else:
            if c==2:
                amt=input("enter amount to be withdrawn ")
                self.__balance-=amt
                print self.__balance
    def calculate(self):
        int=self.__balance*0.04
        self.__balance+=int
        print "Interest is: ",int
        print "The new balance is ",self.__balance
    def raccno(self):
        return self.__accno
cust=list( )
n=input("Enter the number of customers ")
for i in range(0,n):
    c=Banking( )
    c.getdetails( )
    cust.append(c)
for j in range(0,n):
    cust[j].dispdetails( )
for k in range(0,n):
    cust[k].calculate( )
while True:
    choice=raw_input("So you want to deposite or withdraw money ")
    if choice=='y':
        c=input("Enter 1 for deposite & 2 for withdraw ")
        if c==1 or c==2:
            accno=input("Enter Customer accno ")
            for i in range(0,n):
                if accno==cust[i].raccno( ):
                    cust[i].depwith(c)
                    break
                else:
                    continue
    else:
        break
