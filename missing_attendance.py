n=int(input("Enter total numbers of student: "))
l=list(map(int,input("Enter the roll numbers:").split()))
for i in range(1,n+1):
    if i not in l:
        print(i)
        break