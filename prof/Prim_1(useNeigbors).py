import sys

class Node:

  index = 0

  def __init__(self, data): 
    self.index = Node.index
    Node.index += 1
    self.data = data

    self.key = sys.maxsize
    self.memo = None
    self.is_done = False

  def get_index(self):
    return self.index

  def get_data(self):
    return self.data

  def get_key(self):
    return self.key
  
  def get_memo(self):
    return self.memo

  def get_is_done(self):
    return self.is_done

  def set_key(self, key, memo):
    if(self.key > key):
      self.key = key
      self.memo = memo

  def set_is_done(self):
    self.is_done = True

class Graph:

  def __init__(self, nodes, matrix):
    self.nodes = nodes
    self.matrix = matrix

  def execute_prim(self):

    node = nodes[0]
    node.set_key(0, None)
    
    done_count = 0
    while done_count < len(self.nodes):
      node = self.get_min_node()
      node.set_is_done()
      done_count += 1
      self.update(node)

    self.print_result()

  def update(self, node):
    neighbors = self.matrix([node.get_index()])
    node_index = node.get_index()
    for neighbor in neighbors:
      if not neighbor.get_is_done():
        neighbor_index = neighbor.get_index()
        neighbor.set_key(matrix[node_index][neighbor_index], node)

  def get_min_node(self):
    min_node = None
    for node in nodes:
      if not node.get_is_done():
        if min_node is None:
          min_node = node
        else:
          if min_node.get_key() > node.get_key():
            min_node = node
    return min_node

  def print_result(self):
    for node in self.nodes:
      if node.get_memo() is not None:
        print( node.get_data() + ' - ' + node.get_memo().get_data() + 
              ' (' + str(node.get_key()) + ')')

# create an array whose elements are alphabets from 'A' to 'I' using ascii code
dataset = []
for i in range(65, 74):
  dataset.append(chr(i))

# create nodes
nodes = []
for data in dataset:
  nodes.append(Node(data))

# create matrix for weights
matrix = [[0, 4, 0, 0, 0, 0, 0, 8, 0], # w.r.t node A
          [4, 0, 8, 0, 0, 0, 0, 11, 0], # w.r.t node B
          [0, 8, 0, 7, 0, 4, 0, 0, 2], # w.r.t node C
          [0, 0, 7, 0, 9, 14, 0, 0, 0], # w.r.t node D
          [0, 0, 0, 9, 0, 10, 0, 0, 0], # w.r.t node E
          [0, 0, 4, 14, 10, 0, 2, 0, 0], # w.r.t node F
          [0, 0, 0, 0, 0, 2, 0, 1, 6], # w.r.t node G
          [8, 11, 0, 0, 0, 0, 1, 0, 7], # w.r.t node H
          [0, 0, 2, 0, 0, 0, 6, 7, 0]] # w.r.t node I


# create a graph
graph = Graph(nodes, matrix)

# execute prim algorithm
graph.execute_prim()