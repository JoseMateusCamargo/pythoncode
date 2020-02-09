# -*- coding: utf-8 -*-
# working with list - basic

# Using while
lista = [1,2,3,4,5]
x = 0
num_elementos_lista = len(lista)
while(x < num_elementos_lista):
    print(lista[x])
    x+=1
    
# Using for
lista = [1,2,3,4,5]
for item in lista:
    print(item)
    
for item in [1,2,3,4,5]:
    print(item)
    
# Iterating lists 
#
# the code below does not work - just an example
#
# lista_nums = [100,200,300,400]
# for item in lista_nums:
#     item += 1000
# print(lista_nums)
#

# Iterating lists - using range
lista_nums = [100,200,300,400,500,600,700,800]
for item in range(len(lista_nums)):
    lista_nums[item] += 1000
print(lista_nums)

# Iterating lists - using enumerate
lista_nums = [100,200,300,400,500,600,700,800]
for idx, item in enumerate(lista_nums):
    lista_nums[idx] += 1000
print(lista_nums)