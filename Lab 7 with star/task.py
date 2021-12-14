def find_variants(matrix, x0, y0):
    variants = []
    for dx in [-1, 1, -2, 2]:
        for dy in [-1, 1, -2, 2]:
            if abs(dx) == abs(dy):
                continue
            x = x0 - dx
            y = y0 - dy
            if 0 <= x < len(matrix[0]) and 0 <= y < len(matrix):
                if matrix[y][x] == 0:
                    variants.append((x, y))

    return variants


def score(matrix, x_new, y_new):
    return -len(find_variants(matrix, x_new, y_new))


def score_variant(m, n, x, y, x_new, y_new):

    quarter = 0
    if x <= n // 2:
        if y <= m // 2:
            quarter = 3
        else:
            quarter = 2
    else:
        if y <= m // 2:
            quarter = 4
        else:
            quarter = 1
    #print(quarter)
    if quarter == 1:
        return x - x_new
    elif quarter == 2:
        return y - y_new
    elif quarter == 3:
        return x_new - x
    else:
        return y_new - y


def fill_matrix(matrix, x, y, n_steps):
    if n_steps == len(matrix) * len(matrix[0]):
        return True

    variants = find_variants(matrix, x, y)

    if not variants:
        return False

    variants.sort(
        key=lambda variant: (score(matrix, *variant), score_variant(len(matrix), len(matrix[0]), x, y, *variant)),
        reverse=True)
    #print(x, y, '-- position', *variants)
    for x_new, y_new in variants:
        matrix[y_new][x_new] = n_steps + 1
        #print(*matrix, sep='\n')
        if not fill_matrix(matrix, x_new, y_new, n_steps + 1):
            matrix[y_new][x_new] = 0
        else:

            return True

    return False


def create_matrix(m, n, x_start, y_start):
    matrix = [[0 for x in range(n)] for y in range(m)]
    matrix[y_start][x_start] = 1
    if not fill_matrix(matrix, x_start, y_start, 1):
        return None
    return matrix


def print_table(res):
    f = open("output.txt", 'w')
    max_len = len(str(len(res) * len(res[0])))
    for i in reversed(range(len(res))):
        for j in range(len(res[0])):
            f.write(' ' * (max_len - len(str(res[i][j]))) + str(res[i][j]))
        f.write('\n')
    f.close()


def main():
    f = open("input.txt", 'r')
    m, n = (int(x) for x in f.readline().split())
    x, y = [int(x) - 1 for x in f.readline().split()]
    f.close()
    res = create_matrix(m, n, x, y)
    if res is None:
        f = open("output.txt", 'w')
        f.write('Маршрут не существует')
    else:
        print_table(res)
        for row in reversed(res):  # for i in range(5, -1, -1)   (for i in reversed(range(0, 6)))
            print(*(f'{x:3}' for x in row))


if __name__ == '__main__':
    main()

