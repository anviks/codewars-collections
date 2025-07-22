# [Sort binary tree by levels](https://www.codewars.com/kata/52bef5e3588c56132c0003bc)

You are given a binary tree:

```csharp
public class Node
{
    public Node Left;
    public Node Right;
    public int Value;
    
    public Node(Node l, Node r, int v)
    {
        Left = l;
        Right = r;
        Value = v;
    }
}
```
```c
typedef struct Tree {
	struct Tree *left, *right;
	int value;
} Tree;
```
Your task is to return the list with elements from tree sorted by levels, which means the root element goes first, then root children (from left to right) are second and third, and so on.

Return empty list if root is 'null'.
Return empty array if root is `null`.
Set `tree_size` to `0` if root is `NULL`.
Return empty list if root is `Leaf`.

Please also provide `foldr` for your chosen list encoding. Purity is `LetRec`.
Inputs will always contain at least one node.

Example 1 - following tree:

                     2
                8        9
              1  3     4   5

Should return following list:

    [2,8,9,1,3,4,5]

Example 2 - following tree:

                     1
                8        4
                  3        5
                             7
Should return following list:

    [1,8,4,3,5,7]
    
**Note**: A `Node`'s tree can be displayed via Debug:
`println!("{:?}", node)`