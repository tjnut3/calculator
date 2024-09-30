def calculator_input():
    print("โปรแกรมรับตัวเลขและตัวดำเนินการทางคณิตศาสตร์ (พิมพ์ 'exit' เพื่อออกจากโปรแกรม)")

    # เก็บค่าตัวเลขและตัวดำเนินการ
    inputs = []

    while True:
        # รับ input จากผู้ใช้
        user_input = input("ป้อนตัวเลข (0-9) หรือตัวดำเนินการ (+, -, *, /, (, )): ")

        # ตรวจสอบว่าข้อมูลที่ป้อนถูกต้องหรือไม่ (ตัวเลข 0-9 หรือ +, -, *, /, (, ))
        if user_input in '0123456789+-*/()':
            # บันทึกค่า
            inputs.append(user_input)
            print(inputs)
            print(f"ค่าเก็บอยู่: {' '.join(inputs)}")
        elif user_input in '=':
            return ' '.join(inputs)
        else:
            print("ค่าที่ป้อนไม่ถูกต้อง กรุณาป้อนเฉพาะตัวเลข 0-9 หรือตัวดำเนินการ (+, -, *, /, (, ))")

input = calculator_input()