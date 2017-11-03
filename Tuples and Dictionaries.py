####### Tuples #########

'''
* A tuple is a sequence of immutable Python objects. Tuples are sequences, just like lists.
'''

# Define a tuple
my_tuple = ()

my_tuple = (1,2,3,5,4)
print(my_tuple) # (1, 2, 3, 5, 4)


my_tuple = ('Hello', 1, "World", 7)
print(my_tuple) # ('Hello', 1, 'World', 7)
print(my_tuple[0]) # Hello
print(my_tuple[3]) # 7
print(my_tuple[1:3]) # (1, 'World')


# Tuples usually supports the sequence operations supported by string and lists:

# Concatenation
a = (1, 3)
b = (2, 4)
c = a + b
print(c) # (1, 3, 2, 4)

# Repetition
a = (1,2,3,4,5)
b = 2
c = a * b
print(c) #  (1, 2, 3, 4, 5, 1, 2, 3, 4, 5)

# Indexing and slicing
a = (1, 2, 3, 4, 5)
print(a[0], a[1:5]) # 1 (2, 3, 4, 5)

# List to tuple
my_list = [1, 2,3, 4, 5]
my_tuple = tuple(my_list)
print(my_tuple) # (1, 2, 3, 4, 5)


# Sort a tuple
my_tuple = (2, 5, 1, 4, 3)
a = sorted(my_tuple) # It converts tuple to list and sort
print(a) # [1, 2, 3, 4, 5]


######
B = (1, [2, 3], 4)
B[1][0] = 'spam'
print(B) # (1, ['spam', 3], 4)

# how to add value to a tuple?
t = (1,2,3)
t = t + (1,)
print (t) # (1,2,3,1)

a = (1,2,3,5,6)
a = a[:3] + (4,) + a[3:]
print(a) # (1, 2, 3, 4, 5, 6)

# How to input an integer tuple from user?
my_tuple = tuple(map(int,input().split()))
print(my_tuple)

###
my_tuple = ()
for i in range(5):
    a = int(input())
    my_tuple += (a,)

print(my_tuple)
'''
Input:
1
2
3
4
5

Output:
(1, 2, 3, 4, 5)
'''





############### Dictionaries ###################
# empty dictionary
my_dict = {}

# dictionary with integer keys
my_dict = {1: 'apple', 2: 'ball'}
print(my_dict) # {1: 'apple', 2: 'ball'}

# dictionary with mixed keys
my_dict = {'name': 'John', 1: [2, 4, 3]}
print(my_dict) # {'name': 'John', 1: [2, 4, 3]}

# using dict()
my_dict = dict({1:'apple', 2:'ball'})
print(my_dict)  # {1: 'apple', 2: 'ball'}

# from sequence having each item as a pair
my_dict = dict([(1,'apple'), (2,'ball')])
print(my_dict) # {1: 'apple', 2: 'ball'}



### How to access elements from a dictionary?
my_dict = {1: 'Rezwan', 'Haque' : 7}
print(my_dict[1]) # Rezwan
print(my_dict['Haque']) # 7
print(my_dict.get('Haque')) # 7
print(my_dict.keys()) # dict_keys([1, 'Haque'])



### Python Dictionary methods (https://www.programiz.com/python-programming/dictionary)
'''
clear()	=> Remove all items form the dictionary.

copy()	=> Return a shallow copy of the dictionary.

fromkeys(seq[, v]) => Return a new dictionary with keys from seq and value equal to v (defaults to None).

get(key[,d]) =>	Return the value of key. If key doesnot exit, return d (defaults to None).

items()	=> Return a new view of the dictionary's items (key, value).

keys()	Return a new view of the dictionary's keys.

pop(key[,d]) => Remove the item with key and return its value or d if key is not found. If d is not provided and key is not found, raises KeyError.

popitem() => Remove and return an arbitary item (key, value). Raises KeyError if the dictionary is empty.

setdefault(key[,d]) =>	If key is in the dictionary, return its value. If not, insert key with a value of d and return d (defaults to None).

update([other])	=> Update the dictionary with the key/value pairs from other, overwriting existing keys.

values() => Return a new view of the dictionary's values

'''


# Map two lists into a dictionary in Python
keys = ['a', 'b', 'c']
values = [1, 2, 3]
my_dict = dict(zip(keys, values))
print(my_dict) # {'a': 1, 'b': 2, 'c': 3}

## OR
my_dict = dict((k, v) for k, v in zip(keys, values))
print(my_dict) # {'a': 1, 'b': 2, 'c': 3}


d = {'a0': [1, 2, 3], 'a1': [4, 5, 6]}
my_dict = zip(*d.values())
print(*my_dict) # (1, 4) (2, 5) (3, 6)


x = ['1', '2', '3', '4']
y = [[1,0],[2,0],[3,0],[4,]]
my_dict = {key:value for key, value in zip(x,y)}
print(my_dict) # {'1': [1, 0], '2': [2, 0], '3': [3, 0], '4': [4]}


### Make a dictionary in Python from input values
strs="""A1023 CRT
        A1029 Regulator
        A1030 Therm"""

my_dict = dict(x.split() for x in strs.splitlines())
print(my_dict) # {'A1023': 'CRT', 'A1029': 'Regulator', 'A1030': 'Therm'}



#####
n = int(input())          #n is the number of items you want to enter
d ={}
for i in range(n):
    text = input().split()     #split the input text based on space & store in the list 'text'
    d[text[0]] = text[1]       #assign the 1st item to key and 2nd item to value of the dictionary
print(d)
'''
Input:
3
A1023 CRT
A1029 Regulator
A1030 Therm

Output: 
{'A1023': 'CRT', 'A1029': 'Regulator', 'A1030': 'Therm'}
'''



'''Important Link: 
(1) Add new keys to a dictionary? (https://stackoverflow.com/questions/1024847/add-new-keys-to-a-dictionary)
(2) Map two lists into a dictionary in Python (https://stackoverflow.com/questions/209840/map-two-lists-into-a-dictionary-in-python)
(3) zip two values from the dictionary in Python (https://stackoverflow.com/questions/32222563/zip-two-values-from-the-dictionary-in-python)
(4) Python equivalent of zip for dictionaries (https://stackoverflow.com/questions/16458340/python-equivalent-of-zip-for-dictionaries)
(5) Make a dictionary in Python from input values (https://stackoverflow.com/questions/14147369/make-a-dictionary-in-python-from-input-values)

'''





'''
** You are now able to solve following online-judge problems.
_____________________________________________________________
(1) HackerRank | DefaultDict Tutorial
(2) HackerRank | Tuples

'''


