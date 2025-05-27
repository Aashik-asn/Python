try:
    n=32/0
except ZeroDivisionError:
    print("Cannot divide by zero")

try:
    l=[12,32,32,4]
    print(l[7])
except IndexError:
    print("Cannot find the index value")

try:
    a="HELLO"
    b=int(a)
except ValueError:
    print("Cannot convert string to int")

try:
    f=open("sadkj.txt","r")
except FileNotFoundError:
    print("incorrect file name")

try:
    raise Exception("MY ERROR")
except Exception as e:
    print(e)
