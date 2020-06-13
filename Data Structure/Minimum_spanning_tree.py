class Node:
  def __init__(self,data):
    self.data = data
    self.neighbors = []
    self.weight = []
    self.visited = None

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
    self.weight.append([node_x.get_data() , node_y.get_data() , weight])
      
  def get_weight(self, node):
    for i in range (len(self.weight)):
      weight = self.weight[i]
      for __ in range (len(weight)):
        if weight[1] == str(node):
          return self.weight[i][2]

  def get_all_weight(self):
    neighbors = self.get_neighbors()
    info_node = []
    for i in range(len(neighbors)):
      info_node.append([neighbors[i].get_data(), self.get_weight(neighbors[i].get_data())])
    return info_node             

  def compare_weight(self,point_node):
  #return small weight
    weight_list = []
    graph.reset_visit()
    for node in graph.nodes:
      if point_node == node :
        neighbors = node.get_neighbors()
        for neighbor in neighbors:
          weight = neighbor.get_data() , point_node.get_weight(neighbor.get_data())
          weight_list.append(weight)
        weight_list.sort()
        return(weight_list[0])


  


      


class Weight_Graph:
  def __init__(self):
    self.nodes = []
    self.weights = []

  def add_node(self, node):
    self.nodes.append(node)

  def set_weights(self):
    for node in self.nodes:
      self.weights.append({node.get_data(): node.get_all_weight()})
    return self.weights

  def reset_visit(self):
    if len(self.nodes) > 0:
      for i in range (len(self.nodes)):
        self.nodes[i].set_visited = False








    



  
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

print(graph.set_weights())