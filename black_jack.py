import random
deck=[11,2,3,4,5,6,7,8,9,10,10,10,10]
while True:
    user=random.sample(deck,2)
    cpu=random.sample(deck,2)
    while(sum(cpu)<21 and sum(user)<21):
        print(f"Your cards: {user}")
        print("cpu's cards:",cpu[:1])
        choice=input("Press \"y\" to pass the chance or \"n\" to draw a card: ").lower()
        if choice=='n':
            user.append(random.choice(deck))
            if 11 in user and sum(user)>21:
                user[user.index(11)]=1
            
        elif choice=='y':
            while(sum(cpu)<18):
                cpu.append(random.choice(deck))
                if 11 in cpu and sum(cpu)>21:
                    cpu[cpu.index(11)]=1
            break
            
    if sum(cpu)>21 or (sum(user)<22 and sum(user)>sum(cpu)):
        print("You won!!")
        print(f"Your deck : {user}")
        print(f"Cpu deck : {cpu}")
    elif sum(user)==sum(cpu):
        print("Its a draw!!")
        print(f"Your deck : {user}")
        print(f"Cpu deck : {cpu}")
    else:
        print("You lost!!")
        print(f"Your deck : {user}")
        print(f"Cpu deck : {cpu}")
    if(input("Do you want to play again(y/n)? ").lower()=='n'):
        break
    print("\n")
