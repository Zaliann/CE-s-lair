import random


def bubble(list):
    n = len(list)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
    return list


def shell_method(list):
    inc = len(list) // 2
    while inc:
        for index, element in enumerate(list):
            while index >= inc and list[index - inc] > element:
                list[index] = list[index - inc]
                index -= inc
            list[index] = element
        inc = 1 if inc == 2 else int(inc * 5.0 / 11)
    return list


def fast(list):
    if len(list) <= 1:
        return list
    else:
        r = random.choice(list)
        s_nums = []
        m_nums = []
        e_nums = []
        for n in list:
            if n < r:
                s_nums.append(n)
            elif n > r:
                m_nums.append(n)
            else:
                e_nums.append(n)
        return fast(s_nums) + e_nums + fast(m_nums)


def check(list):
    for i in range(1, len(list)):
        if list[i - 1] > list[i]:
            return False
    return True