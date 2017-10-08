class student:
    rollno=None
    sname=None
    tmarks=0
    pmarks=0
    def getdata(self):
        self.rollno=input("Enter Roll No. ")
        self.sname=raw_input("Enter Name ")
        self.tmarks=input("Enter marks ")
        self.pmarks=self.tmarks/5.0
    def display(self):
        print ("roll number:"),self.rollno
        print ("Name "),self.sname
        print ("Total Marks "),self.tmarks
        print ("Percentage Marks"),self.pmarks
stud=list( )
n=input("Enter the number of students ")
for i in range(0,n):
    s=student( )
    s.getdata( )
    stud.append(s)
for j in range(0,n):
    stud[j].display( )
