for i in range(10):
    print(i,end=' ')
print()
'''
Output:
0 1 2 3 4 5 6 7 8 9 
'''

for i in range(10, 0, -1):
    print(i, end=' ')
print()
'''
Output:
10 9 8 7 6 5 4 3 2 1 
'''

for i in reversed(range(10)):
    print(i, end=' ')
print()
'''
Output:
9 8 7 6 5 4 3 2 1 0 
'''

i = 10
while i != 0:
    print(i, end=' ')
    i -= 1
print()
'''
Output:
10 9 8 7 6 5 4 3 2 1 
'''


# 1 + 2 + 3 + ....... + n
### for loop
n = int(input())
sm = 0
for i in range(1, n + 1):
    sm += i

print(sm)
'''
Input:
100

Output:
5050
'''

### while loop
n = int(input())
i = 0
sm = 0
while i <= n:
    sm += i
    i += 1
print(sm)


# Counts how many 2 divides 100
x = 100
cnt = 0
while x%2 == 0:
    x = x//2
    cnt += 1
print(cnt)
'''
Output:
2 
'''

#### Finds out the highest number which is power of 2 and less than 1000
x = 1
# if multiplying by 2 does not exceed 1000, multiply
while x*2 < 1000:
    x *= 2
print(x)


#### prints odd numbers 1 to 10
for i in range(1, 10 + 1):
    if i % 2 == 0: continue
    print(i, end= ' ')
print()

### Print only 1,2,3
for i in range(1, 11):
    if i > 3:
        break
    print(i, end=' ')
print()



##### 1 + (1+2) + (1+2+3) + .... + (1+2+3+..+n)
n = int(input())
sm = 0
for i in range(1, n+1):
    for j in range(1, i):
        sm += j
print(sm)


### Simple function for problem solving

def Main():  # user define function
    n = int(input())
    # now we will calculate the factorial of a number
    fact = 1
    for i in range(1, n + 1):
        fact *= i

    print(fact)


if __name__ == '__main__':  # python3 'main' function
    Main()  # call the user define function 'Main()'

###########

### EOF

while True:
    try:
        a = input()
        print(a)
    except EOFError:
        break





'''
** You are now able to solve following online-judge problems.
------------------------------------------------------------
(1) URI Online Judge | 1103 Alarm Clock
(2) Timus | 1083. Factorials!!!
(3) Timus | 1209. 1, 10, 100, 1000...
(4) URI Online Judge | 1161 Factorial Sum
(5) URI Online Judge | 1059 Even Numbers
(6) HackerRank | Loops
(7) Spoj | TEST - Life, the Universe, and Everything
(8) CodeChef | Life, the Universe, and Everything 
(9) CodeChef | N different palindromes
(10) UVa | 10055 Hashmat the Brave Warrior
'''