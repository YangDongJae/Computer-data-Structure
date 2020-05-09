#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  5 17:34:14 2020

@author: yangdongjae
"""


def main():
    index = eval(input("please add for fibonacci index"))
    print(index, "of fibonacci is ", fib(index), ".")
    
def fib(index):
    if index == 0:
        return 0
    
    elif index == 1:
        return 1
        
    else:
        return fib(index-1) + fib(index-2)

main()