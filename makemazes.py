import random


class Maze:
    """
    A class representing a maze generated using depth-first search.
    Attributes:
        xsize (int): The width of the maze.
        ysize (int): The height of the maze.
        represent (list): A 2D list representing the cells of the maze.
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

    def __init__(self, xsize: int, ysize: int) -> None:
        """
        Initializes a new instance of the Maze class.
        Args:
            xsize (int): The width of the maze.
            ysize (int): The height of the maze.
        """
        self.xsize = xsize
        self.ysize = ysize
        self.represent = []
        self.graph = {}
        self.maze = {}
        self.startmaze()
        self.visited = [False] * (self.xsize * self.ysize)
        self.buildmaze(random.randint(0, self.xsize * self.ysize - 1))
        print("")
        print("")
        print("The maze!")
        for key in self.maze.keys():
            print(f"{key}: {self.maze.get(key)}")
        self.mazegrid = []
        self.getgrid()

    def startmaze(self) -> None:
        """
        Initializes the maze graph.
        """
        for x in range(0, self.ysize * self.xsize, self.xsize):
            row = []
            for y in range(x, x + self.xsize):
                row.append(y)
            self.represent.append(row)
        self.graph = {}
        for x in range(0, self.xsize):
            for y in range(0, self.ysize):
                connections = []
                cellid = self.represent[y][x]
                if self.xsize > x + 1 >= 0:
                    connections.append(self.represent[y][x + 1])
                if self.xsize > x - 1 >= 0:
                    connections.append(self.represent[y][x - 1])
                if self.ysize > y - 1 >= 0:
                    connections.append(self.represent[y - 1][x])
                if self.ysize > y + 1 >= 0:
                    connections.append(self.represent[y + 1][x])
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

    def getgrid(self) -> None:
        """
        Generates a grid that represents the maze for display purposes
        """
        destination = random.randint(1, self.xsize * self.ysize)
        grid = []
        row = ["W"] * (self.xsize * 2 + 1)
        grid.append(row)
        for y in range(0, self.ysize):
            row = ["W"]
            for x in range(0, self.xsize):
                row.append(self.represent[y][x])
                current = self.represent[y][x]
                if self.xsize > x + 1 >= 0 and self.represent[y][x + 1] in self.maze.get(current):
                    row.append(".")
                else:
                    row.append("W")
            grid.append(row)
            row = ["W"] * (self.xsize * 2 + 1)
            grid.append(row)
        for y in range(2, len(grid) - 1, 2):
            for x in range(1, len(grid[y]), 2):
                current = grid[y - 1][x]
                connections = self.maze.get(current)
                down = grid[y + 1][x]
                if down in connections:
                    grid[y][x] = "."
        for y in range(0, len(grid)):
            for x in range(0, len(grid[y])):
                if grid[y][x] == destination:
                    grid[y][x] = "WIN"
        self.mazegrid = grid
