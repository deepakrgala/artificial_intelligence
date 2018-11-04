The code is written in Python checks the possiblity of A winning the game with B playing optimally. 
The code first expands the tree using Breadth First Search (BFS) and while doing so also assigns Utility (Score) value by checking for a terminal states.
Once the tree is complete with all utility values assigned, it uses 'minimax' function to appropriately choose the maximum and minimum utility values for the nodes with same parent nodes.

Utility values are 
	+10*depth for terminal state where A wins
	-10*depth for terminal state where B wins
	  0       for terminal state with a TIE
These utility values also allows to choose the shortest winning path (i.e. with least depth)

The text file (eg. graph_board_Lose.txt) with the number of edges and the edges information should be placed in the same folder
CASES:
graph_board_Lose.txt is the file that represent a graph in which A will always LOSE
graph_board_Win.txt is the file that represent a graph in which A will always WIN
graph_board_Tie.txt  is the file that represent a graph with a TIE
graph_board_Win_Island.txt is the file that represent a graph (with an ISLAND vertex - not connected to any other vertex) in which A will always WIN
graph_board_Lose_Island.txt is the file that represent a graph (with an ISLAND vertex) in which A will always LOSE

NOTE:
1. '0' represent the vertex is uncolored
2. '1' represent the vertex is colored RED (1st player's color, i.e. A's color)
3. '2' represent the vertex is BLUE (2nd player's color, i.e. B's color)
4. In case the graph has an ISLAND node 'x', 'x x' should be considered as an edge
   This will change the number of edges will also add 'x x' as an edge in the text file


The code displays
1. Whether A will WIN, LOSE, or it will be a TIE
2. Nodes at different depth with the utility values and their updated parent's utility values

