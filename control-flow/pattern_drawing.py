length = int(input("Enter the size of the pattern: "))

i = 0

while i < length:
    print("*", end="")
    j = 1
    while j < length:
        print("*", end="")
        j = j + 1
    i = i + 1
    print()  
