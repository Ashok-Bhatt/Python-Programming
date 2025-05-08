
def solve(haystack, needle):
    last_index = len(haystack) - len(needle) + 1
            
    for i in range(last_index):
        
        j = 0
        while (j<len(needle) and haystack[i+j]==needle[j]):
            j+=1
        
        if j==len(needle):
            return i

    return -1

haystack = "a"
needle = "a"
print(solve(haystack, needle))