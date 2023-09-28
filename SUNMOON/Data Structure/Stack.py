class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
    def get_data(self):
        return self.data
    
    def get_next(self):
        return self.next
    
    def set_next(self, next):
        self.next = next
        
class Stack:
    def __init__(self):
        self.size = 0
        self.top = None
        
    def push(self,data):
        new_node = Node(data)
        self.size += 1
        if self.top == None:
            self.top = new_node
        else:
            new_node.set_next(self.top)
            self.top = new_node
            
    
    def pop(self):
        topData = self.top
        if topData != None:
            self.top = topData.get_next()
            #topData = topData.get_next()
            self.size -= 1
        return topData
        
       # else:
        #    topData = topData.get_next()
        #    topData.set_next(topData.get_next())
            
    def get_at(self,index):
        topData = self.top
        if index == 0 :
            return topData
        elif index < self.size:
            for i in range(0,index):
                topData = topData.get_next()
            return topData
                
                
            
            
        
    def print_stack(self):
        print(">> current stack")
        node = self.top
        while node != None:
            print(node.get_data())
            node = node.get_next()
        print(">>>>>>>>>>>")

stack = Stack()
stack.push("Apple")
stack.push("Kiwi")
stack.push("Banana")
stack.print_stack()

node = stack.get_at(0)
if node != None:
    print(node.get_data())
else:
    print("index error")
print(">>>>>>>>>>>>")
while True:
    node = stack.pop()
    if node is None:
        break
    else:
        print("Pop : " + node.get_data())
        if node == None:
            break
stack.print_stack()