a = "PythonString"
print(a)
print(*a)

*f, = "PythonString"  # The comma matters!
print(f)

b, *c, d = [2, 3, 8, 7]
print(b, c, d)
