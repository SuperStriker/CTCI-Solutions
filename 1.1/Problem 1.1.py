# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 13:13:36 2018

@author: Anoop
"""

str= input("Enter a string:")

word = {}
unique= True
for i in str:
    if i in word.keys():
        unique = False
        break
    else:
        word[i]=1
if (unique == False):
    print('String in not unique')
else:
    print('String is Unique')

        

    
    