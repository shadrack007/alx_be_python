size = int(input("Enter the size of the pattern: "))

if size <= 0:
    print("Size must be a positive integer.")
    exit()

row = 0

while row < size:
    for col in range(size):
        print("*", end=" ")
    print()
    row += 1




