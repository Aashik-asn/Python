import turtle as t
tur=t.Turtle()
for i in range(3,8):
    for _ in range(i):
        tur.forward(50)
        tur.right(360/i)
