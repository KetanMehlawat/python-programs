import string
import random
lang=["java","c","c++","python","ruby","perl","php","javascript","html","delphi","cobol","ada","groovy","swift","sql","fortran","scratch"]
steps=['''

   +---+
   |   |
       |
       |
       |
       |
 =========''', '''

   +---+
   |   |
   O   |
       |
       |
       |
 =========''', '''

   +---+
   |   |
   O   |
   |   |
       |
       |
 =========''', '''

   +---+
   |   |
   O   |
  /|   |
       |
       |
 =========''', '''

   +---+
   |   |
   O   |
  /|\  |
       |
       |
 =========''', '''

   +---+
   |   |
   O   |
  /|\  |
  /    |
       |
 =========''', '''

   +---+
   |   |
   O   |
  /|\  |
  / \  |
       |
 =========''']
life=start=count=0
word2=" "
out=""
out1=""
print"                                               LANGMAN"
print"                                A Programming Language guessing game"            
in1=random.randint(0,16)
k=lang[in1]
print"NOTE:Not Enter Vowels"
print "Length of given word is ",len(k)
for i in range(0,len(k)):
    if k[i]=="a" or k[i]=="e" or k[i]=="i" or k[i]=="o" or k[i]=="u":
        out1=str(k[i])
    else:
        out1=str(word2)
    out=out+out1
list1=list(out)
print out,
print steps[0]
while True:
    start=0
    in2=raw_input("Enter Your Suggestion For Missing Letters: ")
    if in2 in k:
        while True:
            pos=k.find(in2,start,len(k))
            if pos==-1:
                break
            list1[pos]=in2
            start=pos+1
            if start>=len(k):
                break
        print("".join(list1))
        if list1==list(k):
            print"You Won"
            break
    else:
         life=life+1
         if life==7:
            print"You Lost"
            print"Language was:",k
            break
         print steps[life],
        
        
    
          
