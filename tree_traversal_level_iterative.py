from collections import deque


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def topDown(root):
    if root is None: return
    buf = deque([root])
    while buf:
        curr = buf.popleft()
        print(curr.data, end=', ')
        if curr.left: buf.append(curr.left)
        if curr.right: buf.append(curr.right)

def bottomUp(root):
    if root is None: return
    buf = deque([root])
    idx, count = 0, 1
    while idx < count:
        curr = buf[idx]
        idx += 1
        if curr.right:
            buf.append(curr.right)
            count += 1
        if curr.left:
            buf.append(curr.left)
            count += 1
    for idx in range(count-1, -1, -1):
        print(buf[idx].data, end=', ')

def topSpiral(root):
    if root is None: return
    fwd_stack, bwd_stack = None, (root, None)
    while fwd_stack or bwd_stack:
        while bwd_stack:
            curr, bwd_stack = bwd_stack
            print(curr.data, end=', ')
            if curr.right: fwd_stack = curr.right, fwd_stack
            if curr.left: fwd_stack = curr.left, fwd_stack
        while fwd_stack:
            curr, fwd_stack = fwd_stack
            print(curr.data, end=', ')
            if curr.left: bwd_stack = curr.left, bwd_stack
            if curr.right: bwd_stack = curr.right, bwd_stack


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
    topSpiral(troot), print('')
