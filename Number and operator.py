def calculator_input():
    print("โปรแกรมรับตัวเลขและตัวดำเนินการทางคณิตศาสตร์ (พิมพ์ 'exit' เพื่อออกจากโปรแกรม)")

    # เก็บค่าตัวเลขและตัวดำเนินการ
    inputs = []

    while True:
        # รับ input จากผู้ใช้
        user_input = input("ป้อนตัวเลข (0-9) หรือตัวดำเนินการ (+, -, *, /, (, )): ")

        # ตรวจสอบหากผู้ใช้ต้องการออกจากโปรแกรม
        if user_input.lower() == 'exit':
            print("ออกจากโปรแกรมแล้ว ขอบคุณที่ใช้บริการ!")
            break

        # ตรวจสอบว่าข้อมูลที่ป้อนถูกต้องหรือไม่ (ตัวเลข 0-9 หรือ +, -, *, /, (, ))
        if user_input in '0123456789+-*/()=':
            # บันทึกค่า
            inputs.append(user_input)
            print(f"ค่าเก็บอยู่: {' '.join(inputs)}")
        else:
            print("ค่าที่ป้อนไม่ถูกต้อง กรุณาป้อนเฉพาะตัวเลข 0-9 หรือตัวดำเนินการ (+, -, *, /, (, ))")
print("Again")
print("ลองเพิ่มดูอีกรอบ")
calculator_input()
