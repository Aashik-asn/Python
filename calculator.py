def add(a,b):
    return a+b
def multiply(a,b):
    return a*b
def subtract(a,b):
    return a-b
def divide(a,b):
    if b==0:
        return "Undefined"
    return a/b
def modulo(a,b):
    if b==0:
        return "Undefined"
    return a%b

d={'+':add,'-':subtract,'*':multiply,'/':divide,'%':modulo}
while(True):
    a=float(input("Enter first number: "))
    while(True):
        op=input(f"Enter operator {list(d.keys())}: ")
        b=float(input("Enter second number: "))
        res=d[op](a,b)
        if res=="Undefined":
            print(f"{res}, Try Again!!!\n")
            break
        print(f"{a:.2f} {op} {b:.2f} = {res:.2f}")
        flag_cont=input(f"Do you want to continue with {res} (y/n)? :").lower()
        if flag_cont=='y':
            a=res
        else:
            print()
            break
