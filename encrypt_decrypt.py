def cypher(text,shift):
    s=""
    for i in text:
        s+=chr(ord(i)+shift)
    print(s)
while True:
    text=input("Enter text: ")
    shift=int(input("Enter shift value in integer: "))
    flag=input("Enter \"encrypt\" or \"decrypt\": ").lower()
    if flag=='decrypt':
        shift*=-1
    cypher(text,shift)
    if(input("Do you want to continue (Y/N)? ").lower()=='n'):
        break
