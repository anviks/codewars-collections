"""https://www.codewars.com/kata/52a89c2ea8ddc5547a000863"""

import unittest

from solution import Node, loop_size


def create_chain(tail_size, loop_size_):
    prev_node = Node()
    start = prev_node
    start.next = start
    if loop_size_ > 1:
        for _ in range(tail_size):
            prev_node.next = Node()
            prev_node = prev_node.next
        end_loop = prev_node
        for _ in range(loop_size_ - 1):
            prev_node.next = Node()
            prev_node = prev_node.next
        prev_node.next = end_loop
    return start


class FixedTests(unittest.TestCase):
    def test_simple_cases(self):
        node1 = Node()
        node2 = Node()
        node3 = Node()
        node4 = Node()
        node1.next = node2
        node2.next = node3
        node3.next = node4
        node4.next = node2
        self.assertEqual(loop_size(node1), 3, 'Loop size of 3 expected')

        # Make a longer chain with a loop of 29
        nodes = [Node() for _ in range(50)]
        for node, next_node in zip(nodes, nodes[1:]):
            node.next = next_node
        nodes[49].next = nodes[21]
        self.assertEqual(loop_size(nodes[0]), 29, 'Loop size of 29 expected')

        # Make a very long chain with a loop of 1087
        chain = create_chain(3904, 1087)
        self.assertEqual(loop_size(chain), 1087, 'Loop size of 1087 expected')
