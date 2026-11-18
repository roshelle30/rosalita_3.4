class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


root = Node('R')

root.left = Node('O')
root.right = Node('S')

root.left.left = Node('H')
root.left.right = Node('E')

root.left.left.left = Node('L')

root.right.left = Node('L')
root.right.right = Node('E')

def get_preorder(node, result=[]):
    if node:
        result.append(str(node.data))
        get_preorder(node.left, result)
        get_preorder(node.right, result)
    return result

def get_inorder(node, result=[]):
    if node:
        get_inorder(node.left, result)
        result.append(str(node.data))
        get_inorder(node.right, result)
    return result

def get_postorder(node, result=[]):
    if node:
        get_postorder(node.left, result)
        get_postorder(node.right, result)
        result.append(str(node.data))
    return result

pre_res = ", ".join(get_preorder(root, []))
in_res = ", ".join(get_inorder(root, []))
post_res = ", ".join(get_postorder(root, []))

print("+---------------------------------------+")
print("|          DFS METHODS IN TREE          |")
print("+---------------------------------------+")
print("| Preorder Traversal:                   |")
print(f"| {pre_res:<37} |")
print("|                                       |")
print("| Inorder Traversal:                    |")
print(f"| {in_res:<37} |")
print("|                                       |")
print("| Postorder Traversal:                  |")
print(f"| {post_res:<37} |")
print("+---------------------------------------+")