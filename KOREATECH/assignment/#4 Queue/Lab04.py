import time
import random 



class CircularQueue:
    def __init__(self, Max_QSIZE):
        self.MAX_QSIZE = Max_QSIZE
        self.front = 0
        self.rear = 0
        self.items = [None] * self.MAX_QSIZE

    def __len__(self):
        return (self.rear - self.front + self.MAX_QSIZE) % self.MAX_QSIZE

    def __str__(self):
        return str(self.items)

    def enqueue(self, item):
        if self.isFull():
            raise Exception("Queue is full")
        self.items[self.rear] = item
        self.rear = (self.rear + 1) % self.MAX_QSIZE

    def dequeue(self):
        if self.isEmpty():
            raise Exception("Queue is empty")
        item = self.items[self.front]
        self.items[self.front] = None  # Clear the dequeued element
        self.front = (self.front + 1) % self.MAX_QSIZE
        return item

    def peek(self):
        if self.isEmpty():
            raise Exception("Queue is empty")
        return self.items[self.front]

    def isEmpty(self):
        return self.front == self.rear

    def isFull(self):
        return (self.rear + 1) % self.MAX_QSIZE == self.front

    def clear(self):
        self.front = self.rear = 0
        self.items = [None] * self.MAX_QSIZE

class CircularDeque(CircularQueue):
    def __init__(self):
        super().__init__(10)

    def addRear(self, item):
        self.enqueue(item)

    def deleteFront(self):
        return self.dequeue()

    def getFront(self):
        return self.peek()

    def addFront(self, item):
        if self.isFull():
            raise Exception("Deque is full")
        self.front = (self.front - 1 + self.MAX_QSIZE) % self.MAX_QSIZE
        self.items[self.front] = item

    def deleteRear(self):
        if self.isEmpty():
            raise Exception("Deque is empty")
        self.rear = (self.rear - 1 + self.MAX_QSIZE) % self.MAX_QSIZE
        return self.items[self.rear]

    def getRear(self):
        if self.isEmpty():
            raise Exception("Deque is empty")
        return self.items[(self.rear - 1 + self.MAX_QSIZE) % self.MAX_QSIZE]

class Passenger:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return f"Passenger ID: {self.id}, Name: {self.name}"

class TicketAgent:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.serving_passenger = None

    def assign_passenger(self, passenger):
        self.serving_passenger = passenger

    def serve_passenger(self):
        if self.serving_passenger:
            print(f"{self.name} is serving {self.serving_passenger}")
            # time.sleep(random.uniform(1, 3))
            print(f"{self.name} has served {self.serving_passenger}")
            self.serving_passenger = None

class TicketCounterSimulation:
    def __init__(self, num_agents, num_passengers):
        self.agents = [TicketAgent(i, f"Agent {i}") for i in range(1, num_agents + 1)]
        self.passenger_queue = CircularQueue(50)
        self.passengers = [Passenger(i, f"Passenger {i}") for i in range(1, num_passengers + 1)]

    def simulate(self):
        for passenger in self.passengers:
            self.passenger_queue.enqueue(passenger)

        while not self.passenger_queue.isEmpty():
            for agent in self.agents:
                if agent.serving_passenger is None and not self.passenger_queue.isEmpty():
                    passenger = self.passenger_queue.dequeue()
                    agent.assign_passenger(passenger)
                    agent.serve_passenger()
                    
                    
class Maze:
    Maze_Size = 6

    def __init__(self):
        self.map = [['e', '1', '1', '1', '1', '1'],
                    ['0', '0', '1', '0', '0', '1'],
                    ['1', '0', '0', '0', '1', '1'],
                    ['1', '0', '1', '0', '1', '1'],
                    ['1', '0', '1', '0', '0', '1'],
                    ['1', '1', '1', '1', 'z', '1']]

    def getMap(self):
        return self.map

    def printMaze(self):
        for row in self.map:
            print(" ".join(row))
        print("\n")

    def isValidPos(self, x, y, map):
        return 0 <= x < Maze.Maze_Size and 0 <= y < Maze.Maze_Size and (map[x][y] != '1' and map[x][y] != 'X' or map[x][y] == 'e')

    def DFS1(self):
        stack = CircularDeque()
        start_x, start_y = 0, 0  # Starting position
        stack.addFront(Cell(start_x, start_y))
        count = 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up

        while not stack.isEmpty():
            count += 1
            time.sleep(1)
            self.printMaze()
            cell = stack.getFront()
            x, y = cell.row, cell.col

            found = False  # Flag to track if a valid move is found

            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy
                if self.map[new_x][new_y] == 'z':
                        print("DFS1 based algorithm need to {}times to solve this problem".format(count))
                        return True   
                if self.isValidPos(new_x, new_y, self.map):
                    stack.addFront(Cell(new_x, new_y))
                    self.map[new_x][new_y] = 'X'  # Mark as visited
                    found = True  # Valid move found

            if not found:
                stack.deleteFront()  # Backtrack if no valid moves are found

        return False


    def DFS2(self):
        stack = Stack()
        start_x, start_y = 0, 0  # Starting position
        stack.push(Cell(start_x, start_y))
        count = 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up

        while not stack.isEmpty():
            count += 1
            cell = stack.pop()
            x, y = cell.row, cell.col
            # time.sleep(1)  # Add a delay for visualization (adjust as needed)
            # self.printMaze()

            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy
                if self.isValidPos(new_x, new_y, self.map):
                    stack.push(Cell(new_x, new_y))
                    if self.map[new_x][new_y] == 'z':
                        print("DFS2 based algorithm need to {}times to solve this problem".format(count))
                        return True
                    self.map[new_x][new_y] = 'X'  # Mark as visited

        return False
    
    def DFS3(self):
        stack = CircularDeque()
        start_x, start_y = 0, 0  # Starting position
        stack.addRear(Cell(start_x, start_y))
        count = 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up

        while not stack.isEmpty():
            count += 1
            self.printMaze()  # Print the maze at each step for visualization
            time.sleep(1)  # Add a delay for visualization (adjust as needed)

            cell = stack.deleteRear()
            x, y = cell.row, cell.col

            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy
                if self.isValidPos(new_x, new_y, self.map):
                    if self.map[new_x][new_y] == 'z':
                        print("DFS3 based algorithm need to {}times to solve this problem".format(count))
                        return True
                    stack.addRear(Cell(new_x, new_y))
                    self.map[new_x][new_y] = 'X'  # Mark as visited

        return False

    def BFS1(self):
        queue = CircularDeque()  # Using CircularDequeue as a queue
        start_x, start_y = 0, 0  # Starting position
        queue.enqueue(Cell(start_x, start_y))
        count = 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up

        while not queue.isEmpty():
            count += 1
            time.sleep(1)
            self.printMaze()
            
            cell = queue.dequeue()
            x, y = cell.row, cell.col

            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy
                if self.map[new_x][new_y] == 'z':
                        print("BFS1 based algorithm need to {}times to solve this problem".format(count))
                        return True
                if self.isValidPos(new_x, new_y, self.map):
                    queue.enqueue(Cell(new_x, new_y))
                    self.map[new_x][new_y] = 'X'  # Mark as visited

        return False

    def BFS2(self):
        queue = CircularQueue(30)  # Using CircularQueue as a queue
        start_x, start_y = 0, 0  # Starting position
        queue.enqueue(Cell(start_x, start_y))
        count = 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up

        while not queue.isEmpty():
            count += 1
            time.sleep(1)
            self.printMaze()
            cell = queue.dequeue()
            x, y = cell.row, cell.col

            for dx, dy in directions:        
                new_x, new_y = x + dx, y + dy
                if self.map[new_x][new_y] == 'z':
                        print("BFS2 based algorithm need to {}times to solve this problem".format(count))
                        return True                        
                if self.isValidPos(new_x, new_y, self.map):
                    queue.enqueue(Cell(new_x, new_y))
                    self.map[new_x][new_y] = 'X'  # Mark as visited

        return False


class Cell:
    def __init__(self, r=0, c=0):
        self.row = r
        self.col = c

    def __str__(self):
        return f"({self.row}, {self.col})"


class Stack:
    def __init__(self):
        self.top = []

    def __contains__(self, item):
        return item in self.top

    def __iter__(self):
        return iter(self.top)

    def __str__(self):
        return str(self.top)

    def push(self, item):
        self.top.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.top.pop()

    def peek(self):
        if not self.isEmpty():
            return self.top[-1]

    def isEmpty(self):
        return len(self.top) == 0

    def size(self):
        return len(self.top)

    def clear(self):
        self.top = []