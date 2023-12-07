"""A long time ago in a galaxy far, far away..."""

anakin = 'Hello There'
print(anakin)
print(id(anakin))

darth_vader = anakin
print(darth_vader)
print(id(darth_vader))

del anakin

print(darth_vader)
print(id(darth_vader))

del darth_vader
