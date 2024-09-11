import tkinter as tk

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

# ฟังก์ชันการจัดการการกดปุ่ม
def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = calculate(screen.get())
            screen_var.set(result)
        except Exception as e:
            screen_var.set("Error")
    elif text == "C":
        screen_var.set("")
    else:
        screen_var.set(screen_var.get() + text)

# สร้างหน้าต่างหลัก
root = tk.Tk()
root.title("Calculator")

# สร้างตัวแปรเพื่อเก็บค่าที่แสดงบนหน้าจอ
screen_var = tk.StringVar()
screen_var.set("")

# สร้างหน้าจอแสดงผล
screen = tk.Entry(root, textvar=screen_var, font="lucida 20 bold")
screen.pack(fill="both", ipadx=8, padx=10, pady=10)

# สร้างปุ่มตัวเลขและเครื่องหมายคำนวณ รวมถึงวงเล็บ ()
button_frame = tk.Frame(root)
button_frame.pack()

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
    '(', ')', 'C'
]

row = 0
col = 0

for button in buttons:
    b = tk.Button(button_frame, text=button, font="lucida 15 bold", padx=20, pady=20)
    b.grid(row=row, column=col, padx=5, pady=5)
    b.bind("<Button-1>", click)
    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()
