# O(n)
# Here the Big O is described as a linear function O = n
def print_items(n):
    for i in range(n):
        print(i)


print_items(10)


# We can add a multiplayer so the linear function is O = 2n, but that doesn't matter, what matters is the tendency of O
def print_items_2(n):
    for i in range(n):
        print(i)

    for j in range(n):
        print(j)


print_items(10)
print_items_2(10)
