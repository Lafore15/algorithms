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
        cur_vertex = deque.popleft()
        print(cur_vertex)
        if cur_vertex.left:
            deque.append(cur_vertex.left)
        if cur_vertex.right:
            deque.append(cur_vertex.right)
    return True

# for graphs


