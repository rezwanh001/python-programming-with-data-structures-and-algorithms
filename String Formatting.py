######## String length, uppercase, lowercase
a = input("Enter a string with uppercase and lowercase: ")
print(a.upper())
print(a.lower())
print(len(a))
'''
Input:
Hello World!

Output:
HELLO WORLD!
hello world!
12
'''

##### Separate string with a character
print("Welcome", "to", "python", "programming", sep="*")
'''
Output:
Welcome*to*python*programming
'''

################################
name = input()
age = int(input())
print(name, "is" , age, "years old!")
print('%s is %d years old!' %(name, age))
'''
Input:
Rezwan
20

Output:
Rezwan is 20 years old!
Rezwan is 20 years old!
'''

##################################
a = float(input())
print("Price of this t-shirt is %.9f" % a)
'''
Input:
855.75

Output:
Price of this t-shirt is 855.750000000
'''
