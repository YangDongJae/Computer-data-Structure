'''
Created on 2020. 4. 4.

@author: yangdongjae
'''
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
    def get_data(self):
        return self.data
    
    def get_next(self):
        return self.next
    
    def set_next(self,next):
        self.next = next
    


        
        
    
class singly_linked_list:
    
    def __init__(self):
        self.header = None
        self.tail = None
        self.size = 0
        self.prev = None
        self.nextData = None

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
        prevNode = self.prev
        node = self.header
        if node == None:
            print("we can't find the data")
            
        elif index == 0:
            if self.tail.get_next() == None:
                node = None
                
            elif self.size == 1:
                node = None
                self.size -= 1
                
            else:
                node = node.set_next(node.get_next())
                self.size -= 1
            
            
        else:
            for i in range (0,index):
                if i == index - 1:
                    prevNode = node
                elif i == self.size -1:
                    break
                node = node.get_next()
                i += 1
            node = node.get_next()
            prevNode.set_next(node)
            self.size -= 1
            
                
                
            
    
                    
                
                
                
            
            
            
        
        
            
            
        
        
sll = singly_linked_list()

sll.append("chicken")
sll.append("coffee")
sll.append("USA")
sll.print_list()

print("-----------")
sll.delete_at(0)
sll.print_list()
print("-----------")
sll.append("airpods")
sll.print_list()
print("-----------")

node = sll.get_at(1)
if node != None:
    print(node.get_data())
else:
    print("index error")
print("-----------")    
node = sll.get_at(2)
if node != None:
    print(node.get_data())
else:
    print("index error")
    
print("-----------")
    
node = sll.search("USA")
if node != None:
    print("we have it!")
else:
    print("We don't have it!")
    
    
    

            
                
            
        
    