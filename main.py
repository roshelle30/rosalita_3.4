from collections import deque


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def bfs_binary_tree(root):
    if not root:
        return
    queue = deque([root])
    result = []

    while queue:
        current = queue.popleft()
        result.append(current.data)

        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

    print("Binary Tree BFS:", " -> ".join(result))


def dfs_binary_tree(node, result=None):
    if result is None:
        result = []
    if node:
        result.append(node.data)
        dfs_binary_tree(node.left, result)
        dfs_binary_tree(node.right, result)
    return result


class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_edge(self, source, destination):
        if source not in self.adj_list:
            self.adj_list[source] = []
        self.adj_list[source].append(destination)

    def bfs_graph(self, start_node):
        visited = set()
        queue = deque([start_node])
        visited.add(start_node)
        result = []

        while queue:
            current = queue.popleft()
            result.append(current)

            for neighbor in self.adj_list.get(current, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        print("Graph BFS:", " -> ".join(result))

    def dfs_graph(self, start_node):
        visited = set()
        result = []

        def dfs_helper(current):
            visited.add(current)
            result.append(current)

            for neighbor in self.adj_list.get(current, []):
                if neighbor not in visited:
                    dfs_helper(neighbor)

        dfs_helper(start_node)
        print("Graph DFS:", " -> ".join(result))



if __name__ == "__main__":
    print("=== ASSESSMENT 3.3: NON-LINEAR DATA STRUCTURE (PYTHON) ===")
    print("Name: Rosalita, Roshelle Mea C. | BSIT-2C | CC104\n")

    # --- BINARY TREE SETUP ---
    root = TreeNode('R')
    root.left = TreeNode('O')
    root.right = TreeNode('S')

    root.left.left = TreeNode('A')
    root.left.right = TreeNode('L')

    root.left.left.left = TreeNode('A')  # Level 3 child of A

    root.right.left = TreeNode('I')
    root.right.right = TreeNode('T')

    print("--- BINARY TREE TRAVERSALS ---")
    bfs_binary_tree(root)
    tree_dfs_res = dfs_binary_tree(root)
    print("Binary Tree DFS:", " -> ".join(tree_dfs_res))
    print()

    g = Graph()
    g.add_edge('R', 'O')
    g.add_edge('R', 'S')
    g.add_edge('R', 'A')

    g.add_edge('O', 'I')
    g.add_edge('O', 'A')  # second A

    g.add_edge('S', 'T')

    g.add_edge('A', 'S')
    g.add_edge('A', 'L')

    print("--- GRAPH TRAVERSALS ---")
    g.bfs_graph('R')
    g.dfs_graph('R')