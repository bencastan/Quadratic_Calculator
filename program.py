
import math

print('Quadratic equation calculator')
print('a^2 x + b -  4 (a)(c) = 0')

num_a = int(input(' Enter A '))
num_b = int(input(' Enter B '))
num_c = int(input(' Enter C '))

d = num_b**2 - 4*num_a*num_c # discriminant

if d < 0:
    print('This equation has no real solution!')
elif d == 0:
    x = (-num_b + math.sqrt(d)) / 2 * num_a
    print('This equation has one solution: ', x)
else:
    x1 = (-num_b+math.sqrt((d))) / (2 * num_a)
    x2 = (-num_b-math.sqrt((d))) / (2 * num_a)

    print('This equation has two solutions: {} or {}'.format(str(x1), str(x2)))


