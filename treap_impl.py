"""Treap — BST + heap hybrid with random priorities."""
import random

class Node:
    def __init__(self, key):
        self.key = key
        self.priority = random.random()
        self.left = self.right = None
        self.size = 1

def size(n): return n.size if n else 0
def update(n):
    if n: n.size = 1 + size(n.left) + size(n.right)

def split(n, key):
    if not n: return None, None
    if key < n.key:
        l, n.left = split(n.left, key)
        update(n); return l, n
    else:
        n.right, r = split(n.right, key)
        update(n); return n, r

def merge(l, r):
    if not l or not r: return l or r
    if l.priority > r.priority:
        l.right = merge(l.right, r); update(l); return l
    else:
        r.left = merge(l, r.left); update(r); return r

def insert(root, key):
    l, r = split(root, key)
    return merge(merge(l, Node(key)), r)

def inorder(n):
    if not n: return []
    return inorder(n.left) + [n.key] + inorder(n.right)

if __name__ == "__main__":
    random.seed(42)
    root = None
    for x in [5, 3, 8, 1, 4, 7, 9, 2, 6]:
        root = insert(root, x)
    result = inorder(root)
    print(f"Treap inorder: {result}")
    assert result == sorted(result)
    assert size(root) == 9
    print("All tests passed!")
