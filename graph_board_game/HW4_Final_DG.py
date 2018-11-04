# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 09:49:44 2018

@author: Deepak
"""

import math
edges=[]

#READING GRAPH FROM TEXT FILE
with open('graph_board_Lose.txt') as f:
#with open('graph_board_Win.txt') as f:
#with open('graph_board2_Tie.txt') as f:
#with open('graph_board2_Win_Island.txt') as f:
    array = [[int(x) for x in line.split()] for line in f]
print(array)
line1=array[0]
Actual_N=line1[0]
for i in range(len(array)-1):
    edges.append(array[i+1])


#edges=[[1, 2],[1, 3], [2, 3], [2, 4],[3, 4],[4, 5]]  # A will lose 
#edges=[[1,2],[1,3],[2,5],[3,5],[2,4],[3,4],[5,4],[3,2]] # A will win 
#edges=[[1,2]] # Its a TIE
#edges=[[1,2],[1,4],[2,3],[3,4]] # A will lose
#edges=[[1,3],[3,4],[1,4]]  # A wins always
#edges=[[1,2],[1,3],[2,3]]  # A will lose
#edges=[[1,2], [1,3]]  # A loses
#edges=[[1,2],[1,3],[2,3],[3,4]]


global N, count, total_nodes, maxdepth, state, ans, path
state=1
maxdepth=[]
total_nodes=[]
path=[]

edges1=list(edges)

#REMOVING ISLANDS FROM EDGES
q=0
for i in edges1:
    if i[0]==i[1]:
        q=q+1
        print('a=',q)
        print('i=',i)
        edges.remove(i)
        N=max(sum(edges, []))+q
    else:
        N=max(sum(edges, []))
        

print('New edges: ',edges)
E=len(edges)


ans=0
count=0

# NODE CLASS
class Node:
    def __init__( self,state, parent,colors, depth, score ):
        self.state = state
        self.parent = parent
        self.depth = depth
        self.colors = colors
        self.score = score

    
# CREATES A NODE
def create_node(state,parent, colors, depth, score):
    return Node(state, parent, colors, depth, score)

# EXPANDS THE NODES
def expand_node( node, nodes):
    global count, total_nodes, state
    indices = [i for i, x in enumerate(node.colors) if x == 0]
    print('\n \nstate selected for expansion')
    print(node.colors)
    expanded_nodes = []
    if len(indices)>0:
        for i in indices:
            col=list(node.colors)
            col[i]=player(node.colors)
            a,sc=check_terminal(col,node.depth+1,node.score)
            if a==0:
                expanded_nodes.append(create_node(state+1, node.state, col, node.depth+1, 0))
                total_nodes.append(create_node(state+1, node.state, col, node.depth+1, 0))
                maxdepth.append(node.depth+1)
                state=state+1
            else:
                expanded_nodes.append(create_node(state+1, node.state, col, node.depth+1, sc))
                total_nodes.append(create_node(state+1, node.state, col, node.depth+1, sc))
                maxdepth.append(node.depth+1)
                state=state+1
                
            count=count+1
            print('node created with color=',col,' depth=', node.depth+1,' utility value=', sc)
    else:
        print('Node cannot be expanded')
        print('node color',node.colors)
        a,sc=check_terminal(node.colors,node.depth+1,node.score)
        if a!=0:
            node.score=sc
        print(node.colors, node.depth, node.score)
#    print(col)
    
    print(node.colors, node.depth, node.score)
    return expanded_nodes


def player(colors):
    if (colors.count(1)==colors.count(2)) or (colors.count(2)>colors.count(1)):
        return 1
    elif colors.count(1)>colors.count(2):
        return 2

#def result(colors, action):
#    colors[action[0]]=action[1]     #action [5,1] means color vetex 5 by color 1


# CHECK FOR TERMINAL STATE AND ASSIGN A UTILITY VALUE (SCORE)
def check_terminal(colors,depth,score):
    a=0
    b=0
    global N
    if colors.count(0)!=0:
        for i in range(E):
            if ((colors[edges[i][0]-1]==colors[edges[i][1]-1]) and (colors[edges[i][0]-1]!=0) and (colors[edges[i][1]-1]!=0)):
                a=a+1
                b=colors[edges[i][0]-1]
        if a>0:
            if b==1:
                print('\nB WON !!')
                score=-depth*10
            else:
                print('\nA WON !!')
                score=(N-depth+1)*10
                
        return(a,score)   
            
    elif colors.count(0)==0:
        for i in range(E):
            if colors[edges[i][0]-1]==colors[edges[i][1]-1]:
                a=a+1
                b=colors[edges[i][0]-1]
        if a>0:
            if b==1:
                print('\nB WON !!')
                score=-depth*10
                
            elif b==2:
                print('\nA WON !!')
                score=(N-depth+1)*10
        else:
                print('\nITS A TIE')
        return(a,score)           
        
        
# BREADTH FIRST SEARCH        
def bfs(colors):
    global total_nodes, state
    print('start state')
    nodes=[]
    nodes.append(create_node(state, 0, colors,0, 0))
    total_nodes.append(create_node(state, 0, colors,0,0))
    maxdepth.append(0)
#    score=0
    while True:
        if len( nodes ) == 0: return None
        node = nodes.pop(0)

        
        if node.score==0:
            nodes.extend(expand_node(node, nodes))

#        print('The length of total_nodes is: ', len(total_nodes))

# REMOVES THE REPEATED PARENTS
def unique(seq): 
   # order preserving
   checked = []
   for e in seq:
       if e not in checked:
           checked.append(e)
   return checked

# FINDS THE MAXIMUM SCORES OF ALL CHILDS WITH SAME PARENT    
def find_child_scores_max(parent_state):
    temp_node=[]
    score=[]
    score.append(-10000)
    for i in total_nodes:
        if i.parent==parent_state:
            temp_node.append(i)
    for j in temp_node:
        score.append(j.score)
    return(max(score))
    

# FINDS THE MINIMUM SCORES OF ALL CHILDS WITH SAME PARENT    
def find_child_scores_min(parent_state):
    temp_node=[]
    scores=[]
    scores.append(10000)
    for i in total_nodes:
        if i.parent==parent_state:
            temp_node.append(i)
    for j in temp_node:
#        print(j.state, j.score)
        scores.append(j.score)
    return(min(scores))

#MINIMAX FUNCTION   
def minmax_decision(total_nodes,d):
    global ans
    temp_nodes=[]
    indices=[]
    node=[]
    parent=[]
    i=range(d+1)
    c=d
    value1=-math.inf
    value2=math.inf
    value=[]
    
    
    for i in range(d+1,0,-1):
        for node in total_nodes:
#            print(i)
            if node.depth==i:
                temp_nodes.append(node)
                parent.append(node.parent)
        parent1=unique(parent)
        
        print('parent1=',parent1)
        
        for k in parent1:
            indices = [kk for kk, x in enumerate(parent) if x == k]
#            for kk in indx:
#                indices.append(parent[kk])
#            print('indices = ',indices)
            for l in indices:
                print('Child state = ',temp_nodes[l].state,'depth = ',c+1,'Parent state = ',parent[l], 'Parent score = ',temp_nodes[l].score)
                if c%2==0:
                    if temp_nodes[l].score==0:
                        total_nodes[temp_nodes[l].state-1].score=find_child_scores_min(temp_nodes[l].state)
                        temp_nodes[l].score=find_child_scores_min(temp_nodes[l].state)
                        print('Parent score updated', temp_nodes[l].score)
                        value.append(temp_nodes[l].score)
#                        ans=temp_nodes[l].score
#                        print('ans=',ans)
                    else:
                        value.append(max(value1,temp_nodes[l].score))
                else:
                    if temp_nodes[l].score==0:
#                        print('min of child scores = ',find_child_scores_min(temp_nodes[l].state))
                        total_nodes[temp_nodes[l].state-1].score=find_child_scores_min(temp_nodes[l].state)
                        temp_nodes[l].score=find_child_scores_max(temp_nodes[l].state)
                        print('Parent score updated', temp_nodes[l].score)
                        value.pop
                        value.append(temp_nodes[l].score)
#                        ans=temp_nodes[l].score
#                        print('ans=',ans)
                    else:
                        value.append(min(value2,temp_nodes[l].score))
            
            if c%2==0:
#                print('even = ', c%2==0)
#                print(value)
                print('the max value is ',max(value),'\n')
                ans=max(value)
                
            else:
#                print('even = ', c%2==0)
                print('the min value is ',min(value),'\n')
                ans=min(value)
                
                indices=[]
                value=[]
        temp_nodes=[]
        c=c-1    
        parent1=[]
        parent=[]
    
        
    if ans==0 or (ans==-10000) or (ans==10000):
        print('\n\nBest possibility is TIE !')
    elif ans<0:
        print('\n\nA is going to LOSE')
    else:
        print('\n\nA will win')
        total_nodes[0].score=max(value)
            

    
def main():
    global N,count, total_nodes, maxdepth
    colors=[]
    best_choice=[]
    temp_score=[]
    temp_nodes=[]

    for i in range(N):
        colors.append(0)      
    print(colors)
    bfs(colors)  
    print(count)
    
    d=max(maxdepth)
    minmax_decision(total_nodes,d)

#ALL NODES WITH FINAL UTILITY VALUES 
#    for i in total_nodes:
#        print(i.state, i.parent, i.colors, i.depth, i.score)
    
    for i in total_nodes:
        if i.depth==1:
            temp_score.append(i.score)
            temp_nodes.append(i)
    indx = temp_score.index(max(temp_score))
    best_choice=temp_nodes[indx].colors
    print('The best choice for the 1st player to start with is :', best_choice)
    print('\nNOTE: 0==> Uncolored \t 1==> 1st player color(RED) \t 2==> 2nd player color(BLUE)\n\n')

if __name__ == "__main__":
	main()