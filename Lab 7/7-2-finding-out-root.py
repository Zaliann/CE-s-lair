def creating_reversed_tree(n):
    """
    Данная функция создаёт словарь из поступающих на вход элементов дерева.
    Нюанс данной функции в том, что она создаёт словарь, в котором указывается
    предок листочка.
    :param n: количество сообщений
    :return: словарь
    """

    tree = {}

    for i in range(n):
        leaf, root = [int(x) for x in input().split()]
        tree[leaf] = root

    return tree


def find_out_root(tree, a):
    """
    Данная функция выводит номер корневого сообщения для темы,
    в которой находится сообщение а
    :param tree: дерево
    :param a: искомое сообщение
    :return: корень
    """

    if tree[a] == 0:
        return a
    return find_out_root(tree, tree[a])
# основная программа
d = creating_reversed_tree(int(input()))
#print(d)
f = int(input())
res = find_out_root(d, f)
print(res)
