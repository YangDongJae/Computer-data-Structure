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
        
    def set_next(self, nextData):
        self.next = nextData
        
    def get_data(self):
        return self.data
    
    def get_prev(self):
        return self.prev
    
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
        while header != None:
            print(header.get_data())
            header = header.get_next()
        print(">>>>>>>>>>>>>>>>")
        
    def append(self,data):
        new_node = Node(data)
        header = self.header
        self.size += 1
        if self.header == None:
            self.header = new_node
        else:
            self.tail.set_next(new_node)
            new_node.set_prev(self.tail)
        self.tail = new_node
         
    def get_at(self,index):
        header = self.header
        for i in range (index):
            header = header.get_next()
        return header.get_next()
    
    def search(self,data):
        node = self.header
        for i in range(self.size):
            if node.get_data() == data:
                return node
            node = self.header.get_next()
        return node
    
    def get_near_by(self,data,scope):
        list = [] 
        header= self.header
        prev = None
        nextData = None
        while header.get_data() != data:
            header = header.get_next()
            if header.get_data() == data:
                prev = header.get_prev()
                nextData = header.get_next()
                for i in range (scope):
                    if prev == None:
                        break
                    list.append(prev.get_data())
                    prev = prev.get_prev()
                for i in range(scope):
                    if nextData == None:
                        break
                    list.append(nextData.get_data())
                    nextData = nextData.get_next()
        return list

                
    

            
            
        

dll = Doubly_linked_list()
dll.append("Apple")
dll.append("Kiwi")
dll.append("Banana") 
dll.append("Melon")
dll.append("Oranged")
dll.append("Blackberry")   
list = dll.get_near_by("Banana" , 3)
print(list)

            
        
        
            
            
        
    
            
             
        
        