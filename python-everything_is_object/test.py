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

s1="best School"
s2= s1
print(s1 is s2)

print(s1 is s2)


s1 = "Best School"
s2 = "Best School"
print(s1 is s2)

l1 = [1, 2, 3]
l2 = [1, 2, 3] 
print(l1 == l2)


l1 = [1, 2, 3]
l2 = [1, 2, 3] 
print(l1 is l2)


l1 = [1, 2, 3]
l2 = l1
print(l1 == l2)

l1 = [1, 2, 3]
l2 = l1
print(l1 is l2)

l1 = [1, 2, 3]
l2 = l1
l1.append(4)
print(l2)

l1 = [1, 2, 3]
l2 = l1
l1 = l1 + [4]
print(l2)
