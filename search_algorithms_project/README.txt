Author: Deepak Gala
The code (written in PYTHON) consists of 4 search algorithms 
1. bfs    ==>    BREADTH FIRST SEARCH
2. dfs    ==>    DEPTH FIRST SEARCH
3. ids    ==>    ITERATIVE DEEPENING SEARCH
4. a_star ==>    A* SEARCH
Respective algorithm can be chosen from the main function by uncommenting the required

The a_star algorithm is capable of using 2 heuristics in three ways
1. OOP ==> OUT OF PLACE TILE
2. MAN ==> MANHATTAN DISTANCE
3. OOP + MAN
Respective heuristic option can be chosen from the a_star algorithm by uncommenting the one required


The user is asked to enter the goal state and the initial state. These states must be entered with each tile separated by single space
Enter the GOAL state (position separated by spaces):* 1 2 3 4 5 6 7 8
Enter the INITIAL state (position separated by spaces):1 2 * 3 4 5 6 7 8

The code also displays
1. State selected for expansion
2. States that will be added to the fringe
3. Number of states expanded (only at the end of the search)
4. Number of states in the fringe (only at the end of the search)
