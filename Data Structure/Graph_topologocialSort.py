class Node:
  def __init__(self, data):
    self.data = data
    self.neighbors = []
    self.visited = False
    
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


class Graph:
  def __init__(self):
    self.nodes = []
    
  def add_node(self, node):
    self.nodes.append(node)

  def tps(self):
    if len(self.nodes) > 0:
      for node in self.nodes:
        node.set_visited(False)
        # reset 'visited' attribute 
    Graph.topological_sort(self,node_A)
    

  def topological_sort(self, point_node):
    stack = []
    neighbor_list = point_node.get_neighbors()

    if len(neighbor_list) > 0:
      for i in range (len(neighbor_list)):
        point_node.set_visited(True)
        self.topological_sort(neighbor_list[i])
        stack.append(point_node)
        
        # if point_node.get_visited == True:
        #   for i in range (len(self.nodes)):
        #     if self.nodes[i].get_data == False:
        #       point_node = self.nodes[i]
        #       self.topological_sort(point_node)

    else:
      point_node.set_visited(True)
      stack.append(point_node)

    for i in range(len(stack)):
      stack_node = stack[i]
      print(stack_node.get_data())
      




    

  def print_self(self):
    for i in range (len(self.nodes)):
      node = self.nodes[i]
      print(node.get_data())
      
      

    


        
      
     
graph = Graph()

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
node_J = Node('J')
graph.add_node(node_J)

node_A.add_neighbor(node_B)
node_A.add_neighbor(node_F)

node_B.add_neighbor(node_H)

node_D.add_neighbor(node_C)
node_D.add_neighbor(node_E)
node_D.add_neighbor(node_I)

node_E.add_neighbor(node_I)

node_G.add_neighbor(node_A)
node_G.add_neighbor(node_B)
node_G.add_neighbor(node_C)

node_I.add_neighbor(node_C)

node_J.add_neighbor(node_E)

graph.tps()