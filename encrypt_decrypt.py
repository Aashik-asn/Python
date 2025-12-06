def encrypt(text,shift):
    s=""
    for i in text:
        s+=chr(ord(i)+shift)
    print(s)
def decrypt(text,shift):
    s=""
    for i in text:
        s+=chr(ord(i)-shift)
    print(s)

while True:
    text=input("Enter text: ")
    shift=int(input("Enter shift value in integer: "))
    flag=input("Enter \"encrypt\" or \"decrypt\": ").lower()
    if flag=="encrypt":
        encrypt(text,shift)
    elif flag=="decrypt":
        decrypt(text,shift)
    if(input("Do you want to continue (Y/N)? ").lower()=='n'):
        break
