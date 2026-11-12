total = 0

for n in range(1, 51):
    if n % 3 == 0:
       continue

    print(n, end=" ")
    total += n

print()
print("Sum:", total)