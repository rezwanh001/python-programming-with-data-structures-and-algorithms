######### take a string (with-space, without-space)
a = input()
print(a)
'''
Input:
Hello World!

Output:
Hello World!
'''



######### take only one int number
a = int(input())
print(a)
'''
Input:
5

Output:
5
'''



######### take only one float number
a = float(input())
print(a)
'''
Input:
5.6

Output:
5.6
'''

##### take only one str
a = str(input())
print(a)
'''
Input:
Rezwan

Output:
Rezwan
'''




###### take two numbers with only one space. like : 2 3
a, b = map(int, input().split())
print(a, b)
'''
Input:
2 3

Output:
2 3
'''




######### take three numbers with only one space
a, b, c = map(int, input().split())
print(a, b, c)
'''
Input:
2 3 4

Output:
2 3 4
'''



############### input a list
arr = list(map(int, input().split())) # int type array
print(arr)
print(*arr)
'''
Input:
1 2 3 4 5 

Output:
[1, 2, 3, 4, 5]
1 2 3 4 5

'''

#########################

a = int(input("Enter a Integer number: "))
print("Entered number is %d" % a)
'''
Enter a Integer number: 233
Entered number is 233
'''

##########################

a = float(input("Enter a Float number: "))
print("Entered number is %f" % a)
'''
Enter a Float number: 233.5
Entered number is 233.5
'''

