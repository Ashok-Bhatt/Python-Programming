import sys

cmd_line_params = sys.argv
n = len(cmd_line_params)

if n < 4:
    raise TypeError(f"Required 4 arguments, but {n} provided.")
elif type(cmd_line_params[1]) != "str" or type(cmd_line_params[2]) != "str":
    raise TypeError(f"Second and third arguments should be only integers.")
else:
    operand1 = int(cmd_line_params[1])
    operand2 = int(cmd_line_params[2])
    operator = cmd_line_params[3]
    if operator == "+":
        print(operand1 + operand2)
    elif operator == "-":
        print(operand1 - operand2)
    else:
        print("Invalid operator")