import heapq
import Problem
from Component import Node, Grid

def dfs(init_node: Node, grid: Node):
    frontier = [init_node]
    explored = set()
    node_count = 0

    while frontier:
        current_node = frontier.pop()
        explored.add(current_node.get_state())

        if Problem.is_goal(current_node, grid):
            return node_count, current_node

        for successor_node in Problem.get_successor_nodes(current_node, grid):
            state = successor_node.get_state()

            if state in explored:
                continue

            frontier.append(successor_node)
            explored.add(state)
            node_count += 1

    return node_count, None

def bfs(init_node, grid):
    frontier = [init_node]  
    explored = set()
    node_count = 0

    while frontier:
        current_node = frontier.pop(0)  
        explored.add(current_node.get_state())

        if Problem.is_goal(current_node, grid):
            return node_count, current_node
        
        for successor_node in Problem.get_successor_nodes(current_node, grid):
            state = successor_node.get_state()
            
            if state in explored:
                continue

            frontier.append(successor_node)  
            explored.add(state)
            node_count += 1

    return node_count, None  

def ucs(init_node: Node, grid: Grid):
    frontier = []
    explored = {}
    node_count = 0
    
    heapq.heappush(frontier, (init_node.weight, init_node))
    
    while frontier:
        _, current_node = heapq.heappop(frontier)
        
        explored[current_node.get_state()] = current_node.weight
        
        if Problem.is_goal(current_node, grid):
            return node_count, current_node

        for successor_node in Problem.get_successor_nodes(current_node, grid):
            state = successor_node.get_state()

            if state in explored and explored[state] <= successor_node.weight:
                continue
            
            heapq.heappush(frontier, (successor_node.weight, successor_node))
            explored[state] = successor_node.weight
            node_count += 1

    return node_count, None  

def a_star(init_node: Node, grid: Grid):
    frontier = []
    explored = {}
    node_count = 0
    
    heapq.heappush(frontier, (Problem.get_heuristic(init_node, grid) + init_node.weight, init_node))
    
    while frontier:
        _, current_node = heapq.heappop(frontier)
        
        explored[current_node.get_state()] = current_node.weight
        
        if Problem.is_goal(current_node, grid):
            return node_count, current_node

        for successor_node in Problem.get_successor_nodes(current_node, grid):
            state = successor_node.get_state()
            total_cost = successor_node.weight + Problem.get_heuristic(successor_node, grid)

            if state in explored and explored[state] <= successor_node.weight:
                continue
            
            heapq.heappush(frontier, (total_cost, successor_node))
            explored[state] = successor_node.weight
            node_count += 1

    return node_count, None  