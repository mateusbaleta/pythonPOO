some_list = ['a','a','b','c','c','d','e']

duplicates = list(set([x for x in some_list if some_list.count(x) > 1]))

print(duplicates)