from math import pi, radians, degrees, sin, cos, tan, asin, e, exp, log, ceil, floor, trunc
from random import random, seed, randrange, randint, choice, sample

# Probando las funciones del modulo 'math'
ad = 90
ar = radians(ad)
ad = degrees(ar)
x = 1.4
y = 2.6

print(ad == 90.)
print(ar == pi / 2.)
print(sin(ar) / cos(ar) == tan(ar))
print(asin(sin(ar)) == ar)
print(pow(e, 1) == exp(log(e)))
print(pow(2, 2) == exp(2 * log(2)))
print(log(e, e) == exp(0))
print(floor(x), floor(y))
print(floor(-x), floor(-y))
print(ceil(x), ceil(y))
print(ceil(-x), ceil(-y))
print(trunc(x), trunc(y))
print(trunc(-x), trunc(-y))

# Probando la funcion 'random()'
for i in range(5):
    print((random()))

seed(0)
for i in range(5):
    print(random())

# Probando las funciones 'randrange()' y 'randint()'
print(randrange(1), end=' ')
print(randrange(0, 1), end=' ')
print(randrange(0, 1, 1), end=' ')
print(randint(0, 1))

for i in range(10):
    print(randint(1, 10), end=',')
print()


# Probando las funciones 'choise()' y 'sample()'
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(choice(my_list))
print(sample(my_list, 5))
print(sample(my_list, 10))

