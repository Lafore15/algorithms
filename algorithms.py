import datastructures
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


# merge sort
def merge(l1, l2):
    result = []
    length1, length2 = len(l1), len(l2)
    i, j = 0, 0
    while i < length1 and j < length2:
        if l1[i] < l2[j]:
            result.append(l1[i])
        else:
            result.append((l2[j]))
    if i < length1:
        result += l1[i:]
    if j < length2:
        result += l2[j:]
    return result


def merge_sort(l):
    length = len(l)
    if length <= 1:
        return l
    mid = length // 2
    left = merge_sort(l[:mid])
    right = merge_sort((l[mid:]))
    return merge(left, right)


# quick sort


def quicksort(values):
    qs(values, 0, len(values) - 1)
    return values


def qs(values, left, right):
    if left >= right:
        return
    p = partition(values, left, right)
    qs(values, left, p - 1)
    qs(values, p + 1, right)


def partition(values, left, right):
    pivot = values[right]
    i = left - 1
    for j in range(left, right):
        if values[j] < pivot:
            i += 1
            values[i], values[j] = values[j], values[i]
    values[i + 1], values[right] = values[right], values[i + 1]
    return i + 1


# pyramid sort(heap sort)

def swap(values, i, j):
    values[i], values[j] = values[j], values[i]


def pyramid_sort(values):
    for i in range(1, len(values)):
        index = i
        while index != 0:
            parent = (index - 1) // 2
            if values[index] <= values[parent]:
                break
            swap(values, index, parent)
            index = parent
    for i in range(len(values) - 1, 0, -1):
        swap(values, 0, i)
        index = 0
        while True:
            child1 = 2 * index + 1
            child2 = 2 * index + 2
            if child1 >= i:
                child1 = index
            if child2 >= i:
                child2 = index
            if values[child1] <= values[index] and values[child2] <= values[index]:
                break
            if values[child1] > values[child2]:
                swap_child = child1
            else:
                swap_child = child2
            swap(values, index, swap_child)
            index = swap_child
    return values


# Kraskal's algorithm

def runKraskal(edges: list[tuple], n: int):
    mst = []
    ds = datastructures.DisjointSet()
    ds.makeSet(edges)
    index = 0
    edges.sort(key=lambda x: x[2])
    while len(mst) != n - 1:
        src, dst, weight = edges[index]
        index += 1
        a, b = ds.find(src), ds.find(dst)
        if a != b:
            mst.append([src, dst, weight])
            ds.union(a, b)
    return mst