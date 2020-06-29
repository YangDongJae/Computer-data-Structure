class Node:
  def __init__(self,data):
    self.data = data
    self.neighbors = []
    self.weight = []
    self.visited = None
    self.prev = None
    self.next = None

  def get_data(self):
    return self.data

  def get_next(self):
      return self.next
  
  def set_next(self,next):
      self.next = next      

  def add_neighbor(self, neighbor):
    self.neighbors.append(neighbor)

  def set_visited(self, visited):
    self.visited = visited

  def get_neighbors(self):
    return self.neighbors

  def get_visited(self):
    return self.visited


  def set_weight(self,weight,node_x , node_y):
    self.weight.append([node_x.get_data() , node_y.get_data() , weight])
      
  def get_weight(self, node):
    #return weigth 
    for i in range (len(self.weight)):
      weight = self.weight[i]
      for __ in range (len(weight)):
        if weight[1] == str(node):
          return self.weight[i][2]

  def get_all_weight(self):
    #return al weigths
    neighbors = self.get_neighbors()
    info_node = []
    for i in range(len(neighbors)):
      info_node.append([neighbors[i].get_data(), self.get_weight(neighbors[i].get_data())])
    return info_node          

  def get_all_visited(self):
    neighbors_visited = []
    for i in range (len(self.neighbors)):
      neighbors_visited.append(self.neighbors[i].get_visited())
    return neighbors_visited

  def get_neighbors_visited(self):
    neighbors_visited = []
    for neighbor in self.neighbors:
      neighbors_visited.append([neighbor.get_data(),neighbor.get_all_visited()])
    return neighbors_visited

  def set_neighbors(self,neigbors):
    self.neighbors = neigbors

class Weight_Graph:
  def __init__(self):
    self.nodes = []
    self.weights = []

  def get_object_reference(self,target):
    for i in range (len(self.nodes)):
      if target == self.nodes[i].get_data():
       result = self.nodes[i]
    return result    

  def add_node(self, node):
    self.nodes.append(node)

  def get_nodes(self):
    return self.nodes

  def set_weights(self):
    for node in self.nodes:
      self.weights.append({node.get_data(): node.get_all_weight()})
    return self.weights

  def reset_visit(self):
    if len(self.nodes) > 0:
      for node in self.nodes:
        node.set_visited(False)
    
  def compare_weight(self,target_node):
    #return small weigth in neigbors node weights
    neighbors_weight = target_node.get_all_weight()
    if len(neighbors_weight) != 1:
      while len(neighbors_weight) == 1:
        if len(neighbors_weight) == 1:
          return neighbors_weight
        else:
          if neighbors_weight[0][1] > neighbors_weight[1][1]:
            neighbors_weight.remove(neighbors_weight[0])
          else:
              neighbors_weight.remove(neighbors_weight[1])
        return neighbors_weight

#!!! have to trouble shooting for use compare weigth node B#

  def check_cycle(self,node):
    #if neighbors have True Visited(Cycle), return False
    handler = node.get_neighbors_visited()
    for i in range (len(handler) - 1):
      if  True in handler[i][1]:
        return False

  def prim(self,start_node):
    self.reset_visit()
    sll = singly_linked_list()
    sll.append(start_node.get_data())
    node_neighbors = start_node.get_neighbors()

    if self.check_cycle(start_node) == False:
      start_node.set_neighbors(self.get_object_reference(node_neighbors.remove(start_node.compare_weight())))
      self.prim(start_node)

    else:
      sll.append(self.get_object_reference(self.compare_weight(start_node)[0][0]).get_data())
      return sll.print_list()

      



        
    

      


class singly_linked_list:
  
  def __init__(self):
    self.header = None
    self.tail = None
    self.size = 0
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
    prev = self.header
    next_data = None
    node = self.header
    if index + 1 > self.size:
        print("index error")
    elif index == 0:
        self.header = node.get_next()
        self.size -= 1
    else:
        for i in range (index - 1):
            node = node.get_next()
            prev = node
        node = self.header
        for i in range (index + 1):
            node = node.get_next()
            next_data = node
        prev.set_next(next_data)
        
        node = self.header
        while node.get_next() != None:
            node = self.header.get_next()
        self.tail = node
        




    



  
graph = Weight_Graph()
minimum_list = singly_linked_list()


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

graph.prim(node_B)
graph.reset_visit()
print(graph.check_cycle(node_B))
print(graph.compare_weight(node_C))