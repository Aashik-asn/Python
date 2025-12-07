import random
while True:
    words=["python", "javascript", "algorithm", "developer", "keyboard",
           "software", "circuit", "protocol", "encrypt", "variable",
           "interface", "database", "desktop", "server", "compiler",
           "monitor", "debugger", "backend", "frontend", "library",
           "adventure", "mystery", "galaxy", "universe", "horizon",
           "mountain", "ocean", "forest", "desert", "volcano",
           "giraffe", "penguin", "elephant", "octopus", "dolphin",
           "sunflower", "rainbow", "thunder", "snowflake", "earthquake"]
    org=random.choice(words)
    life=5
    target=['_' for i in range(len(org))]

    while ('_' in target) and (life>0):
        print(*target)
        choice=input(f"Guess a letter: ").lower()[0]
        if (choice in target):
            print("Try again, You have already choosed this letter")
            print(f"You got {life} lives remaining!!!\n")
            continue
        elif (choice not in org):
            life-=1
            print("Wrong guess!!")
            print(f"You got {life} lives remaining!!!\n")
            continue
        for i in range(len(org)):
            if choice==org[i]:
                target[i]=choice
        print("That was nice guess!!")
        print(f"You got {life} lives remaining!!!\n")

    if '_' in target:
        print(f"Better luck next time, the man is dead and the correct word is \"{org}\"")
    else:
        print("Congratulation, The man is saved!!!")
    if(input("If you want to terminate(press \"n\") or Enter any to play again: ").lower()=='n'):
        break
