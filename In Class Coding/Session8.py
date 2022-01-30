from copy import deepcopy


var = [1, 2, 3, 4, [1, 2, 3, 4]]
# var2 = [5, 6, 7, 8]
# var2.extend(var)
# print(var2)
# var2.sort()
# print(var2)


varx = deepcopy(var)
varx.append(5)
print(varx)
print(var)