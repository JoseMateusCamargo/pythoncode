#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Mon Dec 23 00:12:22 2019
@author: JMC
Checks if the string is palindrome
"""

f=input('tell me a beautiful string:  ')

if f==f[::-1]:
    print('Wow this string is is palindrome --> %s'%(f))
else:
    print('No, this string is not a palindrome --> %s'%(f))
