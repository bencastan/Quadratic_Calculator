import math


def header():
    print('------------------------')
    print('  QUADRATIC CALCULATOR')
    print('a^2 x + b -  4 (a)(c) = 0')
    print('------------------------')
    print('')


def get_values():
    """
    Gets the values for a, b & c
    :return: Tuple of the values of a, b , c
    """
    num_a = int(input(' Enter A '))
    num_b = int(input(' Enter B '))
    num_c = int(input(' Enter C '))
    print('')
    return num_a, num_b, num_c


def get_discriminant(a, b, c):
    """
    Generates the discriminant
    :param a: Value a
    :param b: Value b
    :param c: Value c
    :return: The Discriminant as an integer
    """
    d = b ** 2 - 4 * a * c  # discriminant
    return d


def one_solution(a, b, d):
    """

    :param a:
    :param b:
    :param d:
    :return:
    """
    x = (-b + math.sqrt(d)) / 2 * a
    return x


def two_solution(a, b, c, d):
    """

    :param a:
    :param b:
    :param c:
    :param d:
    :return:
    """
    x1 = (-b + math.sqrt((d))) / (2 * a)
    x2 = (-b - math.sqrt((d))) / (2 * a)
    return x1, x2


# ----Logic----
if __name__ == '__main__':
    header()
    num_a, num_b, num_c = get_values()
    d = get_discriminant(num_a, num_b, num_c)

    if d < 0:
        print('This equation has no real solution!')
    elif d == 0:
        print('This equation has one solution: {}'.format(one_solution(num_a, num_b, d)))
    else:
        x, y = two_solution(num_a, num_b, num_c, d)
        print('This equation has two solutions: {} or {}'.format(x, y))
