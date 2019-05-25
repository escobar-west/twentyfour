from __future__ import print_function
from numpy import inf as INF
import itertools as it

def parse_tree(tree):
    """
    tree: a tree
    returns: numerical evaluation of tree
    ex: (((2,1,-),(2,4,+),*),18,+) will return 24
    """
    n0 = tree[0] if isinstance(tree[0], float) else parse_tree(tree[0])
    n1 = tree[1] if isinstance(tree[1], float) else parse_tree(tree[1])
    op = tree[2]
    if op == '+':
        return n0 + n1
    elif op == '-':
        return n0 - n1
    elif op == '*':
        return n0 * n1
    elif op == '/':
        if n1 != 0:
            return n0 / n1
        else:
            return INF

def add_op_nodes(L0, L1):
    """
    L0, L1: list of trees
    returns: list of all possible new tree combos
    """
    tree_list = []
    for x, y in it.product(L0, L1):
        tree_list.append((x, y, '+'))
        tree_list.append((x, y, '*'))
        tree_list.append((x, y, '-'))
        tree_list.append((y, x, '-'))
        tree_list.append((x, y, '/'))
        tree_list.append((y, x, '/'))

    return tree_list
    
def check_24(*args):
    """
    args: each argument is a list of trees
    returns: the thing you're looking for
    """
    res_list = []
    for L0, L1 in it.combinations(args, 2):
        branches = add_op_nodes(L0, L1)
        sub_args = list(args)
        sub_args.remove(L0)
        sub_args.remove(L1)
        sub_args.append(branches)
        if len(sub_args) >= 2:
            res_list.extend(check_24(*sub_args))
        else:
            return [branch for branch in branches if parse_tree(branch) == 24]
    return list(set(res_list))


if __name__ == '__main__':
    res = check_24([167.0],[1.0],[7.0],[7.0])
    for r in res:
        print(r)
    
