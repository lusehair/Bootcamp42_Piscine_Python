from vector import Vector

v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
v2 = v1 * 5
print(v1)

v1 = Vector([[0.0, 1.0, 2.0, 3.0]])
v2 = v1 * 5
print(v2)
print("this is v1", v1)

v2 = v1 / 2.0
print(v2)
# v1 / 0.0
#
print(Vector([[0.0], [1.0], [2.0], [3.0]]).shape)
print(Vector([[0.0], [1.0], [2.0], [3.0]]).values)
print(Vector([[0.0, 1.0, 2.0, 3.0]]).shape)
print(Vector([[0.0, 1.0, 2.0, 3.0]]).values)
v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
print(v1.shape)

v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
print(v1.shape)

print(v1.T())
print(v1.T().shape)

v2 = Vector([[0.0, 1.0, 2.0, 3.0]])
print(v2.shape)
print(v2.T())
print(v2.T().shape)

v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
v2 = Vector([[2.0], [1.5], [2.25], [4.0]])
print(v1.dot(v2))


v3 = Vector([[1.0, 3.0]])
v4 = Vector([[2.0, 4.0]])
print(v3.dot(v4))


v1 
#print(v1)
