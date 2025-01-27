import copy

x = [1,2,3,4]
y = copy.deepcopy(x)
# y = x

print(id(x) == id(y))
print(id(y))