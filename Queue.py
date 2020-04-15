
class Node:
    def __init__ (self,data):
        self.data = data
        self.prev = None
        
    def get_data(self):
        return self.data
    
    def set_prev(self, prev):
        self.prev = prev
    
    def get_prev(self):
        return self.prev
    
class Queue:
    def __init__ (self):
        self.front = None
        self.rear = None
        self.size = 0
        
    def enqueue(self,data):
        new_node = Node(data)
        self.size += 1
        if self.front == None:
            self.front = new_node
        else:
            self.rear.set_prev(new_node)
        self.rear = new_node

    def dequeue(self):
        front_node = self.front
        if front_node == None:
            return front_node
        elif self.size == 1:
            self.size -= 1
            self.rear = None
            front_node = None
            return front_node
        else:

            self.size -= 1
            self.front = front_node.get_prev()
            return front_node
            
            
            
            
            
            
        

    def print_queue(self):
        node = self.front
        print(">> current queue")
        while self.front != None:
            print(node.get_data())
            node = node.get_prev()
            if node == None:
                break
        print(">>>>>>>>>>>>>>>>")
    
    
queue = Queue()
queue.enqueue("Apple")
queue.enqueue("Kiwi")
queue.enqueue("Banana")
queue.print_queue()

node = queue.dequeue()
print("Dequeue:" + node.get_data())
node = queue.dequeue()
print("Dequeue:" + node.get_data())

queue.enqueue("Melon")

queue.print_queue()

    
        
