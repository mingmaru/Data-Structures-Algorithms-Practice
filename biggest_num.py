def make_tree():

    num=[37, 29, 69, 30, 15, 55, 90, 87, 73, 20]

    in_d=0

    root=Node(num[0])

    for i in range(1,len(num)):
        v = num[i]
        w_node = root

        while w_node != None:
            if w_node.data < v:
                if w_node.righ == None:
                    child = Node(v)
                    w_node.right = child
                    w_node = None
                else:
                    w_node = w_node.right

            else:
                if w_node.left == None:
                    child = Node(v)
                    w_node.left = child
                    w_node = None
                else:
                    w_node = w_node.left


def search_right_only(node, level, ans):
    ans.append(node.data)

    if node.right != None:
        search_right_only(node.right, level+1, ans)