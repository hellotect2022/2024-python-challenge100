from logos.logo import logo_calc 
print(logo_calc)

def multipy(num1,num2):
    return num1 * num2
def plus(num1, num2):
    return num1 + num2
def minus(num1, num2):
    return num1 - num2
def div(num1, num2):
    return num1 / num2

operations = {
    '+': plus,
    '-': minus,
    '*': multipy,
    '/': div,
}

def start_calc(initial_value = None):
    result = 0
    if initial_value is None:
        initial_value = float(input("what's the first number? : "))
    for key in operations:
        print(key)

    operator = input("Pick an operation : ")
    second_num = float(input("what's the second number? : "))
    
    cal_func = operations[operator]
    result = cal_func(initial_value,second_num)
    print(f"{initial_value} {operator} {second_num} = {result}")
    a = input(f"type 'y' to continue calculating with {result}, or type 'n' to start a new calculation : ")
    if a.lower() == "y":
        start_calc(result)

start_calc()