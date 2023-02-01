import sys
readline = sys.stdin.readline

preorder_res = ""
def preorder_traversal(node):
    global graph, preorder_res
    left, right = graph[node]
    preorder_res += node
    if left != '.': preorder_traversal(left)
    if right != '.': preorder_traversal(right)

inorder_res = ""
def inorder_traversal(node):
    global graph, inorder_res
    left, right = graph[node]    
    if left != '.': inorder_traversal(left)
    inorder_res += node
    if right != '.': inorder_traversal(right)    

postorder_res = ""
def postorder_traversal(node):
    global graph, postorder_res
    left, right = graph[node]    
    if left != '.': postorder_traversal(left)
    if right != '.': postorder_traversal(right)
    postorder_res += node

N = int(readline())
graph = {chr(c):list() for c in range(ord('A'), ord('A') + N)}
for _ in range(N):
    parent, *childs = readline().split()
    graph[parent] = childs
preorder_traversal('A')
inorder_traversal('A')
postorder_traversal('A')
print(preorder_res, inorder_res, postorder_res, sep='\n')