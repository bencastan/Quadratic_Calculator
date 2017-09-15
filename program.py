
import math

print('Quadratic equation calculator')
print('a^2 x + b -  4 (a)(c) = 0')

num_a = int(input(' Enter A '))
num_b = int(input(' Enter B '))
num_c = int(input(' Enter C '))

d = num_b**2 - 4*num_a*num_c # discriminant


def one_solution(a, b, d):
    x = (-b + math.sqrt(d)) / 2 * a
    return x


def two_solution(a, b, c, d):
    x1 = (-b+math.sqrt((d))) / (2 * a)
    x2 = (-b-math.sqrt((d))) / (2 * a)
    return x1, x2


if d < 0:
    print('This equation has no real solution!')
elif d == 0:
    print('This equation has one solution: {}' .format(one_solution(num_a, num_b, d)))
else:
    x, y = two_solution(num_a, num_b, num_c, d)
    print('This equation has two solutions: {} or {}'.format(x, y))


