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

def is_ancestor(tree, ancestor, descendant):
    """
    Данная функция определяет является ли сообщение ancestor предком descendant
    :param tree: дерево
    :param ancestor: сообщение-предок
    :param descendant: сообщение-потомок
    :return: отвечает на вопрос: "Является ли предком?"
    """
    if descendant == ancestor:
        return True
    if tree[descendant] == 0:
        return False
    return is_ancestor(tree, ancestor, tree[descendant])

# основная программа
tree = creating_reversed_tree(int(input()))

anc, des = [int(x) for x in input().split()]
print('YES' if is_ancestor(tree, anc, des) else 'NO')