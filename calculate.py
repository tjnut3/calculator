# กำหนดลำดับความสำคัญของตัวดำเนินการ
precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0}

# ฟังก์ชันคำนวณ
def apply_operator(operands, operator):
    b = operands.pop()
    a = operands.pop()
    if operator == '+':
        operands.append(a + b)
    elif operator == '-':
        operands.append(a - b)
    elif operator == '*':
        operands.append(a * b)
    elif operator == '/':
        operands.append(a / b)

def calculate(expression):
    operand_stack = []
    operator_stack = []
    
    i = 0
    while i < len(expression):
        if expression[i].isdigit() or (expression[i] == '.' and (i+1 < len(expression) and expression[i+1].isdigit())):
            num_str = ''
            while i < len(expression) and (expression[i].isdigit() or expression[i] == '.'):
                num_str += expression[i]
                i += 1
            operand_stack.append(float(num_str))
            i -= 1
        elif expression[i] == '(':
            operator_stack.append(expression[i])
        elif expression[i] == ')':
            while operator_stack and operator_stack[-1] != '(':
                apply_operator(operand_stack, operator_stack.pop())
            operator_stack.pop()  # ลบ '(' ออกจาก stack
        else:
            while (operator_stack and precedence[operator_stack[-1]] >= precedence[expression[i]]):
                apply_operator(operand_stack, operator_stack.pop())
            operator_stack.append(expression[i])
        i += 1
    
    while operator_stack:
        apply_operator(operand_stack, operator_stack.pop())

    return operand_stack[-1]