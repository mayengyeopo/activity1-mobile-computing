for i in range(1, 6):
    print('*' * i)

print()  # Empty line between patterns

# Reverse Triangle
for i in range(5, 0, -1):
    print('*' * i)

print()  # Empty line between patterns

# Diamond
for i in range(1, 6):
    print(' ' * (5 - i) + '*' * (2 * i - 1))

for i in range(4, 0, -1):
    print(' ' * (5 - i) + '*' * (2 * i - 1))