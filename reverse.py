# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 18:56:41 2020

@author: Admin
"""

num=int(input('enter the number:'))
print(num)
rev=0
while(num>0):
    rem=num%10
    rev=(rev*10)+rem
    num=num//10
print('reverse number is:',rev)