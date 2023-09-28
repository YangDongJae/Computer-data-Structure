from Lab04 import *

# Test the CircularDeque
def test_Dequeue():
    dq = CircularDeque()
    dq.addFront(1)
    dq.addRear(2)
    dq.addFront(3)
    dq.addRear(4)
    print("Deque:", dq)
    print("Front:", dq.getFront())
    print("Rear:", dq.getRear())
    dq.deleteFront()
    dq.deleteRear()
    print("Deque after deletions:", dq)

def test_passenger_simul():
    num_agents = 3
    num_passengers = 15

    simulation = TicketCounterSimulation(num_agents, num_passengers)
    simulation.simulate()
    
def test_Maze():
    maze1 = Maze()
    maze2 = Maze()
    maze3 = Maze()
    maze4 = Maze()
    maze5 = Maze()

    print("DFS1 Result:", maze1.DFS1())
    print("DFS2 Result:", maze2.DFS2())
    print("DFS3 Result:", maze3.DFS3())
    print("BFS1 Result:", maze4.BFS1())
    print("BFS2 Result:", maze5.BFS2())
    
if __name__ == "__main__":
    # test_Dequeue()
    # test_passenger_simul()
    test_Maze()
