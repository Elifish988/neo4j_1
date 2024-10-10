def my_generator():
    for i in range(5):
        print('hi')
        yield i
        print('by')

gen = my_generator()

print(next(gen))
print(next(gen))
print(next(gen))

