# --- รับตัวเลขหลายค่าเป็น list แล้วคำนวณ ---
# วิธีพิมพ์: ใส่เลขคั่นด้วยช่องว่าง เช่น 10 5 7 3
nums = list(map(int, input("ใส่ตัวเลขหลายๆ ตัว คั่นด้วยช่องว่าง: ").split()))

print("List =", nums)
print("จำนวนสมาชิก =", len(nums))
print("ผลรวม =", sum(nums))
print("ค่าเฉลี่ย =", sum(nums) / len(nums) if nums else 0)
print("ค่าน้อยสุด =", min(nums) if nums else None)
print("ค่ามากสุด =", max(nums) if nums else None)

# เพิ่มค่าใน list
nums.append(100)         # ต่อท้าย
nums.insert(0, 999)      # แทรกตำแหน่ง 0
print("หลังเพิ่ม:", nums)

# ลบค่า
if nums:
    nums.pop()           # ลบตัวท้าย
print("หลังลบตัวท้าย:", nums)






def summarize_numbers(numbers):
    """รับ list ของตัวเลข แล้วสรุปค่าต่างๆ คืนเป็น dict"""
    if not numbers:
        return {"count": 0, "sum": 0, "avg": 0, "min": None, "max": None}
    return {
        "count": len(numbers),
        "sum": sum(numbers),
        "avg": sum(numbers) / len(numbers),
        "min": min(numbers),
        "max": max(numbers),
    }

# ทดลองใช้
nums = [10, 20, 30, 40]
info = summarize_numbers(nums)
print(info)  # {'count': 4, 'sum': 100, 'avg': 25.0, 'min': 10, 'max': 40}






# tuple เหมือน list แต่แก้ไขไม่ได้
point = (3, 5)                # จุด (x, y)
x, y = point                  # tuple unpacking
print("x =", x, "y =", y)

grades = (88, 75, 92)
print("เฉลี่ย =", sum(grades) / len(grades))
# grades[0] = 99  # ❌ แก้ค่าไม่ได้ จะ error




# เก็บคะแนนนักเรียนใน dict: ชื่อ -> คะแนน
scores = {"Ann": 80, "Ben": 92}
scores["Cat"] = 75              # เพิ่มสมาชิก
scores["Ann"] = 85              # แก้ค่า

print("ทั้งหมด:", scores)
print("รายชื่อ:", list(scores.keys()))
print("คะแนน:", list(scores.values()))
print("คู่ (ชื่อ, คะแนน):", list(scores.items()))
print("ผลรวมคะแนน =", sum(scores.values()))
print("ค่าเฉลี่ย =", sum(scores.values()) / len(scores))

# นับความถี่คำง่ายๆ ด้วย dict
words = input("พิมพ์คำ คั่นด้วยช่องว่าง: ").split()
freq = {}
for w in words:
    freq[w] = freq.get(w, 0) + 1
print("ความถี่คำ:", freq)







# สต๊อกสินค้า: ชื่อ -> ราคา
prices = {"apple": 10, "banana": 7, "milk": 22}

# ตะกร้า: ชื่อสินค้า -> จำนวน
cart = {}

def add_to_cart(name, qty=1):
    """เพิ่มสินค้าเข้าตะกร้า ถ้าไม่มีในสต๊อกจะข้าม"""
    if name not in prices:
        print(f"ไม่มีสินค้า '{name}' ในสต๊อก")
        return
    cart[name] = cart.get(name, 0) + qty

def cart_total():
    """คำนวณราคารวมจากตะกร้า"""
    total = 0
    for name, qty in cart.items():
        total += prices[name] * qty
    return total

# ทดลองใช้งาน
add_to_cart("apple", 3)
add_to_cart("banana", 2)
add_to_cart("cookie", 1)   # ไม่มีในสต๊อก -> แจ้งเตือน
print("ตะกร้า:", cart)
print("ยอดรวม =", cart_total(), "บาท")






def read_numbers():
    return list(map(int, input("เลข(คั่นด้วยช่องว่าง): ").split()))

def show_summary(nums):
    s = summarize_numbers(nums)  # ใช้ฟังก์ชันจากข้อ #2
    print(f"จำนวน={s['count']} ผลรวม={s['sum']} เฉลี่ย={s['avg']:.2f} ต่ำสุด={s['min']} สูงสุด={s['max']}")

def demo_tuple():
    t = tuple(read_numbers())
    print("tuple =", t)
    if t:
        print("สมาชิกแรก =", t[0])

def demo_dict_count():
    print("พิมพ์ชื่อของกิน (เว้นวรรคคั่น): ")
    items = input().split()
    counts = {}
    for it in items:
        counts[it] = counts.get(it, 0) + 1
    print("สรุปจำนวนแต่ละอย่าง:", counts)

# เริ่มเดโม
nums = read_numbers()   # รับเป็น list
show_summary(nums)      # สรุป
demo_tuple()            # แปลงเป็น tuple และดูค่า
demo_dict_count()       # สร้าง dict นับความถี่




# หาผลรวมของเลข 1–100
total = 0
for i in range(1, 101):
    total += i
print("ผลรวม 1-100 =", total)



# พิมพ์สูตรคูณแม่ 7
for i in range(1, 13):
    print(f"7 x {i} = {7*i}")



    # หาค่าแฟกทอเรียล (n!)
n = int(input("ใส่ค่า n: "))
fact = 1
for i in range(1, n+1):
    fact *= i
print(f"{n}! =", fact)




#พิมพ์สามเหลี่ยมด้วย *
rows = 5
for i in range(1, rows+1):
    print("*" * i)



# ตรวจหาจำนวนคู่และคี่
nums = [3, 8, 12, 5, 7, 10]
even = []
odd = []

for n in nums:
    if n % 2 == 0:
        even.append(n)
    else:
        odd.append(n)

print("จำนวนคู่ =", even)
print("จำนวนคี่ =", odd)




#หาค่ามากสุด-น้อยสุด (ไม่ใช้ max/min)
nums = [15, 22, 3, 99, 42]
big = nums[0]
small = nums[0]

for n in nums:
    if n > big:
        big = n
    if n < small:
        small = n

print("ค่ามากสุด =", big)
print("ค่าน้อยสุด =", small)


#รับชื่อหลายคนแล้วพิมพ์ทีละชื่อ (ไม่ใช้ split)
text = input("ใส่ชื่อหลายคน คั่นด้วย , : ")   # เช่น ann,ben,cat
name = ""
for ch in text:
    if ch == ",":
        print("ชื่อ:", name.strip())
        name = ""
    else:
        name += ch
if name != "":
    print("ชื่อ:", name.strip())




    # เช็คว่าเป็นจำนวนเฉพาะ (prime number)
n = int(input("ใส่ตัวเลข: "))
is_prime = True

if n < 2:
    is_prime = False
else:
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break

print(n, "เป็นจำนวนเฉพาะ?" , is_prime)




#ตัวอย่างโค้ดเกี่ยวกับ dict
# เก็บชื่อกับคะแนน แล้วหาค่าเฉลี่ย
scores = {"Ann": 80, "Ben": 75, "Cat": 92}

total = 0
for name in scores:
    total += scores[name]

print("คะแนนเฉลี่ย =", total / len(scores))




#หาค่ามากสุดใน dict
scores = {"Ann": 80, "Ben": 95, "Cat": 72}
max_name = ""
max_score = -1

for name, score in scores.items():
    if score > max_score:
        max_score = score
        max_name = name

print("คนที่ได้คะแนนสูงสุดคือ", max_name, "=", max_score)




#ตัวอย่างโค้ดเกี่ยวกับ set
# หาตัวเลขที่ไม่ซ้ำ
nums = [1, 2, 2, 3, 4, 4, 5]
unique = set()

for n in nums:
    unique.add(n)

print("เลขที่ไม่ซ้ำ =", unique)



#หาจำนวนที่เหมือนกันระหว่าง 2 set
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

common = set()
for x in a:
    if x in b:
        common.add(x)

print("สมาชิกที่ซ้ำกัน =", common)




#หาจำนวนที่อยู่ใน a แต่ไม่อยู่ใน b
a = {1, 2, 3, 4}
b = {3, 4, 5}

diff = set()
for x in a:
    if x not in b:
        diff.add(x)

print("สมาชิกที่มีใน a แต่ไม่มีใน b =", diff)





#ตัวอย่างโค้ดเกี่ยวกับ tuple
# เก็บพิกัด (x,y) แล้วบวกทั้งหมด
points = [(2, 3), (5, 7), (1, 9)]
total_x = 0
total_y = 0

for x, y in points:
    total_x += x
    total_y += y

print("ผลรวมแกน x =", total_x)
print("ผลรวมแกน y =", total_y)



# หาค่ามากสุดจาก tuple
nums = (10, 5, 20, 7, 15)

big = nums[0]
for n in nums:
    if n > big:
        big = n

print("ค่ามากสุด =", big)

#dict → ใช้กับข้อมูลแบบ "ชื่อ → ค่า" เช่น นับความถี่, คะแนนนักเรียน

#set → ใช้กับข้อมูลที่ไม่ซ้ำ เช่น หาค่าซ้ำกัน, หาค่าที่ไม่เหมือนกัน

#tuple → ใช้เก็บข้อมูลที่แก้ไม่ได้ เช่น พิกัด (x,y), หรือสลับค่าตัวแปร



#xList + Function
# หาผลรวมและค่าเฉลี่ย
def summarize_list(nums):
    total = 0
    for n in nums:
        total += n
    avg = total / len(nums) if nums else 0
    return total, avg

# ทดลองใช้
numbers = [10, 20, 30, 40]
s, a = summarize_list(numbers)
print("ผลรวม =", s, "ค่าเฉลี่ย =", a)



#Dict + Function
# หาคนที่ได้คะแนนสูงสุด
def top_student(scores):
    max_name = None
    max_score = -1
    for name, score in scores.items():
        if score > max_score:
            max_score = score
            max_name = name
    return max_name, max_score

# ทดลองใช้
scores = {"Ann": 80, "Ben": 95, "Cat": 72}
name, score = top_student(scores)
print("คนที่ได้คะแนนสูงสุดคือ", name, "=", score)






#Tuple + Function
# หาผลรวมพิกัด (x,y)
def sum_points(points):
    total_x, total_y = 0, 0
    for x, y in points:
        total_x += x
        total_y += y
    return total_x, total_y

# ทดลองใช้
pts = [(2, 3), (5, 7), (1, 9)]
x_sum, y_sum = sum_points(pts)
print("ผลรวมแกน x =", x_sum, "ผลรวมแกน y =", y_sum)\





#Set + Function
# หาสมาชิกที่เหมือนกันระหว่าง 2 set
def common_elements(a, b):
    result = set()
    for x in a:
        if x in b:
            result.add(x)
    return result

# ทดลองใช้
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print("สมาชิกที่ซ้ำกัน =", common_elements(A, B))
