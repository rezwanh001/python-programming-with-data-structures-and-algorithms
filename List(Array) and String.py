########################## List(Array) ##########################

# empty list
my_list = []

# list of integers
my_list = [1, 2, 3, 4, 5]

# list with mixed datatypes
my_list = [1, "Hello", 3.4, 2, 'World']

# nested list
my_list = ["mouse", [8, 4, 6], ['a'], ['x', 'y', 'z']]


# Index if list
my_list = ['H', 'L', 'L', 'O']
print(my_list[0])
# Output : H
print(my_list[3])
# Output: O
print(my_list[-1])
# Output: O
print(my_list[-0])
# Output: H
print(my_list[-4])
# Output: H


# Nested List
n_list = ["Happy", [2,0,1,5]]

# Nested indexing

print(n_list[0][1])
# Output: a

print(n_list[1][3])
# Output: 5

num_list = [1, 2, 3, 4, 5 , 6, 7, 8, 9]
print(num_list[0:3])
# Output : [1, 2, 3]
print(num_list[2:])
# Output : [3, 4, 5, 6, 7, 8, 9]
print(num_list[:3])
# Output: [1, 2, 3]
print(num_list[:-1])
# Output: [1, 2, 3, 4, 5, 6, 7, 8]

# Inverse the list
print(num_list[::-1])
# Output : [9, 8, 7, 6, 5, 4, 3, 2, 1]
print(*reversed(num_list)) # 9 8 7 6 5 4 3 2 1

############ How to store value into the list
my_list = [] # declare the empty list
n = int(input('Enter the size of list : '))
for i in range(n):
    a = int(input())
    my_list.append(a)

print(my_list)
''' Input and Output: 
Enter the size of list : 5
1
2
3
4
5
[1, 2, 3, 4, 5]
'''
#You can store value this way:
my_list = list(map(int, input().split())) # after new line value store will be ended
print(my_list)
'''
Input: 
7 8 9 6 5 4

Output: 
[7, 8, 9, 6, 5, 4]
'''


my_list = [5, 3, 4 , 1, 2]
# sort the list
my_list.sort()
print(my_list) #  [1, 2, 3, 4, 5]

my_list = [3, 4, 2, 5, 1]
my_list.remove(4)
print(my_list) # [3, 2, 5, 1]


##Insert an element at specific index in a list and return updated list
a = [1, 2, 4]
a.insert(2, 3) # insert 3 in index 2
b = a[:]
print(b) # [1, 2, 3, 4]

### or
a = [1, 2, 4]
b = a[:2] + [3] + a[2:]
print(b) # [1, 2, 3, 4]

''' This note has taken from this side : https://www.programiz.com/python-programming/list

append() - Add an element to the end of the list
extend() - Add all elements of a list to the another list
insert() - Insert an item at the defined index
remove() - Removes an item from the list
pop() - Removes and returns an element at the given index
clear() - Removes all items from the list
index() - Returns the index of the first matched item
count() - Returns the count of number of items passed as an argument
sort() - Sort items in a list in ascending order
reverse() - Reverse the order of items in the list
copy() - Returns a shallow copy of the list

'''

list_arr = [1, 7, 4, 5, 9, 6]
list_arr.extend([33, 777])
print(list_arr)


list_arr = [1, 7, 4, 5, 9, 6]
list_arr.pop()
print(list_arr) # [1, 7, 4, 5, 9]
list_arr.pop(1)
print(list_arr) # [1, 4, 5, 9]

list_arr = [1, 7, 4, 5, 9, 6]
list_arr.clear()
print(list_arr) # []


list_arr = [1, 7, 4, 5, 9, 6]
idx = list_arr.index(9)
print(idx) # 4


list_arr = [1,1,1,2,3,2,5]
print(list_arr.count(1)) # 3


list_arr = [1, 7, 4, 5, 9, 6]
copy_list_arr = list_arr.copy()
print(copy_list_arr) # [1, 7, 4, 5, 9, 6]


## Find largest number from the list
list_arr = [1,3,4,8,9,77]
largest = max(list_arr)
print(largest) # 77


## Find small number from the list
list_arr = [1,3,4,8,9,77]
small = min(list_arr)
print(small) # 1


# delete entire list
#del my_list

# NameError: name 'my_list' is not defined
#print(my_list)


########################### String ###############################
'''
H   e   l   l   o
0   1   2   3   4
-5  -4  -3  -2  -1

'''

# all of the following are equivalent
my_string = 'Hello'
print(my_string)

my_string = "Hello"
print(my_string)

my_string = '''Hello'''
print(my_string)

# triple quotes string can extend multiple lines
my_string = """Hello, welcome to
           the world of Python"""
print(my_string)

'''
### Output : 
Hello
Hello
Hello
Hello, welcome to
           the world of Python
'''


my_string = "Hello"
print(my_string[0]) # H

my_string = "Hello "
my_string1 = "World!"
string = my_string + my_string1
print(string) # Hello World!


my_string = "I Love You"
if 'I' in my_string:
    print("Ok") # Ok
else:
    print("Not Ok!")

my_string = "I Love You"
if 'Love' in my_string:
    print("Ok")  # Ok
else:
    print("Not Ok!")


# Length of a string
my_string = "Rezwan"
print(len(my_string)) # 6


print('{0}, {1}, {2}'.format("Rezwanul", "Haque", "Rezwan")) # Rezwanul, Haque, Rezwan

print('{}, {}, {}'.format("Rezwanul", "Haque", "Rezwan")) # Rezwanul, Haque, Rezwan

my_string = "I Love You"
STr = my_string.replace("Love","Hate")
print(STr) # I Hate You

### Does Python have a string 'contains' substring method? (https://stackoverflow.com/questions/3437059/does-python-have-a-string-contains-substring-method)
s = "This be a string"
if s.find("is") == -1:
    print( "No 'is' here!")
else:
    print("Found 'is' in the string.") # Found 'is' in the string.


'''Important Link:
(1) Is there a way to substring a string in Python? [ https://stackoverflow.com/questions/663171/is-there-a-way-to-substring-a-string-in-python ]
(2) Generator Expressions vs. List Comprehension [ https://stackoverflow.com/questions/47789/generator-expressions-vs-list-comprehension ]

'''


'''
** You are now able to solve following online-judge problems.
------------------------------------------------------------
(1) CodeForces | A. Straight «A»
(2) Timus | 1000. A+B Problem
(3) URI | 1026 - To Carry or not to Carry 
(4) HackerRank | String Split and Join
(5) Spoj | ADDREV - Adding Reversed Numbers
(6) CodeChef | Devu and an Array 
(7) HackerRank | Find a string
(8) UVa | 11799 - Horror Dash
(9) UVa | 10370 - Above Average
(10) AtCoder | D - Walk and Teleport
'''