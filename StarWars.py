anakin = 'Hello There'
print(anakin)
print(id(anakin))
darthvader = anakin
print(darthvader)
print(id(darthvader))
del anakin
print(darthvader)
print(id(darthvader))