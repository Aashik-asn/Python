import random
print("Guess the number from 1 to 100")
while True:
    level=input("Choose the difficulty(easy or hard)? ").lower()
    if level=='easy':
        lives=10
        break
    elif level=='hard':
        lives=5
        break
    else:
        print("Invalid Level")
num=random.randint(1,100)

while lives>0:
    guess=int(input("Guess the number: "))
    if guess==num:
        print(f"Its correct and you won with {lives} lives")
        break
    elif guess>num:
        print("Too big")
        lives-=1
        print(f"Remaining lives : {lives}")
    else:
        print("Too small")
        lives-=1
        print(f"Remaining lives : {lives}")
if lives==0:
    print(f"You lost and the number is {num}")
