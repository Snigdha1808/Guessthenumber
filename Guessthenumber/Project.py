import random as r

n = r.randrange(100)
x = 5

print("Enter the number in the range of 1 to 100")

for i in range(x):
    if i == x - 1:
        print("This is your last chance.")
        print("Enter your guessed number")
        guess = int(input())

        if guess != n:
            print("Sorry. You lost the game")
            print("The number is: ", n)
        elif guess == n:
            print("You guessed the number correctly. CONGRATULATIONS!!")
    else:
        print("Enter your guessed number")
        guess = int(input())

        if guess == n:
            print("You guessed the number correctly. CONGRATULATIONS!!")
            break
        elif guess > n:
            print("Try guessing a little lower")
        else:
            print("Try guessing a little higher")
