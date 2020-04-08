f = open("Sample","w")
f.write("This is a text")
f.close()

file = open("Sample","rt")
print(file.read())
file.close()

import os
os.remove("Sample")