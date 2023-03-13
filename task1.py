variable1 = variable2 = variable3 = 'Python 2023'
print(variable1 == variable2)
print(variable2 == variable3)
print(type(variable1), ' ', hex(id(variable1)))
print(type(variable2), ' ', hex(id(variable2)))
print(type(variable3), ' ', hex(id(variable3)))
variable3 = 'Java 11'
print(variable1 == variable2)
print(variable2 == variable3)
print(type(variable1), ' ', hex(id(variable1)))
print(type(variable2), ' ', hex(id(variable2)))
print(type(variable3), ' ', hex(id(variable3)))
