লজিক্যাল অপারেটর ব্যবহার করা হয় একাধিক শর্ত (condition) যুক্ত করতে এবং বুলিয়ান (True/False) ভ্যালু নিয়ে কাজ করতে। এগুলো কন্ডিশনাল স্টেটমেন্ট (if-else) এবং লুপ-এ সবচেয়ে বেশি ব্যবহৃত হয়।

পাইথনে ৩টি লজিক্যাল অপারেটর আছে:

অপারেটর	                                    কাজ
 and (অ্যান্ড)                       দুটি শর্তই সত্য হলে True
 or (অর)                          যেকোনো একটি শর্ত সত্য হলে True
 not (নট)                          শর্তকে উল্টে দেয় (True → False, False → True)








  
and অপারেটর (সবগুলো শর্ত সত্য হতে হবে)

and অপারেটরের দুই পাশের সবগুলো শর্তই সত্য (True) হতে হবে। যদি একটি শর্তও মিথ্যা (False) হয়, তবে পুরো ফলাফলটিই False হয়ে যাবে।


# AND এর ট্রুথ টেবিল
print(True and True)   # True
print(True and False)  # False
print(False and True)  # False
print(False and False) # False


# উদাহরণ: ব্যাংকে লোন পাওয়ার জন্য বয়স ১৮+ এবং ইনকাম ২০০০০+ হতে হবে
age = 25
income = 25000

eligible = (age > 18) and (income > 20000)
print("লোন পাবেন কি না? :", eligible)  # Output: True (কারণ দুটি শর্তই সত্য)




# and অপারেটর - দুটি শর্তই সত্য হতে হবে

age = 25
has_license = True

# দুটি শর্তই চেক
if age >= 18 and has_license:
    print("You can drive")  # ✅ এইটা প্রিন্ট হবে
else:
    print("You cannot drive")

# আউটপুট: You can drive



একাধিক শর্ত (চেইনিং):

# একাধিক and ব্যবহার
score = 85
attendance = 90
has_homework = True

if score >= 80 and attendance >= 75 and has_homework:
    print("Student passed with honors")  # ✅ প্রিন্ট হবে
else:
    print("Student needs improvement")



শর্ট-সার্কিট ইভ্যালুয়েশন (Short-Circuit):

# and-এ প্রথম শর্ত যদি False হয়, বাকি শর্ত চেক করা হয় না

def check_first():
    print("Checking first condition")
    return False

def check_second():
    print("Checking second condition")
    return True

# দ্বিতীয় ফাংশন কল হবে না কারণ প্রথমটি False
result = check_first() and check_second()
print(result)  # False

# আউটপুট:
# Checking first condition
# False




রিয়েল-ওয়ার্ল্ড উদাহরণ:

# ইউজার লগইন ভ্যালিডেশন
username = "admin"
password = "secret123"
is_active = True

if username == "admin" and password == "secret123" and is_active:
    print("Login successful!")  # ✅
else:
    print("Invalid credentials")

# ই-কমার্স: অর্ডার প্লেস করা যাবে কিনা
product_price = 500
user_balance = 1000
stock_available = 10
user_is_verified = True

if user_balance >= product_price and stock_available > 0 and user_is_verified:
    print("Order placed successfully!")
    user_balance -= product_price
    stock_available -= 1
else:
    print("Cannot place order. Check balance, stock, or verification.")







or অপারেটর (OR)
or অপারেটরের দুই পাশের শর্তগুলোর মধ্যে যেকোনো একটি সত্য (True) হলেই চূড়ান্ত ফলাফল True হয়। দুটি শর্তই মিথ্যা হলে কেবল তখনই ফলাফল False হয়।

# OR এর ট্রুথ টেবিল
print(True or True)   # True
print(True or False)  # True
print(False or True)  # True
print(False or False) # False



# vacancies: জব পাওয়ার জন্য সিএসই ডিগ্রি অথবা ৩ বছরের অভিজ্ঞতা দরকার
has_cse_degree = False
has_experience = True

got_job = has_cse_degree or has_experience
print("জব পাবেন কি না? :", got_job)  # Output: True (কারণ অভিজ্ঞতা আছে, ১টি শর্ত মিলেছে)



# or অপারেটর - যেকোনো একটি শর্ত সত্য হলেই হবে

day = "Saturday"

if day == "Saturday" or day == "Sunday":
    print("It's weekend!")  # ✅
else:
    print("It's a weekday")

# আউটপুট: It's weekend!



একাধিক শর্ত:

# একাধিক or ব্যবহার
user_role = "editor"

if user_role == "admin" or user_role == "editor" or user_role == "moderator":
    print("User has write access")  # ✅
else:
    print("User has read-only access")



শর্ট-সার্কিট ইভ্যালুয়েশন (OR):

# or-এ প্রথম শর্ত যদি True হয়, বাকি শর্ত চেক করা হয় না

def expensive_operation():
    print("Running expensive operation...")
    return True

def quick_check():
    print("Quick check")
    return True

# প্রথমটি True, তাই expensive_operation() কল হবে না
result = quick_check() or expensive_operation()
print(result)  # True

# আউটপুট:
# Quick check
# True



রিয়েল-ওয়ার্ল্ড উদাহরণ:

# ডিসকাউন্ট চেক - বিভিন্ন শর্তে ডিসকাউন্ট পাওয়া যাবে
is_member = True
has_coupon = False
is_first_order = True
total_amount = 1500

# ডিসকাউন্টের শর্ত: মেম্বার অথবা কুপন অথবা প্রথম অর্ডার
if is_member or has_coupon or is_first_order:
    print("You get a discount!")  # ✅
else:
    print("No discount available")

# ফোন নম্বর ভ্যালিডেশন
phone = "01712345678"
email = "user@example.com"

if phone or email:
    print("Contact info exists")  # ✅
    
# ডিফল্ট ভ্যালু সেট করা
user_input = ""
default_value = "Guest"

# user_input খালি হলে ডিফল্ট ব্যবহার
name = user_input or default_value
print(name)  # Guest





not অপারেটর (NOT)
এটি একটি ইউনারি অপারেটর  এর কাজ হলো সত্যকে মিথ্যা এবং মিথ্যাকে সত্য বানানো।

# NOT এর ট্রুথ টেবিল
print(not True)   # False
print(not False)  # True



is_raining = False
print("বাইরে যাব কি না? :", not is_raining)  # Output: True (বৃষ্টি হচ্ছে না, তাই যাব)



# not অপারেটর - বুলিয়ান ভ্যালু উল্টে দেয়

is_raining = True

if not is_raining:
    print("Let's go outside!")  # ❌ এইটা প্রিন্ট হবে না
else:
    print("Stay inside, it's raining!")  # ✅

# আউটপুট: Stay inside, it's raining!



বিভিন্ন ডেটা টাইপের সাথে NOT:

# পাইথনে False হিসেবে বিবেচিত হয়:
# - False (বুলিয়ান)
# - 0, 0.0 (সংখ্যা)
# - "" (খালি স্ট্রিং)
# - [] (খালি লিস্ট)
# - {} (খালি ডিকশনারি)
# - () (খালি টাপল)
# - None

print(not False)   # True
print(not 0)       # True
print(not "")      # True
print(not [])      # True
print(not {})      # True
print(not None)    # True

# True হিসেবে বিবেচিত হয় বাকি সব
print(not 5)       # False
print(not "Hello") # False
print(not [1, 2])  # False



রিয়েল-ওয়ার্ল্ড উদাহরণ:

# ইউজার লগআউট চেক
is_logged_in = True

if not is_logged_in:
    print("Please login first")
else:
    print("Welcome back, user!")  # ✅

# ফাইল খালি কিনা চেক
file_content = ""

if not file_content:
    print("File is empty")  # ✅
else:
    print("File has content")

# খালি লিস্ট চেক
cart = []

if not cart:
    print("Your cart is empty. Add items!")  # ✅
else:
    print(f"You have {len(cart)} items in cart")

# পারমিশন চেক
has_admin_access = False

if not has_admin_access:
    print("Access denied. Admin rights required.")  # ✅
else:
    print("Welcome to admin panel")




কম্বাইনড অপারেটর (Combining Operators)
AND + OR একসাথে:

# একাধিক লজিক্যাল অপারেটর একসাথে

age = 25
has_id = True
is_student = False
is_weekend = True

# জটিল শর্ত
if (age >= 18 and has_id) or (is_student and is_weekend):
    print("Eligible for discount")  # ✅
else:
    print("Not eligible")

# ব্যাখ্যা: 
# (age >= 18 and has_id) = True
# (is_student and is_weekend) = False
# True or False = True



NOT + AND/OR একসাথে:

# not ব্যবহার করে শর্ত উল্টানো

is_logged_in = True
has_permission = False
is_admin = True

# অ্যাডমিন নয় কিন্তু লগইন করা এবং পারমিশন আছে
if not is_admin and is_logged_in and has_permission:
    print("Access granted")
else:
    print("Access denied")  # ✅ (কারণ has_permission False)

# যদি শর্ত পুরোপুরি উল্টাতে চান
is_blocked = False

if not is_blocked:
    print("User is active")  # ✅


অগ্রাধিকার (Precedence) - কোনটা আগে কাজ করে?

# অগ্রাধিকার ক্রম: not > and > or

# ১. not (সর্বোচ্চ অগ্রাধিকার)
# ২. and
# ৩. or (সর্বনিম্ন অগ্রাধিকার)

x = True
y = False
z = True

# পাইথন এভাবে দেখে: not x or y and z
# (not x) or (y and z)
# not x = False
# y and z = False and True = False
# False or False = False
result = not x or y and z
print(result)  # False

# কিন্তু ব্র্যাকেট ব্যবহার করলে পরিষ্কার হয়
result = (not x) or (y and z)
print(result)  # False

# ব্র্যাকেট পরিবর্তন করলে ফলাফল বদলায়
result = not (x or y) and z
# (x or y) = True
# not True = False
# False and True = False
print(result)  # False




Advanced------------

এলইপি (LBYL) vs এএফপি (EAFP)

LBYL (Look Before You Leap) - চেক করে তারপর কাজ:

# LBYL স্টাইল - শর্ত চেক করে তারপর অপারেশন

user_input = "abc123"

# চেক করছে সংখ্যা কিনা
if user_input.isdigit():
    number = int(user_input)
    print(f"Number: {number}")
else:
    print("Invalid number")

# ফাইল আছে কিনা চেক
import os

if os.path.exists("data.txt"):
    with open("data.txt", "r") as f:
        content = f.read()
else:
    print("File not found")





EAFP (Easier to Ask for Forgiveness than Permission) - পরে এরর হ্যান্ডেল:

# EAFP স্টাইল - চেষ্টা করে দেখ, না হলে এরর হ্যান্ডেল

user_input = "abc123"

try:
    number = int(user_input)
    print(f"Number: {number}")
except ValueError:
    print("Invalid number")

# ফাইল পড়ার চেষ্টা
try:
    with open("data.txt", "r") as f:
        content = f.read()
except FileNotFoundError:
    print("File not found")



লজিক্যাল অপারেটরের অ্যাডভান্সড ব্যবহার

বুলিয়ান ইন্টিজার হিসেবে ব্যবহার:

# True = 1, False = 0

x = True
y = False

print(x + y)        # 1 + 0 = 1
print(x * 5)        # 1 * 5 = 5
print(x - y)        # 1 - 0 = 1

# অ্যাডভান্সড: কাউন্টার হিসেবে
tasks = [True, False, True, True, False]
completed = sum(1 for task in tasks if task)  # True গুলো কাউন্ট
print(f"Completed: {completed} out of {len(tasks)}")  # Completed: 3 out of 5

# অথবা সরাসরি
completed = sum(tasks)  # True = 1, False = 0
print(f"Completed: {completed}")  # Completed: 3



এলিস (or) দিয়ে ডিফল্ট ভ্যালু:

# ডিফল্ট ভ্যালু সেট করা

def get_username(user_data):
    # user_data['username'] থাকলে সেটা নেবে, না হলে ডিফল্ট
    return user_data.get('username') or "Anonymous"

# টেস্ট
user1 = {'username': 'john_doe'}
user2 = {}

print(get_username(user1))  # john_doe
print(get_username(user2))  # Anonymous

# আরেকটি উপায়
name = input("Enter name: ") or "Guest"
print(f"Hello, {name}!")  # ইনপুট না দিলে Guest




আন্ড (and) দিয়ে চেকিং:

# and দিয়ে শর্ত চেক

def validate_age(age):
    # age থাকলে এবং 18 এর বেশি হলে True
    return age and age >= 18

print(validate_age(25))   # True
print(validate_age(15))   # False
print(validate_age(None)) # None (কারণ age False)

# প্রোডাক্ট চেক
def get_product_price(product):
    # product থাকলে এবং stock থাকলে প্রাইস রিটার্ন
    if product and product.get('stock', 0) > 0:
        return product.get('price')
    return 0

product1 = {'name': 'Laptop', 'price': 50000, 'stock': 10}
product2 = {'name': 'Mouse', 'price': 500, 'stock': 0}
product3 = None

print(get_product_price(product1))  # 50000
print(get_product_price(product2))  # 0
print(get_product_price(product3))  # 0


অল (all()) এবং যেকোনো (any()) ফাংশন:

# all() - সবগুলো শর্ত সত্য কিনা

numbers = [10, 20, 30, 40]

# সবগুলো ৫ এর বেশি?
print(all(num > 5 for num in numbers))  # True

# সবগুলো ২৫ এর বেশি?
print(all(num > 25 for num in numbers))  # False

# ইউজার ভ্যালিডেশন
user = {
    'name': 'John',
    'email': 'john@example.com',
    'age': 30
}

required_fields = ['name', 'email', 'age']

# সব ফিল্ড আছে কিনা
if all(field in user for field in required_fields):
    print("User data complete")  # ✅
else:
    print("Missing required fields")

# any() - কোনো একটি শর্ত সত্য কিনা

numbers = [1, 3, 5, 7, 9]

# কোনো জোড় সংখ্যা আছে?
print(any(num % 2 == 0 for num in numbers))  # False

# কোনো ৫ এর বেশি সংখ্যা আছে?
print(any(num > 5 for num in numbers))  # True

# ফাইল চেক
files = ['data.txt', 'config.json', 'log.txt']

# কোনো JSON ফাইল আছে?
if any(file.endswith('.json') for file in files):
    print("JSON file found")  # ✅



লিস্ট কম্প্রিহেনশনে ব্যবহার:

# ফিল্টারিং

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# জোড় এবং ৫ এর বেশি
filtered = [x for x in numbers if x % 2 == 0 and x > 5]
print(filtered)  # [6, 8, 10]

# অথবা ৩ বা ৫ দিয়ে বিভাজ্য
filtered = [x for x in range(1, 21) if x % 3 == 0 or x % 5 == 0]
print(filtered)  # [3, 5, 6, 9, 10, 12, 15, 18, 20]

# not ব্যবহার
numbers = [0, 1, 2, 3, 4, 5]
non_zero = [x for x in numbers if not x == 0]
print(non_zero)  # [1, 2, 3, 4, 5]


লজিক্যাল অপারেটরের ব্যাকএন্ড ব্যবহার ----------------জানা লাগবে
