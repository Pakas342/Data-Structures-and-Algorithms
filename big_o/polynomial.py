# O(n^k)
# Now, an polynomial big O will be something like O = n^2. In this example O = n + n^2
def print_numbers(n):
    for i in range(n):
        print(i)
        for j in range(n):
            print(i, j)


print_numbers(10)
