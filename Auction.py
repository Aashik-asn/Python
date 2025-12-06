d=dict()
while True:
    name=input("Enter your name: ")
    bid=int(input("Enter your bid: "))
    d[name]=bid
    n=input("Do you want to continue (y/n)?: ").lower()
    if n=='n':
        break
high=0
name=''
for i in d:
    if d[i]>high:
        high=d[i]
        name=i
print(f'The winner is {name} with bid ${high}')
