def calculate_y(a, b, X):
    return [(x, a**2 * x + b) for x in range(X + 1)]

a = float(input("a : "))
b = float(input("b : "))
X_max = int(input("Max: "))

results = calculate_y(a, b, X_max)

for x, y in results:
    print(f"{int(a)}^{int(a)}x{x}+{int(b)} =", y)