# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 11:22:30 2018

@author: Deepak
"""

import numpy as np

def display_state( state ):
	print (" ___________________ ")
	print (" | ", state[0]," | ", state[1]," | ", state[2]," | ")
	print (" ___________________ ")
	print (" | ", state[3]," | ", state[4]," | ", state[5]," | ")
	print (" ___________________ ")
	print (" | ", state[6]," | ", state[7]," | ", state[8]," | ")
	print (" ___________________ ")


global count
global fringe
count=0

# MOVING FUNCTIONS
def move_left( prev_state ):
    new_state = prev_state[:]
    index = new_state.index('*')     # return the index of *
    if (index != 0) and (index != 3) and (index != 6) :    # moving left is possible at all other location except 1st column
        temp = new_state[index - 1]
        new_state[index - 1] = new_state[index]
        new_state[index] = temp
        return new_state
    else:
        return None

def move_right( prev_state ):
    new_state = prev_state[:]
    index = new_state.index('*')
    if (index != 2) and (index != 5) and (index != 8) :    # moving right is possible at all other location except 3rd column
        temp = new_state[index + 1]
        new_state[index + 1] = new_state[index]
        new_state[index] = temp
        return new_state
    else:
        return None
    
def move_up( prev_state ):
    new_state = prev_state[:]
    index = new_state.index('*')
    if (index != 0) and (index != 1) and (index != 2) :    # moving up is possible at all other location except 1st row
        temp = new_state[index - 3]
        new_state[index - 3] = new_state[index]
        new_state[index] = temp
        return new_state
    else:
        return None

def move_down(prev_state ):
    new_state = prev_state[:]
    index = new_state.index('*')
    if (index != 6) and (index != 7) and (index != 8) :    # moving down is possible at all other location except 3rd row
        temp = new_state[index + 3]
        new_state[index + 3] = new_state[index]
        new_state[index] = temp
        return new_state
    else:
        return None

# CREATES A NODE
def create_node(state, parent, action, depth, cost):
    return Node(state, parent, action, depth, cost)

# EXPANDS THE NODES
def expand_node( node, nodes):
    print('\n \n state selected for expansion')
    display_state(node.state)
    print('state that will be added')
    expanded_nodes = []
    node_up= create_node( move_up( node.state ), node, "UP", node.depth + 1, 0 )
    node_down= create_node( move_down( node.state ), node, "DOWN", node.depth + 1, 0 )
    node_left= create_node( move_left( node.state ), node, "LEFT", node.depth + 1, 0 )
    node_right=create_node( move_right( node.state), node, "RIGHT", node.depth + 1, 0 )
    expanded_nodes.append(node_up )
    expanded_nodes.append(node_down )
    expanded_nodes.append(node_left )
    expanded_nodes.append( node_right )
    for node in expanded_nodes: 
        if node.state != None:
            print(node.state)
    expanded_nodes = [node for node in expanded_nodes if node.state != None]
    return expanded_nodes

# BREADTH FIRST SEARCH
def bfs( start, goal ):
    print('\n\nStart state:',start)
    nodes = []
    nodes.append( create_node( start, None, None, 0, 0 ) )
    while True:
        if len( nodes ) == 0: return None
        node = nodes.pop(0)
        if node.state == goal:
            print('goal reached!')
            moves = []
            temp = node
            while True:
                moves.insert(0, temp.action)
                if temp.depth == 1: break
                temp = temp.parent
            return moves				
        nodes.extend( expand_node( node, nodes) )
        global count, fringe
        count=count+1
        fringe=len(nodes)

# DEPTH FIRST SEARCH
def dfs( start, goal, depth=10 ):
    print('\n\nStart state:',start)
    depth_limit = depth
    nodes = []
    nodes.append( create_node( start, None, None, 0, 0 ) )
    while True:
        if len( nodes ) == 0: return None
        node = nodes.pop(0)
        if node.state == goal:
            print('goal reached!')
            moves = []
            temp = node
            while True:
                moves.insert(0, temp.action)
                if temp.depth <= 1: break
                temp = temp.parent
            return moves				
        if node.depth < depth_limit:
            expanded_nodes = expand_node( node, nodes )
            expanded_nodes.extend( nodes )
            nodes = expanded_nodes
            global count, fringe
            count=count+1
            fringe=len(nodes)
    

# ITERATIVE DEEPENING SEARCH
def ids( start, goal, depth=5 ):
    for i in range( depth ):
        result = dfs( start, goal, i )
        if result != None:
            print('\n\nfound in depth ',i)
            return result

# A-STAR SEARCH
def a_star( start, goal ):
    nodes = []
    mincost=0
    index=0
    y=[]
    nodes.append( create_node( start, None, None, 0, 0 ) )
    while True:
        if len( nodes ) == 0: return None        
        for i in range (len(nodes)):
            y=nodes[i]           
            # USE OOP FOR OUT OF PLACE HEURISTICS
            # USE MAN FOR MANHATTAN DISTANCE
            # USE OOP+MAN FOR BOTH ABOVE MENTIONED HEURISTICS TOGETHER
                        
 #           cost = y.depth + OOP(y,goal)
 #           cost = y.depth + MAN(y,goal)
            cost = y.depth + OOP(y,goal)+MAN(y,goal)
            
            if i==0:
                mincost=cost
                index=i
            elif mincost>cost:
                mincost=cost
                index=i
        node = nodes.pop(index)        
        print('Action: ', node.action)
        print('\nTrying state', node.state)
        if node.state == goal:
            print('goal reached!')
            moves = []
            temp = node
            while True:
                moves.insert( 0, temp.action )
                if temp.depth <=1: break
                temp = temp.parent
            return moves
        nodes.extend(expand_node( node, nodes) )
        global count, fringe
        count=count+1
        fringe=len(nodes)

# OUT OF PLACE TILES        
def OOP(x,goal):
	score = 0
	for i in range( len( x.state ) ):
		if x.state[i] != goal[i]:
			score = score + 1
	return score
     
# MANHATTAN DISTANCE
def MAN(x,g):
    distance=0
    x1=x.state
    g1=g
    x1=np.array(x1).reshape(3,3)
    g1=np.array(g1).reshape(3,3)
    for element in x.state:
        x_value=np.where(x1==element)[0]
        y_value=np.where(x1==element)[1]
        x_goal=np.where(g1==element)[0]
        y_goal=np.where(g1==element)[1]
        distance += abs(x_value - x_goal) + abs(y_value - y_goal)
#    print('Manhattan distance = ',distance)
    return(distance)


class Node:
    def __init__( self, state, parent, action, depth, cost ):
        self.state = state
        self.parent = parent
        self.action = action   # action that created this node
        self.depth = depth
        self.cost = cost

# Main method
def main():
    data_goal=input('Enter the GOAL state (position separated by spaces):')
    data_start=input('Enter the INITIAL state (position separated by spaces):')
    
    data_goal = data_goal.strip( "\n" )
    data_start = data_start.strip( "\n" )
    data_goal = data_goal.split( " " )
    data_start = data_start.split( " " )

    goal_state = []
    start_state = []
    for element in data_goal:
        goal_state.append( str( element ) )
    for element in data_start:
        start_state.append( str( element ) )
    
#    start_state=['1', '2','*', '3', '4', '5', '6', '7', '8']
#    goal_state=['*','1', '2', '3', '4', '5', '6', '7', '8']


# UNCOMMENT AS PER THE REQUIRED ALGORITHM TO WORK 
        # bfs ==> BREADTH FIRST SEARCH
        # dfs ==> DEPTH FIRST SEARCH
        # ids ==> ITERATIVE-DEEPENING SEARCH
        # a_star ==> A* SEARCH
        
    result = bfs( start_state, goal_state )
#    result = dfs( start_state, goal_state )                
#    result = ids( start_state, goal_state )
#    result = a_star( start_state, goal_state )
        
    print('\nnumber of states expanded:',count)
    print('number of states in the fringe: ',fringe)
    
    if result == None:
        print ("No solution found")
    elif result == [None]:
        print ("Start node was the goal!")
    else:
        print('\nRequired actions are: ',result)
        print ('required number of moves: ', len(result))

if __name__ == "__main__":
	main()