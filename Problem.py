from Component import Node, Grid

def is_goal(node: Node, grid: Grid) -> bool:
    return set([(r, c) for r, c, _ in node.stones]) == set(grid.switches)

def get_successor_nodes(node: Node, grid: Grid) -> list[Node]:
    successor_nodes: list[Node] = []
    
    for dx, dy, dir in [(-1, 0, 'u'), (1, 0, 'd'), (0, -1, 'l'), (0, 1, 'r')]:
        ins_stones = node.stones[:]
        ins_ares = (node.ares[0] + dx, node.ares[1] + dy)
        ins_weight = 1
        ins_dir = dir

        if ins_ares in grid.walls:
            continue
        
        ins_stones_pos = [(x, y) for x, y, _ in node.stones][:]

        if ins_ares in ins_stones_pos:
            ins_push = (ins_ares[0] + dx, ins_ares[1] + dy)

            if ins_push in ins_stones_pos + grid.walls:
                continue

            idx = ins_stones_pos.index(ins_ares)
            ins_stones[idx] = ins_push + (ins_stones[idx][2],)
            ins_weight = ins_stones[idx][2]
            ins_dir = ins_dir.upper()

        successor_nodes.append(Node(
            ares=ins_ares,
            stones=ins_stones,
            parent=node,
            weight=node.weight + ins_weight,
            dir=ins_dir
        ))
    
    return successor_nodes

def get_heuristic(node: Node, grid: Grid):
    return sum(min(abs(sx - x) + abs(sy - y) for sx, sy in grid.switches) * w for x, y, w in node.stones)