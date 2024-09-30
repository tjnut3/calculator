def calculator_input():
    print("โปรแกรมรับตัวเลขและตัวดำเนินการทางคณิตศาสตร์ (พิมพ์ 'exit' เพื่อออกจากโปรแกรม)")

    # เก็บค่าตัวเลขและตัวดำเนินการ
    inputs = []

    while True:
        # รับ input จากผู้ใช้
        user_input = input("ป้อนตัวเลข (0-9) หรือตัวดำเนินการ (+, -, *, /, (, ), =): ")

        # ตรวจสอบว่าข้อมูลที่ป้อนถูกต้องหรือไม่ (ตัวเลข 0-9 หรือ +, -, *, /, (, ), =)
        if user_input in '0123456789+-*/()':
            # บันทึกค่า
            inputs.append(user_input)
            print(f"ค่าเก็บอยู่: {' '.join(inputs)}")
        elif user_input == '=':
            # เมื่อผู้ใช้ใส่ = ให้ return ค่าที่เก็บไว้ใน inputs
            return ''.join(inputs)
        elif user_input == 'exit':
            break
        else:
            print("ค่าที่ป้อนไม่ถูกต้อง กรุณาป้อนเฉพาะตัวเลข 0-9 หรือตัวดำเนินการ (+, -, *, /, (, ), =)")

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
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0}
    operand_stack = []
    operator_stack = []

    i = 0
    while i < len(expression):
        if expression[i].isdigit() or (expression[i] == '.' and (i + 1 < len(expression) and expression[i + 1].isdigit())):
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
            operator_stack.pop()
        else:
            while operator_stack and precedence[operator_stack[-1]] >= precedence[expression[i]]:
                apply_operator(operand_stack, operator_stack.pop())
            operator_stack.append(expression[i])
        i += 1

    while operator_stack:
        apply_operator(operand_stack, operator_stack.pop())

    return operand_stack[-1]

# เรียกใช้โปรแกรม
user_expression = calculator_input()
print((calculate(user_expression)))
