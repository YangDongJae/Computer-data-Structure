class Node:
    def __init__(self,data):
        self.data = data
        self.children = []
        self.count = 0

    def get_data(self):
        return self.data
    
    def get_children(self):
        return self.children

    def add_children(self,add_data):
        self.children.append(add_data)

class Tree:
    def __init__(self):
        self.root = None
        self.node = []
    
    def get_root(self):
        return self.root
    
    def set_root(self,root_data):
        self.root = root_data
    
    def make_node(self):
        node_data = input("what's the node data?")
        self.node.append(Node(node_data))

    def set_child(self,parent_data):
        self.set_root(self.node[0])
        
        #재귀함수로 구현 예정, 입력값으로 child 노드 받고, node 리스트에 있는지 점검.
        #리스트에 그 값이 있다면 인덱스 번호를 활용하여 add_child 해줌.
        #addchild한 값은 node 리스트에서 pop 해줌
        #이과정을 node 리스트의 길이가 1이 될때까지(root노드만 남을때 까지) 반복.
