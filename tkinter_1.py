import tkinter as tk
def greet():
    name=entry.get()
    label_result.config(text=f"Hello, {name}")
def toggle():
    if subs.get():
        label_check.config(text="Subscribed")
    else:
        label_check.config(text="Not Subscribed")
def select():
    label_gender.config(text=f"Gender : {gender.get()}")

root=tk.Tk()
root.title("Simple GUI")
root.geometry("300x250")

entry=tk.Entry(root)
entry.pack(pady=5)

button=tk.Button(root,text="Greet",command=greet)
button.pack(pady=5)
label_result=tk.Label(root,text="")
label_result.pack(pady=5)

subs=tk.BooleanVar()
checkbutton=tk.Checkbutton(root,text="Subscribe",variable=subs,command=toggle)
checkbutton.pack(pady=5)
label_check=tk.Label(root,text="")
label_check.pack(pady=5)

gender=tk.StringVar()
gender.set(None)

male=tk.Radiobutton(root,text="male",variable=gender,value="Male",command=select)
female=tk.Radiobutton(root,text="female",variable=gender,value="Female",command=select)
male.pack()
female.pack()
label_gender=tk.Label(root,text="Gender: None")
label_gender.pack(pady=5)

root.mainloop()
