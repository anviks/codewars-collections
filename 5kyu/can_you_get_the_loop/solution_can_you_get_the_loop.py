"""https://www.codewars.com/kata/52a89c2ea8ddc5547a000863"""


class Node:
    next: 'Node'


def loop_size(node: Node) -> int:
    visited = set()

    while node not in visited:
        visited.add(node)
        node = node.next

    counter = 1
    loop_node = node.next

    while loop_node != node:
        loop_node = loop_node.next
        counter += 1

    return counter
