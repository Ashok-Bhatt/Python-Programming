# Below code will break both loops
# Output: 1 2 3 4 (in new line)

for i in range(5):
    for j in range(5):
        print((i+1)*(j+1))
        if j==3:
            break
    break