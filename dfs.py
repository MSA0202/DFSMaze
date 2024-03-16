class dfs:

    def __init__(self):
        self.recordMoves = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [2, 5], [3, 5], [4, 5], [5, 5], [5, 6], [5, 7], [5, 8], [6, 8], [7, 8], [8, 8]] #for testing, put as empty after

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

        if maze[moveUp][currentColumn] != '#' and ([moveUp,currentColumn] not in self.recordMoves): #and perhaps need to check if this move is not already recorded
            self.recordMoves.append([moveUp,currentColumn]) # append coordinates
        elif maze[currentRow][moveRight] != '#'  and ([currentRow,moveRight] not in self.recordMoves):
            self.recordMoves.append([currentRow,moveRight])
        elif maze[moveDown][currentColumn] != '#' and ([moveDown,currentColumn] not in self.recordMoves):
            self.recordMoves.append([moveDown,currentColumn])
        elif maze[currentRow][moveLeft] != '#' and ([currentRow,moveLeft] not in self.recordMoves):
            self.recordMoves.append([currentRow,moveLeft])

    def printRoute(self,maze):
        for row in range(len(maze)):
            for column in range(len(maze)):
                print([row,column])
                if [row,column] in self.recordMoves and [row,column] != self.startingPosition(maze) and [row,column] != self.goalPosition(maze):
                    maze[row][column] = '*'
                
    def DFS(self, maze):
        while self.goalPosition() not in self.recordMoves:
            self.move()
        self.printRoute()
        self.printMaze()
        

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
    #init.printMaze(maze1)
    #print(init.startingPosition(maze1))
    #print(type(init.startingPosition(maze1)))
    init.printRoute(maze1)
    init.printMaze(maze1)
if __name__ == '__main__':
    main()
