class Node:
    def __init__(self,data):
        self.data = data
        self.child = []

    def get_data(self):
        return self.data
    
    def get_child(self):
        return self.child

    def set_child(self,data):
        self.child.append(data)

class Tree:
    def __init__(self):
        self.root = None
    
    def get_root(self):
        return self.root

    def set_root(self,root_data):
        self.root = root_data

    def print_node(self, node, depth):
        msg = ""
        if node is not None:
            for i in range(0, depth):
                msg += "  "
            msg += node.get_data()
            print(msg)
        
        children = node.get_child()
        for i in range(0, len(children)):
            self.print_node(children[i], depth + 1)
            
tree = Tree()

node_a = Node("A")
node_b = Node("B")
node_c = Node("C")
node_d = Node("D")
node_e = Node("E")
node_f = Node("F")
node_g = Node("G")

node_a.set_child(node_b)
node_a.set_child(node_c)

node_c.set_child(node_d)
node_c.set_child(node_e)
node_c.set_child(node_f)

node_b.set_child(node_g)

tree.print_node(node_a , 1)