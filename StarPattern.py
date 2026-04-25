n=int(input("Enter the number of rows: "))
for i in range(1, n+1):
    print('* ' * i)

for i in range(1, n+1):
    for j in range(n-i):
        print(' ', end='')
    for k in range(2*i-1):
        print('*', end='')
    print()

for i in range(1, n+1):
    for j in range(1, n+1):
        if i==1 or i==n or j==1 or j==n:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()

def print_reverse_pattern(n):
    for i in range(1, n+1):
        print('* '* (n-i+1))

print_reverse_pattern(n)