import random
n=random.randint(1000,9999)
print"               COWS N BULLS"
print"Cow: Correct digit at wrong place"
print"Bull: Correct digit at right place"
print"Random number generated is between 1000 and 9999"
r=str(n)
cows=bulls=0
while True:
    cows=bulls=0
    inp=raw_input("Enter Guess")
    for i in range(0,4):
        if inp[i] in r:
            if inp[i]==r[i]:
                bulls=bulls+1
            else:
                cows=cows+1
    print"Bulls=",bulls
    print"Cows=",cows
    if bulls==4:
        print"!!!You Won!!!"
        break
