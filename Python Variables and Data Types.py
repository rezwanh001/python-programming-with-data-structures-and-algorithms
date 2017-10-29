# variable assignment
x = 7
y = 2.3
z = 'hello'
print(x, y, z) # 7 2.3 hello

print(type(x)) # <class 'int'>
print(type(y)) # <class 'float'>
print(type(z)) # <class 'str'>


# multiple assignment
x, y, z = 1, 2.3, 'hello'
print(x, y, z) # 1 2.3 hello

# python number
a = 5
print(a, "is of type", type(a))

a = 2.0
print(a, "is of type", type(a))

a = 2e22
print(a, "is of type", type(a)) # 2e+22 is of type <class 'float'>

a = 1+2j
print(a, "is complex number?", isinstance(1+2j, complex)) # (1+2j) is complex number? True

a = complex(2, 3)
print(a) # (2+3j)

a = True
print(a) # True
print(int(a)) # 1

a = False
print(a) # False
print(int(a)) # 0

###  Built-in Atomic Data Types
print(2 + 3 * 4) # 14
print((2 + 3) * 4)  # 20
print(2**3) # 8 ( ** works as exponential )
print(6/2) # 3.0 ( type float )
print(6//2) # 3 (type int)
print(6%2) # 0
print(7%3) # 1
print(2**100) # 1267650600228229401496703205376 (python can store big integer by default)

a = 2
b = 3
print(a+b) # 5

a = "Hello"
b = "World"
print(a + b)# HelloWorld
print(5*a) # HelloHelloHelloHelloHello


print(5==10) # False
print(10 > 5) # True
print((5 >= 1) and (5 <= 10)) # True

