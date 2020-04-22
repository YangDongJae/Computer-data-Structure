#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 11:31:45 2020

@author: yangdongjae
"""


class Node:
    def __init__(self,data):
        self.data = data
        self.left_child = None
        self.right_child = None
        
    def get_left_child(self):
        return self.left_child
    
    def get_right_child(self):
        return self.right_child
    
    def get_data(self):
        return self.data
    
    def set_left_child(self, left_child):
        self.set_left_child = left_child
        
    def set_right_child(self, right_child):
        self.set_right_child = right_child
        
class Binary_tree:
    def __init__ (self):
        self.root = None
        
    def get_root(self):
        return self.root
    
    def set_root(self, root):
        self.root = root
        
    def pre_order(self, node):
        if node != None:
            print(node.get_data(), end = " ")
            self.pre_order(node.get_left_child())
            self.pre_order(node.get_right_child())
            
            
b_tree = Binary_tree()

node_a = Node("A")
node_b = Node("B")
node_c = Node("C")
node_d = Node("D")
node_e = Node("E")
node_f = Node("F")
node_g = Node("G")
node_h = Node("H")

b_tree.set_root(node_a)

node_a.set_left_child(node_b)
node_a.set_right_child(node_c)

node_b.set_left_child(node_d)
node_b.set_right_child(node_e)

node_c.set_right_child(node_f)

node_d.set_right_child(node_g)

node_e.set_left_child(node_h)

b_tree.pre_order(b_tree.get_root())