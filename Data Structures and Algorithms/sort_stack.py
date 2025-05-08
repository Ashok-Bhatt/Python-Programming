def placeTop(s, top):
    if len(s)==0 or s[0]<=top:
        s.insert(0, top)
        return
    element = s.pop(0)
    placeTop(s, top)
    s.insert(0, element)

def sortStack(s):
    if len(s) == 0:
        return
    top = s.pop(0)
    sortStack(s)
    placeTop(s, top)

s = [4,7,4,6,2,1]
print(s)
sortStack(s)
print(s)