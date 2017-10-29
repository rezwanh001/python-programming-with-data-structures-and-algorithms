a = input() # take a string (with-space, without-space)
# hello world
print(a) # hello world


a = int(input()) # take only one int number
# 5
print(a) # 5

a = float(input()) # take only one float number
print(a)

a = str(input()) # take only one str
print(a)

a, b = map(int, input().split()) # take two numbers with only one space. like : 2 3
print(a, b) # 2 3

a, b, c = map(int, input().split()) # take three numbers with only one space # 2 3 4
print(a, b, c) # 2 3 4

# input a list
arr = list(map(int, input().split())) # int type array
print(arr) # [1, 2, 3, 4, 5]
print(*arr) # 1 2 3 4 5

a = int(input("Enter a Integer number: "))
print("Entered number is %d" % a)
'''
Enter a Integer number: 233
Entered number is 233
'''

a = float(input("Enter a Float number: "))
print("Entered number is %f" % a)
'''
Enter a Float number: 233.5
Entered number is 233.5
'''
