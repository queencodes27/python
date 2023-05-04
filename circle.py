in_line = 0
per_line = []

circle = int(input('Enter the circle of the circle: '))

# You must account for the loops being zero-based, but the quotient of the circle / 2 being
# one-based. If you use the exact radius, you will be short one column and one row.
n = (circle / 2) - 0.5

for i in range(circle):
    for j in range(circle):
        x = i - n
        y = j - n
        if x * x + y * y <= n * n + 1:
            print('*', end='  ')
            in_line += 1
        else:
            print(' ', end='  ')
    per_line.append(in_line)
    in_line = 0
    print()

print('The pixels per line are {0}.'.format(per_line))