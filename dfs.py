class dfs:

    def __init__(self):
        self.recordMoves = [] #for testing, put as empty after
        self.visited = []

    def printMaze(self,maze):
        for row in maze:
            for column in row:
                print(column,end="")
            print()

    def startingPosition(self,maze):
        for row in range(len(maze)):
            for column in range(len(maze[row])):
                if maze[row][column] == 'S':
                    return [row,column] #x,y coords
                
    def goalPosition(self,maze):
        for row in range(len(maze)):
            for column in range(len(maze[row])):
                if maze[row][column] == 'E':
                    return [row,column] #x,y coords
                    
    def move(self,currentRow,currentColumn,maze):
        moveUp = currentRow - 1
        moveRight = currentColumn + 1
        moveDown = currentRow + 1
        moveLeft = currentColumn - 1

        if maze[moveUp][currentColumn] != '#' and ([moveUp,currentColumn] not in self.visited):
            self.recordMoves.append([moveUp,currentColumn]) # append coordinates
            self.visited.append([moveUp,currentColumn])
        elif maze[currentRow][moveRight] != '#'  and ([currentRow,moveRight] not in self.visited):
            self.recordMoves.append([currentRow,moveRight])
            self.visited.append([currentRow,moveRight])
        elif maze[moveDown][currentColumn] != '#' and ([moveDown,currentColumn] not in self.visited):
            self.recordMoves.append([moveDown,currentColumn])
            self.visited.append([moveDown,currentColumn])
        elif maze[currentRow][moveLeft] != '#' and ([currentRow,moveLeft] not in self.visited):
            self.recordMoves.append([currentRow,moveLeft])
            self.visited.append([currentRow,moveLeft])
        else: #backtrack to previous move
            self.recordMoves.pop()

    def printRoute(self,maze):
        for row in range(len(maze)):
            for column in range(len(maze)):
                if [row,column] in self.recordMoves and [row,column] != self.startingPosition(maze) and [row,column] != self.goalPosition(maze):
                    maze[row][column] = '*'
                
    def DFS(self, maze):
        currentRow = self.startingPosition(maze)[0]
        currentColumn = self.startingPosition(maze)[1]
        while self.goalPosition(maze) not in self.recordMoves:
            self.move(currentRow,currentColumn,maze)
            currentRow = self.recordMoves[len(self.recordMoves)-1][0] #because we always want to be at the most recently added position that has been recorded
            currentColumn = self.recordMoves[len(self.recordMoves)-1][1]
        self.printRoute(maze)
        self.printMaze(maze)
        

def main():
    maze1 = [
        ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
        ["#", "S", " ", " ", " ", " ", " ", " ", " ", "#"],
        ["#", " ", "#", "#", "#", " ", "#", "#", " ", "#"],
        ["#", " ", "#", " ", "#", " ", "#", " ", " ", "#"],
        ["#", " ", " ", " ", "#", " ", "#", "#", "#", "#"],
        ["#", "#", "#", " ", "#", " ", " ", " ", " ", "#"],
        ["#", " ", "#", " ", "#", "#", "#", "#", " ", "#"],
        ["#", " ", "#", " ", " ", " ", " ", "#", " ", "#"],
        ["#", " ", " ", "#", "#", "#", " ", "#", "E", "#"],
        ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
    ]
    maze2 = [
        ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
        ["#", "S", " ", "#", " ", " ", " ", "#", " ", "#"],
        ["#", " ", " ", "#", " ", "#", " ", " ", " ", "#"],
        ["#", " ", "#", "#", " ", "#", "#", "#", "#", "#"],
        ["#", " ", "#", " ", " ", " ", " ", " ", "#", "#"],
        ["#", " ", "#", "#", "#", "#", "#", " ", " ", "#"],
        ["#", " ", " ", " ", "#", " ", "#", "#", " ", "#"],
        ["#", "#", "#", " ", "#", " ", " ", "#", " ", "#"],
        ["#", " ", " ", " ", " ", "#", " ", " ", "E", "#"],
        ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
    ]
    maze3 = [
        ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
        ["#", "S", "#", " ", " ", " ", "#", " ", " ", "#"],
        ["#", " ", "#", " ", "#", " ", "#", "#", " ", "#"],
        ["#", " ", " ", " ", "#", " ", " ", "#", " ", "#"],
        ["#", " ", "#", "#", "#", "#", " ", "#", " ", "#"],
        ["#", " ", " ", " ", "#", " ", " ", "#", " ", "#"],
        ["#", "#", "#", " ", "#", " ", "#", "#", " ", "#"],
        ["#", " ", "#", " ", " ", " ", "#", " ", " ", "#"],
        ["#", " ", " ", "#", "#", " ", " ", " ", "E", "#"],
        ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
    ]

    init = dfs()
    print("MAZE1")
    init.DFS(maze1)
    print("MAZE2")
    init.DFS(maze2)
    print("MAZE3")
    init.DFS(maze3)
if __name__ == '__main__':
    main()


# self.recordMoves  for maze1= [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [2, 5], [3, 5], [4, 5], [5, 5], [5, 6], [5, 7], [5, 8], [6, 8], [7, 8], [8, 8]] #for testing, put as empty after
