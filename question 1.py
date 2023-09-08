# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 15:03:45 2023

@author: LAB
"""

n = int(input('enter a number between 1 to 20: '))
i = 1
j = 1
while j<=n:
    i=1
    while i<=20:
        print(j,'x',i,'=',j*i )
        i+=1
        if i==21:
            break
        
    j+=1