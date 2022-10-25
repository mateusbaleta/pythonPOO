# Square
nums = [5,4,3]

square_nums = list(map(lambda x: x ** 2, nums))
print(square_nums)


# List sort
a = [(0,2), (4,3), (9,9), (10, -1)]

res = sorted(a, key = lambda x: x[1])
print(str(res))