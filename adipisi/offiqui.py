def my_generator():
    yield [1, 18, 0.0026713408791001632]

# Create an instance of the generator
gen = my_generator()

# Iterate over the values yielded by the generator
for value in gen:
    print(value)
