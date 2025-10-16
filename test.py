def calculate_grade(score):

    if score >= 80:

        grade = "A"

    elif score >= 70:

        grade = "B"

    elif score >= 60:

        grade = "C"

    elif score >= 50:

        grade = "D"

    else:

        grade = "F"

    return grade
 
 
# ตัวอย่างการใช้งาน

score = float(input("กรอกคะแนนของนักเรียน: "))

print(f"เกรดที่ได้คือ: {calculate_grade(score)}")

ตัดเกรด funtion
 






 
def calculate_total(price, quantity, discount=0, tax=0):

    subtotal = price * quantity

    total_after_discount = subtotal - (subtotal * discount / 100)

    total_with_tax = total_after_discount + (total_after_discount * tax / 100)

    return total_with_tax
 
 
# ตัวอย่างการใช้งาน

price = float(input("ราคาต่อชิ้น: "))

quantity = int(input("จำนวนชิ้น: "))

discount = float(input("ส่วนลด (%) : "))

tax = float(input("ภาษี (%) : "))
 
total = calculate_total(price, quantity, discount, tax)

print(f"ราคารวมทั้งหมด: {total:.2f} บาท")

คำนวนสินค้า funtion
 