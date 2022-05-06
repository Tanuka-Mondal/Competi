def my_gen():
    n = 1
    yield n
    n += 1
    yield n
    n += 1
    yield n

a = my_gen()
print(next(a))
print(next(a))
print(next(a))    