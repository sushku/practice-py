def is_multiple(n, m):
    if n // m == n / m:
        return True
    else:
        return False

a = 10
b = 5
assert(a == int(a))
assert(b == int(b) and b != 0)
print(is_multiple(a, b))
