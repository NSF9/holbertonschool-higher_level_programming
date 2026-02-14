a = 89
b = 90
print(type(a))

print(id(a))

print(id(b))

print(a is b)

b=a
print(a is b)

print(id(a), id(b))

b = a+1
print(id(a), id(b))