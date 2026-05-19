expression = input("Expression: ")
space_indx = expression.find(" ")
operation = expression[space_indx +1]

expression_list = expression.split(operation)
x = int(expression_list[0].strip())
z = int(expression_list[1].strip())

if operation == "+":
    result = round(float(x + z),1)
elif operation == "-":
    result = round(float(x - z),1)
elif operation == "*":
    result = round(float(x * z),1)
elif operation == "/":
    result = round(float(x / z),1)

print(result)

