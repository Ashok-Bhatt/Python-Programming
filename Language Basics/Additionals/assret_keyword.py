def solve(x, y):
    
    assert y!=0, "Division by zero not possible! "
    addition = x + y
    subtraction = x - y
    multiplication = x * y
    division = x / y
    return [addition, subtraction, multiplication, division]


print(solve(8,0))