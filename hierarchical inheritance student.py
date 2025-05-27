class student:
    def __init__(self,name,dept):
        self.name=name
        self.dept=dept
    def info(self):
        print("Name:",self.name)
        print("Dept:",self.dept)
class mark(student):
    def __init__(self,name,dept,m1,m2,m3):
        super().__init__(name,dept)
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def show_mark(self):
        print(f"Marks: {self.m1},{self.m2},{self.m3}")
class result(student):
    def __init__(self,name,dept,total):
        super().__init__(name,dept)
        self.total=total
    def show_res(self):
        print("Total Mark: {self.total}")
student1=mark("Aashik","MCA",90,85,99)
student1.info()
student1.show_mark()
print()
total=student1.m1+student1.m2+student1.m3
res1=result(student1.name,student1.dept,total)
res1.info()
res1.show_res()
