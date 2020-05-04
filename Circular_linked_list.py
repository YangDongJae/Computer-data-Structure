#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 15:01:35 2020

@author: yangdongjae
"""


class Node:
    def __init__(self, data):
        self.node = data
        self.next = None
        
    def get_node(self):
        return self.node
    
    def get_next(self):
        return self.next
    
    def set_next(self, nextData):
        self.next = nextData
        
class singly_linked_list:
    
    def __init__(self):
        self.header = None
        self.tail = None
        self.size = 0


    def append(self,data):
        self.size += 1
        new_node = Node(data)
        if self.header == None:
            self.header = new_node
        else:
            self.tail.set_next(new_node)
        self.tail = new_node
    
    def print_list(self):
        node = self.header
        while node != None:
            print(node.get_data())
            node = node.get_next()
        
    def get_at(self,index):
        if self.size <= index :
            return None
        else:
            header = self.header            
            for i in range(0,index):
                header = header.get_next()
            return header
        
    def search(self,data):
        node = self.header
        for i in range(self.size):
            if node.get_data() == data:
                return node
            node = self.header.get_next()
        return node
    
    def delete_at(self,index):
        prev = self.header
        next_data = None
        node = self.header
        if index + 1 > self.size:
            print("index error")
        elif index == 0:
            self.header = node.get_next()
            self.size -= 1
        else:
            for i in range (index - 1):
                node = node.get_next()
                prev = node
            node = self.header
            for i in range (index + 1):
                node = node.get_next()
                next_data = node
            prev.set_next(next_data)
            
            node = self.header
            while node.get_next() != None:
                node = self.header.get_next()
            self.tail = node
        
    