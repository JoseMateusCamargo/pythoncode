#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# creating own exceptions

class error(Exception):
    def __init__(self, n):
        self.num = n
        
    def __str__(self):
        return 'Error, you repeated that number: %i' %(self.num)

def main():
    list = []
    for i in range(3):
        while True:
            try:
                num = int(input('tell me a beautiful number: '))
                break
            except ValueError:
                print('only numbers, plz: ')
        if num not in list:
            list.append(num)
        else:
            raise error(num)

main()