class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def preOrder(root):
    if root is None:
        return
    print(root.data, end=', ')
    preOrder(root.left)
    preOrder(root.right)

def postOrder(root):
    if root is None:
        return
    postOrder(root.left)
    postOrder(root.right)
    print(root.data, end=', ')

def inOrder(root):
    if root is None:
        return
    inOrder(root.left)
    print(root.data, end=', ')
    inOrder(root.right)


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
