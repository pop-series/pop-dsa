from collections import deque


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def preOrder(root):
    curr = root
    while curr:
        if curr.left:
            predecessor = curr.left
            while predecessor.right and predecessor.right != curr:
                predecessor = predecessor.right
            if not predecessor.right:
                print(curr.data, end=', ')
                predecessor.right = curr
                curr = curr.left
                continue
            predecessor.right = None
        else:
            print(curr.data, end=', ')
        curr = curr.right

def postOrder(root):
    buf = deque()
    curr = root
    while curr:
        if curr.right:
            predecessor = curr.right
            while predecessor.left and predecessor.left != curr:
                predecessor = predecessor.left
            if not predecessor.left:
                buf.append(curr.data)
                predecessor.left = curr
                curr = curr.right
                continue
            predecessor.left = None
        else:
            buf.append(curr.data)
        curr = curr.left
    for val in reversed(buf):
        print(val, end=', ')

def inOrder(root):
    curr = root
    while curr:
        if curr.left:
            predecessor = curr.left
            while predecessor.right and predecessor.right != curr:
                predecessor = predecessor.right
            if not predecessor.right:
                predecessor.right = curr
                curr = curr.left
                continue
            predecessor.right = None
        print(curr.data, end=', ')
        curr = curr.right

if __name__ == '__main__':
    troot = Node(
        8,
        Node(11,
            None,
            Node(13,
                Node(12,
                    Node(1, Node(23), None),
                    Node(6, None, Node(71))
                ),
                Node(90, Node(4), None)
            )
        ),
        Node(6,
            Node(15),
            Node(20, None, Node(17))
        )
    )

    exp_preOrder = [8, 11, 13, 12, 1, 23, 6, 71, 90, 4, 6, 15, 20, 17]
    print('preOrder (exp, actual)')
    print(exp_preOrder)
    preOrder(troot), print('')

    exp_postOrder = [23, 1, 71, 6, 12, 4, 90, 13, 11, 15, 17, 20, 6, 8]
    print('postOrder (exp, actual)')
    print(exp_postOrder)
    postOrder(troot), print('')

    exp_inOrder = [11, 23, 1, 12, 6, 71, 13, 4, 90, 8, 15, 6, 20, 17]
    print('inOrder(exp, actual)')
    print(exp_inOrder)
    inOrder(troot), print('')
