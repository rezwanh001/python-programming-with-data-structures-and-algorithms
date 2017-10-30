##############
marks = 55
if marks >= 40:
    print('You are paseed!')
else:
    print('You are failed!')
'''
Output:
You are paseed!
'''


################
balance = int(input('Enter your balance: '))
if balance < 100 :
    print('You balance is bellow 100' )
elif balance == 100:
    print('You balance is equal 100' )
else:
    print('You balance is over 100' )

'''
Input:
Enter your balance: 175

Output:
You balance is over 100
'''

###### Find largest number among three number using nested if-else statement
a, b, c = map(int, input().split())
if a >= b:
    if a >= c:
        print('Largest number a is ', a)
    else:
        print('Largest number c is ', c)
else:
    if (b >= c):
        print('Largest number b is %d' %b)
    else:
        print('Largest number c is %d' %c)

##### Find largest number among three number simple if-else statement
a, b, c = map(int, input().split())
if a >= b and a >= c:
    print('Largest number a is ', a)
elif b >= c and b >= a:
    print('Largest number b is %d' % b)
else:
    print('Largest number c is ', c)

##### Find largest number among three number python build-in function "max()"
a, b, c = map(int, input().split())
mx = max(a, b, c)
print('Maximum number is ', mx)
'''
Input:
1 2 3

Output:
Maximum number is  3
'''

#### Student Grade system using conditional statements
mark = float(input('Enter your mark of a subject: '))
if mark >=80 and mark <= 100:
    print('A+')
elif 70 <= mark < 80:
    print('A')
elif 60 <= mark < 70:
    print('B')
elif 50 <= mark < 60:
    print('C')
else:
    print('Failed')

'''
Input:
Enter your mark of a subject: 58.75

Output:
C

'''

a = input('Enter your nationality : ')

if a.lower() == 'bangladeshi':  # all characters will be lower due to using 'a.lower()'
    print('Yeah! You are Bangladeshi')
else:
    print('Opps! You are Foreigner')

'''
Input:
Enter your nationality : BanGlaDeshi

Output:
Yeah! You are Bangladeshi
'''



########## Leaf Year
year = int(input())

if( year%400 == 0 or (year%100 != 0 and year%4 == 0) ):
    print('%d is leaf year.' % year)
else:
    print('%d is not leaf year.' % year)





'''
** You are now able to solve following online-judge problems.
------------------------------------------------------------
1. http://codeforces.com/problemset/problem/4/A 
    
2. http://abc070.contest.atcoder.jp/tasks/abc070_b

3. https://timus.spatarel.ro/problem.aspx%3Fspace=1&num=1068

'''