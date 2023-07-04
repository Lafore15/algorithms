# binary search
def binary_search(values, target):
    # values = sorted(values)
    left = 0
    right = len(values) - 1
    while left <= right:
        mid = (left + right) // 2
        if values[mid] == target:
            return mid
        elif values[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


#   bfs algorithms

# for binary tree

def bfs(root):
    from collections import deque
    deque = deque()
    deque.append(root)
    while deque:
        cur_node = deque.popleft()
        print(cur_node)
        if cur_node.left:
            deque.append(cur_node.left)
        if cur_node.right:
            deque.append(cur_node.right)
    return True

# for graphs


def bfs_2(graph, node):
    from collections import deque
    deque = deque([node])
    visited = set()
    while deque:
        cur_node = deque.popleft()
        print(cur_node)
        for neighbour in graph[cur_node]:
            if neighbour not in visited:
                deque.append(neighbour)
                visited.add(neighbour)
    return True


#   dfs algorithms


# for binary tree

def dfs(root):
    stack = [root]
    while stack:
        cur_node = stack.pop()
        if cur_node:
            print(cur_node)
            stack.append(cur_node.right)
            stack.append(cur_node.left)
    return True


# for graphs


def dfs_2(graph, node):
    visited = set()
    stack = [node]
    while stack:
        cur_node = stack.pop()
        stack.append(cur_node)
        visited.add(cur_node)
        for neighbour in graph[cur_node]:
            if neighbour not in visited:
                stack.append(neighbour)
    return True




