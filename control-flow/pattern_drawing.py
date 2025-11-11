size = int(input("Enter the size of the pattern:"))

#initializes the row counter
i = 1

while i <= size:
    for col in range(size):
        print("*", end="")# prints stars side by side

    print()

    i +=1