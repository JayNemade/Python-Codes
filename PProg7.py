"""Iterators"""
sisters = ('Chiya','Roma','Tiya','Nitya','Pihu')
it = iter(sisters)
print(next(it))
print(next(it))

mystr = "banana"

for x in mystr:
  print(x)

class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def next(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
