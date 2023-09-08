# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 15:19:35 2023

@author: LAB
"""

n = int(input('enter a number n :'))
i = 1
while i<=n:
    j = 1
    while j<=i:
        print('*', end=' ')
        j+=1
    print()
    i+=1