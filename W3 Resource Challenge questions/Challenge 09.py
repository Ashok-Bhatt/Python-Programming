# Challenge-8: Write a Python program to find missing numbers from a list (same as Challenge-7):

# Write a Python program to find three numbers from an array such that the sum of three numbers equal to zero.

array = [2,5,-1,1,-2,-3,0,4,-4]
possible_combination=[]

for i in array:
    for j in array:
        for k in array:
            if i+j+k==0:
                for x in (i,j,k):
                    for y in (i,j,k):
                        for z in (i,j,k):
                            if (x,y,z) not in possible_combination:
                                possible_combination.append((i,j,k))
            else:
                continue

print("The pairs of three number whose sum is zero is given by:")
for combinations in possible_combination:
    print(f"{combinations[0]},{combinations[1]} and {combinations[2]}")