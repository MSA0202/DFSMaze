class dfs:
    #Start at S and goal is E
    #Able to move up, right, left down
    #need function to define movement
    #need to record previous moves
    def __init__(self):
        self.recordMoves = []

    def printMaze(self,maze):
        for row in maze:
            for column in row:
                print(column,end="")
            print()

    def startingPosition(self,maze):
        for row in range(len(maze)):
            for column in range(len(maze[row])):
                if maze[row][column] == 'S':
                    return row,column #x,y coords
                
    def goalPosition(self,maze):
        for row in range(len(maze)):
            for column in range(len(maze[row])):
                if maze[row][column] == 'E':
                    return row,column #x,y coords
                    
    def up(self,currentRow,currentColumn,maze):
        moveUp = currentRow - 1
        if maze[moveUp][currentColumn] != '#':
            self.recordMoves.append([moveUp,currentColumn])

    # def right(self,currentCoords):

    # def down(self,currentCoords):

    # def left(self,currentCoords):
    
    # def DFS(self, maze):
    #     recordMoves = []
    #     #


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
    init.printMaze(maze1)
    print(init.startingPosition(maze1))

if __name__ == '__main__':
    main()
