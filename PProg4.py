#Loops and Conditionals

#while Loops

i = 1
while i < 10:
  print(i)
  if i == 9:
  	break
  i += 1


#For Loops#
for x in range(5):
	print(x+1)

ferrari = dict(modal="Spyder",color="red",engine="Turboshaft",max_speed=290)

for x in ferrari:
	print(x,ferrari[x])
x = "False"
y = "True"
if x == "True":
	print('true')

elif x == "False":
	print('false')

else:
	print('false')