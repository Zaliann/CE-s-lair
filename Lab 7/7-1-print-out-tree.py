def creating_tree(n):
    """
    Данная функция создаёт словарь из поступающих на вход элементов дерева
    :param n: количество сообщений
    :return: словарь
    """

    tree = {}

    for i in range(n):
        leaf, root = [int(x) for x in input().split()]
        if root not in tree:
            tree[root] = []
        tree[root] += [leaf]
        tree[root].sort()


    return tree


def print_out_tree(tree, curr_level, curr_elem):
    """
    Данная функция выводит дерево
    :param tree: дерево
    :param curr_elem: элемент, который мы печатаем
    :param curr_level: уровень, на котором мы находимся в конкретный момент времени
    :return:
    """
    '''
    if curr_elem != 0:
        print(curr_elem)
    '''
    if curr_elem not in tree:
        return

    for i in range(len(tree[curr_elem])):
        print('**' * curr_level + str(tree[curr_elem][i]))
        print_out_tree(tree, curr_level + 1, tree[curr_elem][i])


# основная программа
tree = creating_tree(int(input()))
print_out_tree(tree, 0, 0)