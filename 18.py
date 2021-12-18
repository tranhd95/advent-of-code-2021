from __future__ import annotations

from ast import literal_eval
from dataclasses import dataclass
from itertools import chain, pairwise, product
from math import ceil, floor

from utils import iter_lines, rinput


def first(it, pred):
    return next(filter(pred, it), None)


@dataclass
class Node:
    value: int
    depth: int
    left: Node
    right: Node
    parent: Node

    def explode(self, root):
        if pred := get_pred(root, self.left):
            pred.value += self.left.value
        if succ := get_succ(root, self.right):
            succ.value += self.right.value
        self.value = 0
        self.left, self.right = None, None

    def split(self):
        half = self.value / 2.0
        self.value = None
        self.left = Node(floor(half), self.depth + 1, None, None, self)
        self.right = Node(ceil(half), self.depth + 1, None, None, self)

    def __add__(self, other):
        if not other:
            return self
        new_root = Node(None, 0, self, other, None)
        self.parent, other.parent = new_root, new_root
        for n in chain(preorder(self), preorder(other)):
            n.depth += 1
        return reduce(new_root)


def get_pred(root, source):
    return next(
        (fst for fst, snd in pairwise(preorder_vals(root)) if snd is source), None
    )


def get_succ(root, source):
    return next(
        (snd for fst, snd in pairwise(preorder_vals(root)) if fst is source), None
    )


def preorder_vals(node):
    for node in preorder(node):
        if node.value is not None:
            yield node


def preorder(node):
    if node:
        yield node
        yield from preorder(node.left)
        yield from preorder(node.right)


def reduce(root):
    while explodable := first(preorder(root), is_explodable):
            explodable.explode(root)
            
    if splittable := first(preorder(root), is_splitable):
        splittable.split()
        reduce(root)

    return root


def is_explodable(node):
    return (
        node.depth >= 4
        and node.left
        and node.right
        and node.left.value is not None
        and node.right.value is not None
    )


def is_splitable(node):
    return node.value is not None and node.value >= 10


def parse(inp, depth=0):
    node = Node(None, depth, None, None, None)
    if isinstance(inp, int):
        node.value = inp
        return node
    node.left = parse(inp[0], depth + 1)
    node.right = parse(inp[1], depth + 1)
    node.left.parent = node
    node.right.parent = node
    return node


def magnitude(node):
    if node and node.value is not None:
        return node.value
    return 3 * magnitude(node.left) + 2 * magnitude(node.right)


def solve1(inp):
    trees = map(parse, map(literal_eval, iter_lines(inp)))
    return magnitude(sum(trees, next(trees)))


def solve2(inp):
    trees = list(map(literal_eval, iter_lines(inp)))
    largest = -1
    for fst, snd in product(trees, trees):
        fst, snd = parse(fst), parse(snd)
        largest = max(largest, magnitude(fst + snd))
    return largest


print(solve1(rinput(18)))
print(solve2(rinput(18)))
