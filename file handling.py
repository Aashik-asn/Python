f=open("example.txt","w")
f.write("Hello Boy\n")
f.write("I am Aashik")
f.close()

with open("example.txt","a") as f:
    f.write("I MCA F")
    
f=open("example.txt","r")
content=f.read()
print(content)

pos=f.tell()
print("Current Position:",pos)
f.close()
