'''
Created on May 16, 2016

@author: Md. Rezwanul Haque
'''
s = input()
tar = input()
score = 0
for i in range(len(s)):
    if s[i:i + len(tar)] == tar:
        score+=1
print(score)