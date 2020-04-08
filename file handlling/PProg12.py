f = open("Sample document", "w")
f.write("Now the file has more content!")
f.close()

#open and read the file after the appending:
f = open("Sample document", "r")
print(f.read())
