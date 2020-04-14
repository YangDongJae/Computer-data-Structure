#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 20:06:58 2020

@author: yangdongjae
"""


class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None
    
    def set_prev(self,prev):
        self.prev = prev
        
    def set_next(self, next):
        self.next = next
        
    def get_data(self):
        return self.data
    
    def get_prev(self):
        return self.data
    
    def get_next(self):
        return self.next
        
        
class Doubly_linked_list:
    def __init__(self):
        self.header = None
        self.tail = None
        self.size = 0
        
    def print_list(self):
        header = self.header
        print(">>>Current List")
        while header == None:
            print(header.get_data())
            header = header.get_next()
        print(">>>>>>>>>>>>>>>>")
        
    def append(self,data):
        new_node = Node(data)
        self.size += 1
        if self.header == None:
            self.header = new_node
        else:
            self.tail.set_next(new_node)
            new_node.set_prev(self.tail)
        self.tail = new_node

    def append(self,data):
        self.size += 1
        new_node = Node(data)
        if self.header == None:
            self.header = new_node
        else:
            self.tail.set_next(new_node)
        self.tail = new_node        
        
    def get_at(self,index):
        header = self.header
        for i in range (index):
            header = header.get_next()
        return header.get_next()
    
    def search(self,data):
        self.header = header
        for i in range (size - 1):
            header = self.get_next()
        return header

dll = Doubly_linked_list()
dll.append("Apple")
dll.append("Kiwi")
dll.append("Banana")         
dll.print_list()   
            
        
        
            
            
        
    
            
             
        
        