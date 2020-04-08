#Lists,Tuples,Sets,Dictionaries

"""LISTS"""

#printing Lists
my_list = ['Jay','Yogendra','krupal','Rishab','Pryansh']
print(my_list[2])

#Looping through lists
for x in my_list:
  print(x)

#len() method for strings and Arrays
print(len(my_list))  

#adding items to the lists
my_list.append('Atharva')
my_list.insert(1,'Pawan')
print(my_list)

#removing items from list
my_list.pop()
my_list.remove('Rishab')
del my_list[4]
print(my_list)
#clear() method empties the list

#Coping the list
thisList = list(my_list)#copy() method does the same
print(thisList)
"""
a empty  list is defined by
<list name> = list()

Python has a set of built-in methods that you can use on lists.

Method	    Description
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list

"""

"""TUPLES"""
my_tuple = ('Jay','Pavni','Yogendra','krupal')

for x in my_tuple:
	print(x)

#To check if an item exists  in the tuple
if 'Pavni' in my_tuple:
	print(my_tuple[1])
#to delete a tuple
del my_tuple

"""
a empty  list is defined by
<list name> = tuple()

Python has two built-in methods that you can use on tuples.

Method	Description
count()	Returns the number of times a specified value occurs in a tuple
index()	Searches the tuple for a specified value and returns the position of where it was found

"""

"""SETS"""

my_set = {'Jay','Pavni', 'Pawan', 'Yogendra', 'krupal'}

for x in my_set:
	print(x)

"""	Python has a set of built-in methods that you can use on sets.

Method	Description
add()	Adds an element to the set
clear()	Removes all the elements from the set
copy()	Returns a copy of the set
difference()	Returns a set containing the difference between two or more sets
difference_update()	Removes the items in this set that are also included in another, specified set
discard()	Remove the specified item
intersection()	Returns a set, that is the intersection of two other sets
intersection_update()	Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	Returns whether two sets have a intersection or not
issubset()	Returns whether another set contains this set or not
issuperset()	Returns whether this set contains another set or not
pop()	Removes an element from the set
remove()	Removes the specified element
symmetric_difference()	Returns a set with the symmetric differences of two sets
symmetric_difference_update()	inserts the symmetric differences from this set and another
union()	Return a set containing the union of sets
update()	Update the set with the union of this set and others
"""
"""Dictionaries"""
ferrari = {
	'modal':'Spyder',
	'color':'red',
	'engine':'4 Cylinder',
    'body':'Super Aero'
}
for i in ferrari:
	print(i)

for k in ferrari:
     print(ferrari[k])	