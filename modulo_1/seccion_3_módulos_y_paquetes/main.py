from sys import path


path.append('..\\modules')


from module import suml, prod1


zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]

print(suml(zeroes))
print(prod1(ones))
