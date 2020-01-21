#!/usr/bin/env python3
""" Compara linhas de dois .csv e salva diferenca """

import sys
import argparse
import csv

with open('1.csv', 'r') as t1, open('2.csv', 'r') as t2:
    fileone = t1.readlines()
    filetwo = t2.readlines()

with open('update.csv', 'w') as outFile:
    for line in filetwo:
        if line not in fileone:
            outFile.write(line)

print("Finish")
            
