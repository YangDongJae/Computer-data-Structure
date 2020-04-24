#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 10:47:33 2020

@author: yangdongjae
"""


L = []

L.append(5)
L.append(8)
L.append(10)
L.append(15)
L.append(20)
L.append(25)
L.append(30)
L.append(40)
L.append(50)
L.append(54)
L.append(66)
L.append(69)
L.append(83)
L.append(86)
L.append(90)

def find(L, target, start, end):
    if L[start + end // 2] < target:
        find(L,target,start + end // 2 +1, end)
    elif L[start + end // 2] > target:
        find(L,target,start,start + end // 2 -1)
    else:
        return L[start + end // 2]

index = find(L, 66, 0, len(L) - 1)
print(index)