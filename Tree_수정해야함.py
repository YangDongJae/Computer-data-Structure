class Node:
    def __init__(self,data):
        self.leftChild = None
        self.rightChild = None
        self.nodeData = data
    
    def get_nodeData(self):
        return self.nodeData
    
    def set_nodeData(self,nodeData):
        self.nodeData = nodeData
        
    def get_leftChild(self):
        return self.leftChild
    
    def get_rightChild(self):
        return self.rightChild
    
    def set_leftchild(self,leftchildData):
        self.leftchild = leftchildData
        
    def set_rigthchild(self,rightChildData):
        self.rightchild = rightChildData
            
        
class Tree:
    def __init__(self):
        self.root = None
        self.size = 0
        self.fixData = None
        self.loopCount = None
        self.root_node = None
        
    def set_root(self,rootNode):
        self.root = rootNode
        
    def get_root(self):
        return self.root
    
    def input_Child(self,classifier,node_data):
        
        while classifier != 0:
            child_classifier = input("the Data location is left? or Right? [l/r]")
            
            if child_classifier == "l":
                input_node = input("what is data for it?")
                node_data.set_leftchild(input_node)
                classifier -= 1
                
                
            elif child_classifier == "r":
                input_node = input("whatis data for it?")
                node_data.set_rightchild(input_node)
                classifier -= 1

       
class Main:
    
    node = Node()
    
    def make_tree():
        tree  = Tree()
        
        root_node_data = input("what is root node Data?")
        
        tree.set_root(root_node_data)
        
        child_classifier = eval(input("how many have the node of child nodes?"))
        
        tree.input_Child(child_classifier,tree.get_nodeData)
        
        
        
        
        
        
        