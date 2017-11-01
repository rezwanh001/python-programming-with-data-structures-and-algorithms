
'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

'''
Created on Aug 9, 2016

@author: Md. Rezwanul Haque
'''
def Fact(n):
    if n == 0 or n == 0: return 1
    return n*Fact(n-1)

while True:
    try:
        a, b = map(int, input().split())
        S = Fact(a) + Fact(b)
        print(S)
    except EOFError:
            break