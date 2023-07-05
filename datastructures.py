

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = Node()

    def append(self, data):
        new_node = Node(data)
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = new_node

    def length(self):
        length = 0
        cur = self.head
        while cur.next is not None:
            length += 1
            cur = cur.next
        return length

    def display(self):
        elems = []
        cur = self.head
        while cur.next is not None:
            cur = cur.next
            elems.append(cur.data)
        return elems

    def find_cell(self, target_data):
        cur = self.head
        while cur.next is not None:
            if cur.next.data == target_data:
                return True
            cur = cur.next
        return False

    def get(self, index):
        if index >= self.length():
            return None
        cur_index = 0
        cur = self.head
        while True:
            cur = cur.next
            if cur_index == index:
                return cur.data
            cur_index += 1

    def erase(self, index):
        if index >= self.length():
            return
        cur_index = 0
        cur_node = self.head
        while True:
            last_node = cur_node
            cur_node = cur_node.next
            if cur_index == index:
                last_node.next = cur_node.next
                return
            cur_index += 1

    def add(self, after_me_index, data):
        if after_me_index >= self.length():
            return None
        after_me_data = self.get(after_me_index)
        new_node = Node(data)
        cur_node = self.head
        while True:
            if cur_node.next.data == after_me_data:
                new_node.next, cur_node.next = cur_node.next, new_node
                return
            else:
                cur_node = cur_node.next


class DisjointSet:
    parent = {}

    # perform MakeSet operation
    def makeSet(self, n):
        # create `n` disjoint sets (one for each vertex)
        for i in range(n):
            self.parent[i] = i

    # Find the root of the set in which element `k` belongs
    def find(self, k):
        # if `k` is root
        if self.parent[k] == k:
            return k

        # recur for the parent until we find the root
        return self.find(self.parent[k])

    # Perform Union of two subsets
    def union(self, a, b):
        # find the root of the sets in which elements `x` and `y` belongs
        x = self.find(a)
        y = self.find(b)

        self.parent[x] = y
