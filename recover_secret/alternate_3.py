import collections, functools, itertools


def recover_secret(triplets):
    """triplets is a list of triplets from the secret string. Return the string."""

    # Build a reverse directed graph of letters
    graph = Graph()
    for triplet in triplets:
        for i, j in pairwise(triplet):
            graph[i].goes_to(graph[j])

    # Pop off orphan letters one-by-one to form the word
    cardinality = lambda node: len([p for p in node.parents if p.value in graph])
    getnext = functools.partial(min, graph.values(), key=cardinality)
    word = (graph.pop(getnext().value).value for i in range(len(graph)))

    return ''.join(word)


class Graph(collections.defaultdict):
    """A graph that autocreates nodes"""

    def __missing__(self, key):
        self[key] = Node(key)
        return self[key]


class Node(object):
    """A directed graph node that knows its parents"""

    def __init__(self, value):
        self.value = value
        self.parents = []

    def goes_to(self, child):
        child.parents.append(self)


def pairwise(iterable):
    """Iterates through an iterable in pairs [a,b,c,d] --> ( [a,b], [b,c], [c,d] )"""
    a, b = itertools.tee(iterable)
    next(b, None)
    return zip(a, b)
