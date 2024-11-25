def aStarAlgo(start_node, stop_node):
    # Open and closed sets
    open_set = set([start_node])
    closed_set = set()

    # g represents the cost from start_node to the current node
    g = {start_node: 0}

    # Parents map for reconstructing the path
    parents = {start_node: None}

    while open_set:
        # Node with the lowest f = g + heuristic
        n = None
        for node in open_set:
            if n is None or g[node] + heuristic(node) < g[n] + heuristic(n):
                n = node

        if n is None:
            print("Path does not exist!")
            return None

        # If the destination node is reached
        if n == stop_node:
            path = []
            while n is not None:
                path.append(n)
                n = parents[n]
            path.reverse()
            print(f"Path found: {path}")
            return path

        # Get neighbors and evaluate them
        for (neighbor, weight) in get_neighbors(n):
            if neighbor not in open_set and neighbor not in closed_set:
                open_set.add(neighbor)
                parents[neighbor] = n
                g[neighbor] = g[n] + weight
            else:
                if g[neighbor] > g[n] + weight:
                    g[neighbor] = g[n] + weight
                    parents[neighbor] = n
                    if neighbor in closed_set:
                        closed_set.remove(neighbor)
                        open_set.add(neighbor)

        # Move current node from open to closed set
        open_set.remove(n)
        closed_set.add(n)

    print("Path does not exist!")
    return None


def get_neighbors(v):
    """
    Returns the neighbors of a given node.
    """
    return Graph_nodes.get(v, [])


def heuristic(n):
    """
    Returns the heuristic distance for a given node.
    """
    H_dist = {
        'A': 11,
        'B': 6,
        'C': 99,
        'D': 1,
        'E': 7,
        'G': 0,
    }
    return H_dist.get(n, float('inf'))


# Define the graph as an adjacency list
Graph_nodes = {
    'A': [('B', 2), ('E', 3)],
    'B': [('C', 1), ('G', 9)],
    'C': [],
    'E': [('D', 6)],
    'D': [('G', 1)],
}

# Execute the algorithm
aStarAlgo('A', 'G')
