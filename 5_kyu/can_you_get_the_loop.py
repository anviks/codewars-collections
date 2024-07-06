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


def main():
    from util_funcs import pretty_compare
    
    node1 = Node()
    node2 = Node()
    node3 = Node()
    node4 = Node()
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2
    pretty_compare(loop_size(node1), 3)

    # Make a longer chain with a loop of 29
    nodes = [Node() for _ in range(50)]
    for node, next_node in zip(nodes, nodes[1:]):
        node.next = next_node
    nodes[49].next = nodes[21]
    pretty_compare(loop_size(nodes[0]), 29)


if __name__ == '__main__':
    main()
