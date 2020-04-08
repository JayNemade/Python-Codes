#Dealing with Strings
sent = "Jay is {} yrs old"
str = 'Hello, World'
str2 = ' Hello World '
age = 14

print(str[4:8])

#strip() method to remove any whitespaces
print(str2.strip())

#lower() and upper() method
print(str.lower(),str.upper())

#replace() method
print(str.replace("H","J"))

#split() method to split a string into a array
print(str.split(","))

#format() method to add a integer to a string 
print(sent.format(age))