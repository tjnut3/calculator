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

# สองหน้าจอ
from tkinter import *
from tkinter import font

# โครตสำคัญ !!!!!!!!!!!
# ตัวค่าที่ต้องส่งออกไปใช้งานคือตัวแปร value บรรทัดที่ 36 และรับค่าที่คำนวณเสร็จ 41

window = Tk()
window.title("Calculator คอบ. 2")
# font size
button_font = font.Font(size="20")
entry_font = font.Font(size="30")

# สร้าง Frame กำหนดกรอบแยก screen กับ button เพื่อให้ใช้งาน .pack กับ .grid ด้วยกันได้
screen_frame = Frame(window,bg="lightgray")
screen_frame.pack(side=TOP,fill=BOTH,expand=True)
button_frame = Frame(window)
button_frame.pack(side=BOTTOM,fill=BOTH,expand=True)

# # ฟังก์ชันเพื่อเพิ่มค่าลงใน Entry
def append_value(value):
    current_text = getValue.get() # ดึงค่าปัจจุบันจาก Entry
    getValue.delete(0,END)  # ลบค่าปัจจุบันออก ใน button จะใช้งานโดยตรงไม่ได้ใช้ในฟังก์ชั่น
    getValue.insert(0, current_text + value) # เพิ่มค่าใหม่เข้าไปใน Entry

# ลบแค่ค่าเดียว
def delete_last_character():
    current_text = getValue.get()  # ดึงค่าปัจจุบันจาก Entry
    if current_text:  # ตรวจสอบว่ามีข้อความอยู่หรือไม่
        new_text = current_text[:-1]  # ลบตัวอักษรสุดท้าย
        getValue.delete(0, END)  # ลบค่าทั้งหมดใน Entry
        getValue.insert(0, new_text)  # ใส่ข้อความใหม่ที่ไม่มีตัวอักษรสุดท้าย

# save ค่าที่รับมาทั้งหมดแล้ว (=)
def save_value():
    value = textValue.get()  # ตัวแปรที่รับค่าจาก getValue เพื่อจะส่งข้อมูลออกไป
    result = calculate(value)
    showInput.delete(0,END)
    showInput.insert(0,value)
    getValue.delete(0,END) # ใช้รีเช็ตค่าด้านในช่องให้ก่อนแล้วจึงนำผลลัพธ์มาแสดง
    getValue.insert(0,result) # ผลลัพธ์ที่ได้มาใส่ตรงนี้

# button "c" delete ช่อง showInput กับช่อง คำนวณ
def clear_value():
    showInput.delete(0,END)
    getValue.delete(0,END)

# ช่องในการรับค่า
showInput = Entry(screen_frame,width=20,justify="right",font=entry_font)
showInput.pack(fill=BOTH, expand=True,padx=3,pady=3)
textValue = StringVar()
getValue = Entry(screen_frame,textvariable=textValue,width=20,justify="right",font=entry_font)
getValue.pack(fill=BOTH, expand=True,padx=3,pady=3)



# การสร้างปลุ่มโดยใช้ button fg="กำหนดสีคัวอักษร"  bg="กำหนดสีพื้นหลัง" text="ใช้เขียนข้อความ" font=ใช้กำหนดลักษณะตัวอักษร
# ใช้งาน command สำเร็จรูปคือ lambda เป็นการสร้างฟังก์ชั่น นิรนาม เพื่อรับค่า และส่งค่าไปยังฟังก์ชั่น เพื่อลดการซ้ำซ้อนของโปรแกรม ใน Program นี้คือ Function append_value() เมื่อกดปุ่มแล่วส่งค่าให้กับ Entry ที่รับค่า โดยไม่ต้องสร้างฟังก์ชั่นแยกสำหรับปุ่ม หลายๆ ค่า

# แถวที่ 1 ปุ่ม (, ), c , <-
bt_open_p = Button(button_frame,text="(",font=button_font,width=4, command=lambda: append_value("(")).grid(row=1, column=0, sticky="nsew")
bt_close_p = Button(button_frame,text=")",font=button_font,width=4, command=lambda: append_value(")")).grid(row=1, column=1, sticky="nsew")
clear = Button(button_frame,text="C",font=button_font,width=4, command=lambda: clear_value()).grid(row=1, column=2, sticky="nsew")
delete_lastValue = Button(button_frame,text="<-",font=button_font,width=4, command=lambda: delete_last_character()).grid(row=1, column=3, sticky="nsew")

# แถวที่ 2 ปุ่ม 1, 2, 3, +
bt_one = Button(button_frame,text="1",font=button_font,width=4, command=lambda: append_value("1")).grid(row=2, column=0, sticky="nsew")
bt_two = Button(button_frame,text="2",font=button_font,width=4, command=lambda: append_value("2")).grid(row=2, column=1, sticky="nsew")
bt_three = Button(button_frame,text="3",font=button_font,width=4, command=lambda: append_value("3")).grid(row=2, column=2, sticky="nsew")
plus = Button(button_frame,text="+",font=button_font,width=4, command=lambda: append_value("+")).grid(row=2, column=3, sticky="nsew")

# แถวที่ 3 ปุ่ม 4, 5, 6, -
bt_four = Button(button_frame,text="4",font=button_font,width=4, command=lambda: append_value("4")).grid(row=3, column=0, sticky="nsew")
bt_five = Button(button_frame,text="5",font=button_font,width=4, command=lambda: append_value("5")).grid(row=3, column=1, sticky="nsew")
bt_six = Button(button_frame,text="6",font=button_font,width=4, command=lambda: append_value("6")).grid(row=3, column=2, sticky="nsew")
minus = Button(button_frame,text="-",font=button_font,width=4, command=lambda: append_value("-")).grid(row=3, column=3, sticky="nsew")

# แถวที่ 4 ปุ่ม 7, 8, 9, *
bt_seven = Button(button_frame,text="7",font=button_font,width=4, command=lambda: append_value("7")).grid(row=4, column=0, sticky="nsew")
bt_eight = Button(button_frame,text="8",font=button_font,width=4, command=lambda: append_value("8")).grid(row=4, column=1, sticky="nsew")
bt_nine = Button(button_frame,text="9",font=button_font,width=4, command=lambda: append_value("9")).grid(row=4, column=2, sticky="nsew")
multi = Button(button_frame,text="*",font=button_font,width=4, command=lambda: append_value("*")).grid(row=4, column=3, sticky="nsew")

# แถวที่ 5 ปุ่ม ., 0, =, /
dot = Button(button_frame,text=".",font=button_font,width=4, command=lambda: append_value(".")).grid(row=5, column=0, sticky="nsew")
bt_zero = Button(button_frame,text="0",font=button_font,width=4, command=lambda: append_value("0")).grid(row=5, column=1, sticky="nsew")
equal = Button(button_frame,text="=",font=button_font,width=4,command=save_value).grid(row=5, column=2, sticky="nsew")
devide = Button(button_frame,text="/",font=button_font,width=4, command=lambda: append_value("/")).grid(row=5, column=3, sticky="nsew")

# กำหนดให้ปุ่มหน้าจอขยายตามขอบโปรแกรม (Responesive)
for i in range(5):
    window.grid_columnconfigure(i, weight=1) # weight= 1 กำหนดให้มีขยายตามหน้าจอโปรแกรม 0 คือไม่ต้องขยายตาม
for i in range(6):
    button_frame.grid_rowconfigure(i, weight=1)  # Make rows grow with window
for i in range(4):
    button_frame.grid_columnconfigure(i, weight=1)  # Make columns grow with window

# กำหนดขนาดของโปรแกรม
window.geometry("300x400")
window.minsize(200, 200)
window.mainloop()  # ให้โปรแกรมทำงานเรื่อย ๆ
