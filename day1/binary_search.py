import random

msg = "This program will generate a random number between 1 - 100." \
      "You should be able to guess it within 7 times, let's see if you can actually do it"

print(msg)
counter = 0
n = random.randint(1, 100)
guess = int(input("Enter an integer from 1 to 99: "))
while n != "guess" and counter < 7:
    if guess < n:
        print("guess is low")
        guess = int(input("Enter an integer from 1 to 99: "))
    elif guess > n:
        print("guess is high")
        guess = int(input("Enter an integer from 1 to 99: "))
    else:
        print("you guessed it!")
        break
    counter += 1
    print()

if counter < 7:
    print("Congratulations, you won")
else:
    print("Unfortunately, you lost")
