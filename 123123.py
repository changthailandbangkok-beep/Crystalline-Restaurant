def calculate_income(name_employ, personal_number, address_employ, employ_number,
                     dept_employ, age_employ, tel_number, salary, total_hours_worked):

    normal_hours = 25 * 8  # 200 ชั่วโมงทำงานปกติ
    hrs_ot = max(0, total_hours_worked - normal_hours)  # ชั่วโมง OT ถ้ามี
    ot_money = hrs_ot * 50
    all_money = salary + ot_money
    social_sec = salary * 0.05
    net_income = all_money - social_sec

    print("\n===== สรุปข้อมูลรายได้ =====")
    print(f"ชื่อพนักงาน: {name_employ}")
    print(f"รหัสพนักงาน: {employ_number}")
    print(f"แผนก: {dept_employ}")
    print(f"เงินเดือน: {salary:.2f} บาท")
    print(f"จำนวนชั่วโมงทำงานทั้งหมด: {total_hours_worked} ชั่วโมง")
    print(f"จำนวนชั่วโมง OT: {hrs_ot} ชั่วโมง")
    print(f"ค่าล่วงเวลา OT: {ot_money:.2f} บาท")
    print(f"รายได้รวม (เงินเดือน + OT): {all_money:.2f} บาท")
    print(f"หักประกันสังคม (5%): {social_sec:.2f} บาท")
    print(f"รายได้สุทธิ: {net_income:.2f} บาท")
    print("==============================\n")

num_employees = int(input("กรอกจำนวนพนักงาน: "))

for i in range(num_employees):
    print(f"\n=== กรอกข้อมูลพนักงานคนที่ {i+1} ===")
    name_employ = input("ชื่อ-นามสกุล: ")
    employ_number = input("รหัสพนักงาน: ")
    dept_employ = input("แผนก: ")
    age_employ = int(input("อายุ: "))
    personal_number = input("รหัสประจำตัวประชาชน: ")
    address_employ = input("ที่อยู่: ")
    tel_number = input("เบอร์โทร: ")
    salary = float(input("เงินเดือน (บาท): "))
    total_hours_worked = int(input("จำนวนชั่วโมงที่ทำงานในเดือนนี้: "))

    calculate_income(name_employ, personal_number, address_employ, employ_number,
                     dept_employ, age_employ, tel_number, salary, total_hours_worked)
