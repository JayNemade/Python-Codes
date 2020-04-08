class person:
	
  def __init__(self, name, age):
    self.name = name
    self.age = age
     
  def greet(self):
    print("Hello,"+self.name)

    def Name(self):
    	print(self.name)

p1 = person("Jay", 14)
p1.greet()

class Student(person):
    def __init__(self,sname,sage,grade):
    	person.__init__(self,sname,sage)
        self.grade = grade

    def func(self):
     print(self.name)

s = Student('Nemade',15,9)
s.greet()
s.func()