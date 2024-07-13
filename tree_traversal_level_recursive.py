class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def topDown(*roots):
    children = []
    for root in roots:
        if root is None: continue
        print(root.data, end=', ')
        children.append(root.left)
        children.append(root.right)
    if children: topDown(*children)

def bottomUp(*roots):
    children = []
    for root in roots:
        if root is None: continue
        children.append(root.left)
        children.append(root.right)
    if children: bottomUp(*children)
    for root in roots:
        if root is None: continue
        print(root.data, end=', ')

def topSpiral(roots, flip=1):
    children = []
    for root in reversed(roots):
        if root is None: continue
        print(root.data, end=', ')
        if flip:
            children.append(root.right)
            children.append(root.left)
        else:
            children.append(root.left)
            children.append(root.right)
    if children: topSpiral(children, flip^1)


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

    exp_topDown = [8, 11, 6, 13, 15, 20, 12, 90, 17, 1, 6, 4, 23, 71]
    print('topDown (exp, actual)')
    print(exp_topDown)
    topDown(troot), print('')

    exp_bottomUp = [23, 71, 1, 6, 4, 12, 90, 17, 13, 15, 20, 11, 6, 8]
    print('bottomUp (exp, actual)')
    print(exp_bottomUp)
    bottomUp(troot), print('')

    exp_topSpiral = [8, 11, 6, 20, 15, 13, 12, 90, 17, 4, 6, 1, 23, 71]
    print('topSpiral(exp, actual)')
    print(exp_topSpiral)
    topSpiral([troot]), print('')
