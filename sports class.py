class Sports:
    totalfess=0
    def __init__(self):
        self.scode=None
        self.sname=None
        self.fees=0
        self.duration=0
    def Newsports(self):
        self.scode=input("Enter the code for your desired sport ")
        self.sname=input("Enter name of your sport ")
    def dispdetails(self):
        if (sname=="table tennis "):
            self.fees=2000
            self.duration=40 minutes
        elif (sname=="cricket"):
            self.fees=2500
            self.duration=70 minutes:
        elif (sname=="Basket Ball"):
            self.fees=1700
            self.duration=65 minutes
        elif (sname=="Football"):
            self.fees=2100
            self.duration=90 minutes
            
