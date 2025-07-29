import random 
num = random.randrange(1000,10000)
n = int(input("Guess the 4 digit number:"))
if n == num:
    print("Great! You guessed the number in you first try, MASTERMIND!")
else:
    ctr=0 
    while n != num:
        ctr += 1
        count=0 
        n = str(n)
        num = str(num)
        correct=['X']*4
        for i in range (4):
            if n[i] == num[i]:
                count+=1
                correct[i]=n[i]
            else:
                continue
        print("Not quite the number but you did get",count,"digit(s) correct")
        print('\n')
        print('\n')
        n = int(input("Enter your next choice : "))
    if count == 0:
        print("None of the numbers in your input match")
    n = int(input("Enter your next choice:"))
    if n == num:
        ctr += 1
        print("You became a mastermind")
        print("It took you only", ctr, "tries")