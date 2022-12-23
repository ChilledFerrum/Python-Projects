# Maze Generator using Pygame in Python Version (1.0)
### With 3 maze generation and 2 maze solving algorithms

**Description:** <br/>
  This algorithm contains parameters that are available to the user in which it allows the user to change the output of the maze generation algorithm. It contains a total of 3 maze generation algorithms and 2 maze solving algorithms. The generation algorithms are Iterative-Backtracking or DFS, Breadth-First-Search and Disjoint-sets. The maze solving algorithms are based on the Iterative-backtracking or DFS algorithm and the Breadth-First-Search algorithm. <br/>
  Within the project every algorithm's changes are visualized using pygame. Most of the operations and functions are written in the Canvas.py and Maze.py files.
<br/>
<br/>
**Parameters:** <br/>
The user can modify the following parameters based on their needs. The parameters are located in the Canvas.py file <br/>
 - rows = <Number of rows in the Maze (is Integer)> <br/>
 - cols = <Number of Colums in the Maze (is Integer)> <br/>
 - cellWidth = <The width of each cell in the Maze (is Integer) (The resolution of the maze is as follows Width: cols*cellWidth, Height: rows*cellwidth + UIoffset)> <br/>
 - FPS = <The tick speed of the maze generation algorithms (Is Integer)> <br/>
 - MazeSolver_TickSpeed = <The tick speed of the maze solving algorithms (Is Integer)> <br/>
 - use_BFS_Maze_Solver = <Write False to use the Iterative-Backtracking or DFS algorithm as the maze solver or True to use the BFS Maze Solver algorithm as the maze solver> <br/>
 - use_x_MazeGeneration_Algorithm = <Choose one of the 3 maze generation algorithms based on the below dictionary. (Read Comments if needed) (Is Integer)> <br/>

  
  ![](https://github.com/ChilledFerrum/Python/imgs/MazeGeneratorandMazeSolverBFSgen.gif)
