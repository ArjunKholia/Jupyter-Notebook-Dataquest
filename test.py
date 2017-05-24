# -*- coding: utf-8 -*-
"""
Created on Wed May 24 00:16:27 2017

@author: Arjun
"""

import csv
File = open("guns.csv",'r')
data = list(csv.reader(File))
for x in range(5):
    print(data[x])