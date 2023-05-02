import random


class Maze:
    """
    A class representing a maze generated using depth-first search.

    Attributes:
        size (int): The size of the maze.
        represent (list): A 2D list representing the cells of the maze.
        difficulty (str): The difficulty level of the maze.
        graph (dict): A graph representation of the maze.
        maze (dict): The final maze represented as a graph.
        visited (list): A list of boolean values indicating whether each cell has been visited.

    Methods:
        __init__(self, size: int, difficulty: str, start: int) -> None:
            Initializes a new instance of the Maze class.

        startmaze(self) -> None:
            Initializes the maze graph.

        buildmaze(self, node: int) -> None:
            Generates the maze using depth-first search.
    """

    def __init__(self, size: int, difficulty: str, start: int) -> None:
        """
        Initializes a new instance of the Maze class.

        Args:
            size (int): The size of the maze.
            difficulty (str): The difficulty level of the maze.
            start (int): The starting node for the maze generation.
        """
        self.size = size
        self.represent = []
        self.difficulty = difficulty
        self.graph = {}
        self.maze = {}
        self.startmaze()
        self.visited = [False] * (self.size * self.size)
        self.buildmaze(start)
        print("")
        print("")
        print("The maze!")
        for key in self.maze.keys():
            print(f"{key}: {self.maze.get(key)}")

    def startmaze(self) -> None:
        """
        Initializes the maze graph.
        """
        for x in range(0, self.size * self.size, self.size):
            row = []
            for y in range(x, x + self.size):
                row.append(y)
            self.represent.append(row)
        self.graph = {}
        for x in range(0, self.size):
            for y in range(0, self.size):
                connections = []
                cellid = self.represent[x][y]
                if self.size > x + 1 >= 0:
                    connections.append(self.represent[x + 1][y])
                if self.size > x - 1 >= 0:
                    connections.append(self.represent[x - 1][y])
                if self.size > y - 1 >= 0:
                    connections.append(self.represent[x][y - 1])
                if self.size > y + 1 >= 0:
                    connections.append(self.represent[x][y + 1])
                self.graph.update({cellid: connections})
        for key in self.graph.keys():
            print(f"{key}: {self.graph.get(key)}")

    def buildmaze(self, node: int) -> None:
        """
        Generates the maze using depth-first search.

        Args:
            node (int): The starting node for the maze generation.
        """
        self.visited[node] = True
        random.shuffle(self.graph.get(node))
        for child in self.graph.get(node):
            if not self.visited[child]:
                self.maze.setdefault(child, []).append(node)
                self.maze.setdefault(node, []).append(child)
                self.buildmaze(child)
