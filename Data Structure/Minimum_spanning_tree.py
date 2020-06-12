class Node:
  def __init__(self,data):
    self.data = data
    self.neighbors = []
    self.weight = {}

  def add_neighbor(self, neighbor):
    self.neighbors.append(neighbor)

  def set_visited(self, visited):
    self.visited = visited

  def get_data(self):
    return self.data

  def get_neighbors(self):
    return self.neighbors

  def get_visited(self):
    return self.visited

  def set_weight(self,weight,node_x , node_y):
    self.weight = {node_x.get_data() : [node_y.get_data() , weight]}

  def get_weight(self):
    return self.weight
    
class Weight_Graph:
  def __init__(self):
    self.nodes = []

  def add_node(self, node):
    self.nodes.append(node)

  
graph = Weight_Graph()


node_A = Node('A')
graph.add_node(node_A)
node_B = Node('B')
graph.add_node(node_B)
node_C = Node('C')
graph.add_node(node_C)
node_D = Node('D')
graph.add_node(node_D)
node_E = Node('E')
graph.add_node(node_E)
node_F = Node('F')
graph.add_node(node_F)
node_G = Node('G')
graph.add_node(node_G)
node_H = Node('H')
graph.add_node(node_H)
node_I = Node('I')
graph.add_node(node_I)


node_A.add_neighbor(node_B)
node_A.set_weight(4, node_A , node_B)
node_A.add_neighbor(node_H)
node_A.set_weight(8, node_A , node_H)

node_B.add_neighbor(node_A)
node_B.set_weight(4, node_B , node_A)
node_B.add_neighbor(node_H)
node_B.set_weight(11, node_B , node_H)
node_B.add_neighbor(node_C)
node_B.set_weight(8, node_B , node_C)

node_C.add_neighbor(node_B)
node_C.set_weight(8 , node_C , node_B)
node_C.add_neighbor(node_I)
node_C.set_weight(2 , node_C , node_I)
node_C.add_neighbor(node_F)
node_C.set_weight(4 , node_C , node_F)
node_C.add_neighbor(node_D)
node_C.set_weight(7 , node_C , node_D)

node_D.add_neighbor(node_C)
node_D.set_weight(7,node_D,node_C)
node_D.add_neighbor(node_F)
node_D.set_weight(14,node_D,node_F)
node_D.add_neighbor(node_E)
node_D.set_weight(9,node_D,node_E)

node_E.add_neighbor(node_D)
node_E.set_weight(9,node_E,node_D)
node_E.add_neighbor(node_F)
node_E.set_weight(10,node_E,node_F)

node_F.add_neighbor(node_E)
node_F.set_weight(10,node_F,node_E)
node_F.add_neighbor(node_D)
node_F.set_weight(14,node_F,node_D)
node_F.add_neighbor(node_C)
node_F.set_weight(4,node_F,node_C)

node_G.add_neighbor(node_H)
node_G.set_weight(1,node_G,node_H)
node_G.add_neighbor(node_I)
node_G.set_weight(6,node_G,node_I)
node_G.add_neighbor(node_F)
node_G.set_weight(2,node_G,node_F)

node_H.add_neighbor(node_A)
node_H.set_weight(8,node_H,node_A)
node_H.add_neighbor(node_B)
node_H.set_weight(11,node_H,node_B)
node_H.add_neighbor(node_I)
node_H.set_weight(7,node_H,node_I)
node_H.add_neighbor(node_G)
node_H.set_weight(1,node_H,node_G)

node_I.add_neighbor(node_C)
node_I.set_weight(2,node_I,node_C)
node_I.add_neighbor(node_H)
node_I.set_weight(7,node_I,node_H)
node_I.add_neighbor(node_G)
node_I.set_weight(6,node_I,node_G)



