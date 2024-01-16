import random as r
n=r.randrange(100)
x=5
print("Enter the numbers within the range 0 and 100")
while x>=0:
    print("Enter your guessed number")
    guess=int(input())
    def check(y):
        if guess==y:
            print("You've guessed correctly. Congratulations!!")
            return True
        elif guess>y:
            print("Try to guess a little lower")
        else:
            print("Try to guess a little higher")
            return False
    if x>1:
        if check(n):
            break
    elif x==1:
        if check(n):
            break
        print("This is your last chance")
    else:
        print("Sorry. You lost!")
        print("The number is: ",n)
    x=x-1
