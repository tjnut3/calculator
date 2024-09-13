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

# ฟังก์ชันการจัดการกับสมการ และลำดับความสำคัญ
def calculate(expression):
    operand_stack = []
    operator_stack = []
    
    i = 0
    while i < len(expression):
        # Str เป็นตัวเลขไหม or (เป็นจุดไหม and (ไม่ใช่ Str ตัวสุดท้าย and ตัวต่อไปเป็นตัวเลข))
        # if true จะถูกนำไปเก็บเป็น str 
        if expression[i].isdigit() or (expression[i] == '.' and (i+1 < len(expression) and expression[i+1].isdigit())):
            num_str = ''
            # Str ไม่ใช่ตัวสุดท้าย and (str เป็นตัวเลข or str คือ .)
            # while true เก็บค่าไว้ใน num_str
            while i < len(expression) and (expression[i].isdigit() or expression[i] == '.'):
                num_str += expression[i]
                print(f"str = ", len(expression))
                print(f"i = ", i)
                print(num_str)
                # เช็คตัวต่อไปเลยว่าตัวต่อไปเป็นตัวเลข
                i += 1
            # แปลง str ที่เก็บใน num_str ทั้งหมดไปเป็น float และนำเข้า list operand_stack
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

print(calculate("2+0.3"))
print(len("2+0.3"))