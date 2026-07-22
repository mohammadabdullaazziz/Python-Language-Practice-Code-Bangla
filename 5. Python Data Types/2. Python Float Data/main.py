float হলো Python-এর দশমিক সংখ্যা (Floating-point number) ডেটা টাইপ। যেমন: 3.1416, 99.99, -0.5, বা এমনকি 5.0 (এখানে এটি পূর্ণসংখ্যা মনে হলেও দশমিক থাকার কারণে এটি ফ্লোট)।

এটি দশমিক বিন্দু (.) যুক্ত সংখ্যা ধারণ করে।

উদাহরণ: ৩.১৪, -০.৫, ২.০, ১.৫e৩ (বৈজ্ঞানিক notation)।





মূল ডাটা (C-level IEEE 754): ৮ বাইট বা ৬৪-বিট
কম্পিউটার বা প্রসেসরের হার্ডওয়্যার কেবল ০ এবং ১ বোঝে।
বিশ্বের সব বিজ্ঞানীরা মিলে যে IEEE 754 Double-precision standard তৈরি করেছেন, সেই নিয়ম অনুযায়ী একটি দশমিক সংখ্যাকে কম্পিউটারের বিটে রূপান্তর করে জমা রাখতে ঠিক ৬৪ বিট (বা ৮ বাইট) জায়গাই লাগে।
আর পাইথনের ফ্লোট যেহেতু একটু বেশি ক্ষমতাশালী, তাই সে এই নিয়মের ডাবল-প্রিসিশন (Double-precision) বা ৬৪-বিট সংস্করণটি ব্যবহার করে।


পাইথনের অবজেক্ট (Python PyObject): ২৪ বাইট

পাইথন একটি হাই-লেভেল ল্যাঙ্গুয়েজ। পাইথনে কোনো সংখ্যা সরাসরি খালি অবস্থায় মেমোরিতে বসে না।

পাইথন সেই ৮ বাইটের ফ্লোট সংখ্যাটিকে একটি সুন্দর প্যাকেজ বা খামের (Object Header) ভিতর মুড়িয়ে রাখে। এই অতিরিক্ত তথ্যগুলো পাইথনকে মেমোরি ম্যানেজমেন্ট ও ডাইনামিক টাইপিংয়ে সাহায্য করে।

মেমোরির হিসাবটা তখন এমন দাঁড়ায়:

১৬ বাইট: পাইথনের নিজস্ব প্যাকেজিং ওভারহেড (Reference count & Type info)

+ ৮ বাইট: মূল IEEE 754 স্ট্যান্ডার্ডের ৬৪-বিট ফ্লোটিং সংখ্যাটি

= মোট ২৪ বাইট (মেমোরিতে পাইথনের একটি float অবজেক্টের সাইজ)


import sys

x = 3.14
print(sys.getsizeof(x))  # আউটপুট দেখাবে: 24 (Bytes)

হার্ডওয়্যার ও IEEE 754 স্ট্যান্ডার্ডের বিচারে: ফ্লোট ৬৪-বিট (৮ বাইট)।

পাইথন প্রোগ্রামিং ও মেমোরি অ্যালকেশনের বিচারে: একটি float অবজেক্ট মেমোরিতে ২৪ বাইট জায়গা দখল করে।





ইমিউটেবল (Immutable)	একবার তৈরি হলে পরিবর্তন করা যায় না।

সীমাবদ্ধতা	খুব বড় বা খুব ছোট সংখ্যার জন্য সীমা আছে (যেমন: ১.৭৯e৩০৮ পর্যন্ত)

প্রিসিশন	প্রায় ১৫-১৭ দশমিক ডিজিট পর্যন্ত সঠিকতা থাকে 

বৈজ্ঞানিক notation	e বা E ব্যবহার করে লেখা যায়




পাইথনে একটি float সর্বোচ্চ 1.79 * 10^308 পর্যন্ত বড় সংখ্যা এবং সর্বনিম্ন 2.22 * 10^-308 পর্যন্ত ক্ষুদ্রতম সংখ্যা ধরে রাখতে পারে।

এর চেয়ে বড় কোনো সংখ্যা পাইথনে দিলে সেটি মেমোরিতে ধরে রাখতে পারে না এবং পাইথন সেটাকে inf (Infinity) হিসেবে গণ্য করে।



Float এর সীমা ও বিশেষ মান

import sys

# সর্বোচ্চ ও সর্বনিম্ন float মান
print(sys.float_info.max)   # 1.7976931348623157e+308
print(sys.float_info.min)   # 2.2250738585072014e-308

# বিশেষ মান
infinity = float('inf')      # অসীম (∞)
neg_inf  = float('-inf')     # ঋণাত্মক অসীম (-∞)
not_num  = float('nan')      # NaN = Not a Number

print(infinity)    # inf
print(neg_inf)     # -inf
print(not_num)     # nan

# পরীক্ষা করা
import math
print(math.isinf(infinity))   # True
print(math.isnan(not_num))    # True




num1 = 10.2

print(f'Is int: {isinstance(num1, float)}')

print(f'Is type int {type(num1) == float}')




💰 টাকার হিসাব → ৯৯.৯৯ টাকা
🌡️ তাপমাত্রা → ৩৬.৫°C
📏 উচ্চতা → ৫.৮ ফুট
⚖️ ওজন → ৬৫.৫ কেজি




১. ডিক্লেয়ারেশন বা লেখার নিয়ম

পাইথনে কোনো ভেরিয়েবলে দশমিক সংখ্যা রাখলেই সেটি স্বয়ংক্রিয়ভাবে ফ্লোট ডেটা টাইপ হয়ে যায়:

price = 250.50   # ধনাত্মক দশমিক সংখ্যা
temperature = -4.5 # ঋণাত্মক দশমিক সংখ্যা
x = 5.0          # এটিও একটি float, কারণ শেষে .0 আছে

print(type(x))   # আউটপুট দেখাবে: <class 'float'>



২. বৈজ্ঞানিক প্রতীক বা Scientific Notation (e বা E)

খুব বড় বা খুব ছোট দশমিক সংখ্যাগুলোকে সহজে লেখার জন্য পাইথনে e বা E (Exponent) ব্যবহার করা যায়। এর মানে হলো 10-এর পাওয়ার বা ঘাত।

3e2 মানে হলো 3 * 10^2 = 300.0

5.5e-3 মানে হলো 5.5 * 10^-3 = 0.0055

big_num = 2.5e4    # ২.৫ এর সাথে ১০,০০০ গুণ (২৫০০০.০)
small_num = 1e-3   # ১ এর সাথে ০.০০১ গুণ (০.০০১)

print(big_num)     # আউটপুট: 25000.0
print(small_num)   # আউটপুট: 0.001




x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))

এই e বা E লেখা দেখলে একটু অদ্ভুত লাগতেই পারে। এটি আসলে গণিত এবং কম্পিউটারের একটি শর্টকাট লেখার নিয়ম, যাকে বলা হয় Scientific Notation (বৈজ্ঞানিক রূপ)।
ই e বা E এর মানে হলো "১০ এর পাওয়ার বা ঘাত" (10power)।

e এর পর যে সংখ্যাটি আছে, তার মানে হলো— "বাম পাশের সংখ্যার সাথে ১ লিখে ডান পাশের সংখ্যাটির সমপরিমাণ শূন্য গুণ করো।"

১. x = 35e3 এর মানে কী?
এখানে e3 মানে হলো 10 er upore 3 বা ১ এর পিঠে ৩টি শূন্য (1000)।

হিসাব: 35 * 1000 = 35000

পাইথন মেমোরিতে x এর মান ধরবে 35000.0।




২. y = 12E4 এর মানে কী?
ছোট হাতের e আর বড় হাতের E এর কাজে কোনো তফাৎ নেই, দুটিই এক। এখানে E4 মানে হলো 10 er upor 4 বা ১ এর পিঠে ৪টি শূন্য (10000)।

হিসাব: 12 * 10000 = 120000
অর্থাৎ, পাইথন মেমোরিতে y এর মান ধরবে 120000.0।

৩. z = -87.7e100 এর মানে কী?
এখানে e100 মানে হলো ১ এর পিঠে ১০০টি শূন্য! এত বড় সংখ্যা খাতায় লিখতে গেলে আপনার পুরো খাতা শেষ
হয়ে যাবে (যেমন: -87.7 * 10^er upore 100)।

এত বড় সংখ্যা যেন কষ্ট করে টাইপ করতে না হয়, সেজন্যই এই e শর্টকাটটি ব্যবহার করা হয়।

🔍 একটি জরুরি নোট (ডেটা টাইপ):

 যখন print(type(x)) রান করা হবে, তিনটির জন্যই আউটপুট আসবে <class 'float'>।

মনে খটকা লাগতে পারে— 35000 তো একটা পূর্ণসংখ্যা (Integer), তাহলে এটি float কেন হলো?

নিয়ম: পাইথনে যখনই কোনো সংখ্যার মাঝে এই বৈজ্ঞানিক e বা E ব্যবহার করা হবে, পাইথন তাকে অটোমেটিক Float (দশমিক সংখ্যা) হিসেবে ধরে নেয়।

💡 সহজে চেনার ট্রিক:
5e1 = ৫ এর পর ১টি শূন্য = 50.0

5e2 = ৫ এর পর ২টি শূন্য = 500.0

5e3 = ৫ এর পর ৩টি শূন্য = 5000.0

5000 না লিখে শেষে কেন .0 আসলো,

সহজ কথায়: পাইথনে এই বৈজ্ঞানিক e বা E চিহ্নটি তৈরিই করা হয়েছে বিজ্ঞানের জটিল ও নিখুঁত হিসাব-নিকাশ করার জন্য। আর বিজ্ঞানের বা ল্যাবের হিসেবে দশমিকের পরের অংশ অত্যন্ত গুরুত্বপূর্ণ।
পাইথন যখনই কোনো সংখ্যার সাথে e দেখে, সে ধরে নেয় এই সংখ্যাটি দিয়ে হয়তো অনেক বড় কোনো বৈজ্ঞানিক গণনা করা হবে, 
যেখানে সামান্য একটু ভুলের জন্যও বড় তফাৎ হয়ে যেতে পারে। তাই পাইথন এই সংখ্যার জাত বা ডেটা টাইপ বদলে পূর্ণসংখ্যা (Integer) থেকে সরাসরি দশমিক সংখ্যা (Float)-এ রূপান্তর করে ফেলে।


কম্পিউটারের মেমোরির নিয়ম (Data Type)
পাইথনে সাধারণ সংখ্যা (যেমন: 5000) হলো int। কিন্তু দশমিক ওয়ালা সংখ্যা (যেমন: 5000.0) হলো float।

যেহেতু পাইথন e দেখলেই তাকে float বানিয়ে দেয়, আর আমরা জানি যেকোনো float সংখ্যাকে স্ক্রিনে দেখাতে গেলে তার পিঠে একটা দশমিক এবং শূন্য (.0) দেখাতে হয়। তাই 5e3 এর আউটপুট 5000.0 আসে।

 যদি জোর করে .0 তাড়াতে চাওয়া হয় (Type Casting)
 কোডে যদি কোনো কারণে এই .0 দেখতে ভালো না লাগে এবং চাওয়া হয় ওটা খাঁটি পূর্ণসংখ্যা (Integer) হয়ে যাক, তবে int() ফাংশন ব্যবহার করে জোর করে .0 তাড়িয়ে দেওয়া যাবে:

x = 5e3      # এটি হলো 5000.0 (Float)
print(x)

# int() দিয়ে রূপান্তর করলে .0 হাওয়া হয়ে যাবে!
clean_x = int(x) 
print(clean_x) # আউটপুট আসবে: 5000

তাহলে মূল কথা হলো: e ব্যবহার করলেই পাইথন ওটাকে Float বা দশমিকের জাত বানিয়ে দেয়, আর সেই জাতের পরিচয় দেওয়ার জন্যই শেষে ওই .0 এসে বসে থাকে।



Float Variable তৈরি

price = 150.50
height = 5.8
weight = 62.75

print(price)
print(height)
print(weight)


Float তৈরির বিভিন্ন উপায়

# সরাসরি দশমিক দিয়ে
a = 3.14
b = -7.5
c = 0.001
d = 100.0      # পূর্ণ সংখ্যাও float হয় .0 দিলে

# বৈজ্ঞানিক নোটেশন (e notation)
e1 = 1.5e3     # 1.5 × 10³ = 1500.0
e2 = 2.5e-4    # 2.5 × 10⁻⁴ = 0.00025
e3 = 3e8       # আলোর গতি = 300000000.0

print(a, b, c, d)
print(e1, e2, e3)


# ফ্লোট ভেরিয়েবল ডিক্লেয়ারেশন
gpa = 3.91
pi = 3.1416


print("GPA:", gpa)
print("Value of PI:", pi)

print("-" * 30) # একটা সুন্দর ডিভাইডার লাইনের জন্য


print("GPA Data Type:", type(gpa))
print("PI Data Type:", type(pi))


print("-" * 30) -------------
এক লাইনে বললে—print("-" * 30) এর মানে হলো: স্ক্রিনে বা আউটপুটে একসাথে টানা ৩০টি মাইনাস বা ড্যাশ (-) চিহ্ন প্রিন্ট করো। প্রোগ্রামিংয়ের ভাষায় একে বলা হয় String Replication (স্ট্রিংয়ের পুনরাবৃত্তি)।

পাইথনে যখন কোনো টেক্সট বা স্ট্রিংয়ের সাথে গুণের চিহ্ন (*) এবং একটি সংখ্যা ব্যবহার করা হয়, তখন পাইথন গুণ করার বদলে ওই টেক্সটটাকে ততবার পরপর লিখে জোড়া লাগিয়ে দেয়।

এখানে কোডের দুটি অংশ আছে:
১. "-"  এটি একটি স্ট্রিং বা টেক্সট (ড্যাশ চিহ্ন)।
২. * 30 পাইথনকে বলা হচ্ছে, এই ড্যাশটাকে ৩০ বার গুণ করো (অর্থাৎ পুনরাবৃত্তি করো)।

যখন কনসোলে বা টার্মিনালে বড় কোনো আউটপুট দেখাতে চাওয়া হবে, তখন একটা তথ্যের সাথে আরেকটা তথ্য আলাদা করার জন্য বা দেখতে সুন্দর লাগার জন্য  
এইরকম ডিভাইডার লাইন (Divider Line) বা বর্ডার তৈরি করা হয়।


print("--- স্টুডেন্ট প্রোফাইল ---")
print("নাম: আবদুল্লাহ")
print("বয়স: ২৫")

# একটা সুন্দর বর্ডার দিয়ে নিচের তথ্য আলাদা করার জন্য:
print("-" * 30) 

print("সাবজেক্ট: প্রোগ্রামিং")
print("সিজিপিএ: ৩.৫০")

--- স্টুডেন্ট প্রোফাইল ---
নাম: আবদুল্লাহ
বয়স: ২৫
------------------------------
সাবজেক্ট: প্রোগ্রামিং
সিজিপিএ: ৩.৫০





পাইথনে যখন একটি পূর্ণসংখ্যাকে (int) আরেকটি পূর্ণসংখ্যা (int) দিয়ে সাধারণ ভাগ করা হয়, তখন আউটপুট সবসময় অটোমেটিক float (দশমিক) হয়ে যাবে। 

# সাধারণ ভাগ (Division)
result = 10 / 2
print(result)  
# আউটপুট আসবে: 5.0 (খেয়াল করুন, ৫ আসেনি, এটি float হয়ে গেছে!)
print(type(result)) # <class 'float'>


যদি দশমিক না চাওয়া হয় , অর্থাৎ একদম খাঁটি পূর্ণসংখ্যা (int) আউটপুট চাওয়া হয়, তবে পাইথনে ডাবল স্ল্যাশ // ব্যবহার করতে হয়, যাকে বলা হয় Floor Division। 

# পূর্ণসংখ্যার ভাগ (Floor Division)
integer_result = 10 // 2
print(integer_result)  
# আউটপুট আসবে: 5 (এবার এটি খাঁটি int)
print(type(integer_result)) # <class 'int'>


x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))





Float এর গাণিতিক অপারেশন

a = 10.5
b = 3.2

# মূল অপারেশন
print(a + b)    # 13.7   — যোগ
print(a - b)    # 7.3    — বিয়োগ
print(a * b)    # 33.6   — গুণ
print(a / b)    # 3.28125 — ভাগ
print(a // b)   # 3.0    — পূর্ণ ভাগ (ফলাফল float)
print(a % b)    # 0.8999... — ভাগশেষ
print(a ** 2)   # 110.25 — ঘাত

# int + float = সবসময় float
print(5 + 3.0)    # 8.0
print(10 * 2.5)   # 25.0


Float এর নির্ভুলতার সমস্যা

# বিখ্যাত সমস্যা — Floating Point Precision
print(0.1 + 0.2)         # 0.30000000000000004 ❌
print(0.1 + 0.2 == 0.3)  # False ❌

# সমাধান ১ — round() ব্যবহার
result = round(0.1 + 0.2, 2)
print(result)             # 0.3 ✅
print(result == 0.3)      # True ✅

# সমাধান ২ — math.isclose() ব্যবহার
import math
print(math.isclose(0.1 + 0.2, 0.3))   # True ✅

# সমাধান ৩ — Decimal মডিউল
from decimal import Decimal
x = Decimal('0.1') + Decimal('0.2')
print(x)              # 0.3 ✅
print(x == Decimal('0.3'))   # True ✅



Float ফরম্যাটিং (সুন্দরভাবে দেখানো)

pi = 3.14159265358979

# দশমিকের পরে কত ঘর দেখাবে
print(f"{pi:.2f}")    # 3.14   (২ ঘর)
print(f"{pi:.4f}")    # 3.1416 (৪ ঘর)
print(f"{pi:.0f}")    # 3      (০ ঘর)

# হাজার বিভাজক
big = 1234567.891
print(f"{big:,.2f}")     # 1,234,567.89

# শতাংশ
ratio = 0.8567
print(f"{ratio:.1%}")    # 85.7%

# বৈজ্ঞানিক নোটেশনে
small = 0.000123
print(f"{small:.2e}")    # 1.23e-04

# round() ফাংশন
x = 3.7689
print(round(x))      # 4      (নিকটতম পূর্ণ সংখ্যা)
print(round(x, 1))   # 3.8    (১ দশমিক)
print(round(x, 2))   # 3.77   (২ দশমিক)


Type Conversion (রূপান্তর)

# int → float
a = float(10)
print(a)          # 10.0
print(type(a))    # <class 'float'>

# string → float
b = float("3.14")
print(b)          # 3.14

b2 = float("1.5e3")
print(b2)         # 1500.0

# float → int (দশমিক কেটে যাবে)
c = int(9.99)
print(c)          # 9 (রাউন্ড হয় না, কাটা যায়)

# সঠিকভাবে রাউন্ড করে int
d = round(9.99)
print(d)          # 10 ✅

# bool → float
print(float(True))    # 1.0
print(float(False))   # 0.0


Float তুলনা করা

a = 5.0
b = 5

# float ও int তুলনা
print(a == b)     # True (মান সমান)
print(a is b)     # False (একই object নয়)

# নিরাপদ তুলনা
import math
x = 0.1 + 0.2
y = 0.3

# সরাসরি তুলনা — বিপজ্জনক
print(x == y)                    # False ❌

# isclose() দিয়ে তুলনা — নিরাপদ
print(math.isclose(x, y))        # True ✅

# নিজে tolerance দিয়ে
print(math.isclose(x, y, rel_tol=1e-9))  # True ✅



------------------------------------
💰 ব্যাংকিং সিস্টেম

from decimal import Decimal, ROUND_HALF_UP

class BankAccount:
    def __init__(self, name, balance=0.0):
        self.name = name
        self.balance = Decimal(str(balance))

    def deposit(self, amount):
        self.balance += Decimal(str(amount))
        print(f"জমা: ৳{amount:.2f}")

    def withdraw(self, amount):
        amount = Decimal(str(amount))
        if amount > self.balance:
            print("❌ পর্যাপ্ত টাকা নেই!")
        else:
            self.balance -= amount
            print(f"উত্তোলন: ৳{amount:.2f}")

    def show_balance(self):
        print(f"💰 {self.name} এর ব্যালেন্স: ৳{self.balance:.2f}")


account = BankAccount("Rahim", 1000.00)
account.deposit(500.50)
account.withdraw(200.75)
account.show_balance()



🌡️ তাপমাত্রা রূপান্তর

def celsius_to_fahrenheit(c):
    return round((c * 9/5) + 32, 2)

def fahrenheit_to_celsius(f):
    return round((f - 32) * 5/9, 2)

def celsius_to_kelvin(c):
    return round(c + 273.15, 2)

temps = [0.0, 25.5, 37.0, 100.0, -10.5]

print(f"{'Celsius':>10} {'Fahrenheit':>12} {'Kelvin':>10}")
print("-" * 35)
for c in temps:
    f = celsius_to_fahrenheit(c)
    k = celsius_to_kelvin(c)
    print(f"{c:>10.1f} {f:>12.2f} {k:>10.2f}")


📐 বৃত্তের হিসাব
import math

def circle_info(radius: float):
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    diameter = 2 * radius

    print(f"বৃত্তের তথ্য (ব্যাসার্ধ = {radius})")
    print(f"  ব্যাস       : {diameter:.4f}")
    print(f"  পরিধি      : {circumference:.4f}")
    print(f"  ক্ষেত্রফল  : {area:.4f}")

circle_info(5.0)
circle_info(12.75)

-----------------------------------------

✅ সাধারণ হিসাবে → float ব্যবহার 
✅ টাকার হিসাবে → Decimal ব্যবহার
✅ তুলনায় → math.isclose() ব্যবহারো
✅ দেখাতে → f-string এ :.2f ব্যবহার


ফ্লোটের একটি অদ্ভুত সমস্যা (Floating Point Precision Issue)
কম্পিউটার  দশমিক সংখ্যাগুলোকে ব্যাকএন্ডে বাইনারি (০ এবং ১) আকারে জমা রাখে। কিছু কিছু দশমিক সংখ্যাকে বাইনারিতে নিখুঁতভাবে প্রকাশ করা যায় না 
(যেমনটা 1 কে 3 দিয়ে ভাগ করলে 0.3333... পাই, যা কখনো শেষ হয় না)।
এই কারণে পাইথনে ফ্লোট সংখ্যা নিয়ে কাজ করার সময় মাঝে মাঝে সামান্য একটু গরমিল দেখা যায়:

print(0.1 + 0.2)  
#  মনে হতে পারে উত্তর আসবে 0.3
# কিন্তু আউটপুট আসবে: 0.30000000000000004

পাইথনের এই দশমিকের সামান্য গরমিল (যেমন: 0.1 + 0.2 করলে 0.30000000000000004 আসা) সমাধান করার জন্য সবচেয়ে সেরা এবং প্রফেশনাল উপায় হলো পাইথনের বিল্ট-ইন decimal মডিউল ব্যবহার করা।

১: decimal মডিউল ব্যবহার করা (সবচেয়ে নিখুঁত উপায়)

টাকা-পয়সার হিসাব, ব্যাংকিং সফটওয়্যার বা যেকোনো গুরুত্বপূর্ণ ক্যালকুলেশনের জন্য এটি ব্যবহার করা হয়। এখানে সংখ্যাগুলোকে সাধারণ ফ্লোটের বদলে স্ট্রিং (" ") আকারে পাস করতে হয়,
যাতে পাইথন শুরুতেই কোনো বাইনারি গরমিল করতে না পারে।


from decimal import Decimal

# সাধারণ ফ্লোটের সমস্যা
print("সাধারণ ফ্লোট:", 0.1 + 0.2) 
# আউটপুট: 0.30000000000000004

# ডেসিমাল মডিউল দিয়ে সমাধান
num1 = Decimal("0.1")
num2 = Decimal("0.2")
result = num1 + num2

print("ডেসিমাল মডিউল:", result)  
# আউটপুট আসবে একদম নিখুঁত: 0.3



২: round() ফাংশন ব্যবহার করা (সহজ ট্রিক)

যদি কোনো বড় লাইব্রেরি ইমপোর্ট করতে ইচ্ছা না করে এবং শুধু ডিসপ্লে বা আউটপুট সুন্দর করার জন্য নিখুঁত মান চাওয়া হয়, তবে round() ফাংশন ব্যবহার করতে হবে।

# যোগ করার পর দশমিকের পর ১ বা ২ ঘর পর্যন্ত রাউন্ড করে নেওয়া
total = 0.1 + 0.2
perfect_total = round(total, 1)

print("রাউন্ড করার পর:", perfect_total)  
# আউটপুট আসবে: 0.3


৩: math.isclose() (শর্ত বা ইফ-এলসের ভেতর তুলনা করতে)

ফ্লোটের এই গরমিলের কারণে যদি সরাসরি if (0.1 + 0.2 == 0.3): লিখা হয়, তবে পাইথন বলবে False (মিথ্যা)। এই শর্ত পরীক্ষা করার জন্য পাইথনের math.isclose() ফাংশন ব্যবহার করতে হয়।

import math

a = 0.1 + 0.2
b = 0.3

# সরাসরি তুলনা করলে ভুল আসবে
print(a == b)  # আউটপুট: False

# সঠিক নিয়ম: math.isclose ব্যবহার করা
print(math.isclose(a, b))  # আউটপুট আসবে: True (কারণ এরা প্রায় সমান)

সহজ কথা: সাধারণ কাজের জন্য round() ব্যবহার করলেই চলে, তবে হিসাব যদি হয় টাকা-পয়সার, তবে সবসময় Decimal ব্যবহার করাই নিয়ম।


স্পেশাল ফ্লোট ভ্যালু (Special Float Values)
পাইথনে ফ্লোট টাইপের তিনটি বিশেষ মান রয়েছে, যা গাণিতিক অসাধারণ পরিস্থিতিতে ব্যবহৃত হয়:

float('inf'): পজিটিভ ইনফিনিটি বা অসীম সংখ্যা।

float('-inf'): নেগেটিভ ইনফিনিটি।

float('nan'): Not a Number (যখন কোনো গাণিতিক ফল সংজ্ঞায়িত করা যায় না)।

import math

infinity = float('inf')
print(infinity > 99999999)  # আউটপুট: True (কারণ অসীম সব সংখ্যার চেয়ে বড়)

not_a_number = float('nan')
print(math.isnan(not_a_number)) # আউটপুট: True





দশমিক নির্ভুলতা

print(math.floor(3.9))   # নিচের পূর্ণসংখ্যা → ৩
math.floor() ফাংশনটি যেকোনো দশমিক সংখ্যাকে তার নিচের নিকটতম পূর্ণসংখ্যায় (Integer) রাউন্ড বা নামিয়ে দেয়।
3.9, এর নিচের নিকটতম পূর্ণসংখ্যাটি হলো 3 (দশমিকের পরের অংশ বাদ পড়ে যাবে)।

import math

# math.floor() এর ব্যবহার
number = 3.9
result = math.floor(number)

print("Original Number:", number)
print("Floor Output:", result)




print(math.ceil(3.1))  # উপরের পূর্ণসংখ্যা → ৪
math.ceil() ফাংশনটি (Ceiling থেকে এসেছে) যেকোনো দশমিক সংখ্যাকে তার উপরের নিকটতম পূর্ণসংখ্যায় (Integer) তুলে বা বাড়িয়ে দেয়।
ইনপুট 3.1, এটি দশমিকের পর যেকোনো ছোট মান থাকা সত্ত্বেও তার উপরের পূর্ণসংখ্যা 4-এ রূপান্তর হয়ে যাবে।

import math

# math.ceil() এর ব্যবহার
number = 3.1
result = math.ceil(number)

print("Original Number:", number)
print("Ceil Output:", result)



print(math.trunc(3.9))   # দশমিক অংশ বাদ → ৩
math.trunc() ফাংশনটি (Truncate থেকে এসেছে) কাজ করে খুবই সোজা নিয়মে—এটি সংখ্যাটি ধনাত্মক হোক বা ঋণাত্মক, যেকোনো দশমিকের পরের অংশকে সরাসরি কেটে ফেলে বাদ দিয়ে দেয়।

কোনো রাউন্ডিং (Rounding) বা ছোট-বড় করার ঝামেলায় এটি যায় না।

import math

number = 3.9
result = math.trunc(number)

print("Original Number:", number)
print("Trunc Output:", result)






# ৩. বিশেষ মান
print(float('inf'))      # ইনফিনিটি 
float('inf') হলো পাইথনের একটি বিশেষ মান, যা অসীম বা Infinity নির্দেশ করে। এর কোনো নির্দিষ্ট গাণিতিক সীমা নেই—এটি যেকোনো সংখ্যার চেয়ে বড়।


# ইনফিনিটি তৈরি ও তুলনা
positive_infinity = float('inf')

print("Output Value:", positive_infinity)
print("Type:", type(positive_infinity))

# যেকোনো বড় সংখ্যার সাথে তুলনা
big_number = 10**300
print("Is Inf greater than 10^300?", positive_infinity > big_number)



print(float('-inf'))     # নেগেটিভ ইনফিনিটি 
float('-inf') হলো পাইথনের ঋণাত্মক অসীম (Negative Infinity)। এটি ধনাত্মক বা যেকোনো বাস্তব সংখ্যার চেয়ে ছোট এবং গণিতের সবচেয়ে ছোট মান হিসেবে বিবেচিত হয়।

# নেগেটিভ ইনফিনিটি তৈরি ও তুলনা
negative_infinity = float('-inf')

print("Output Value:", negative_infinity)
print("Type:", type(negative_infinity))

# যেকোনো ছোট বা বড় ঋণাত্মক সংখ্যার সাথে তুলনা
very_small_num = -10**300
print("Is -inf smaller than -10^300?", negative_infinity < very_small_num)


Output Value: -inf
Type: <class 'float'>
Is -inf smaller than -10^300? True





print(float('nan'))      # NaN (Not a Number)
float('nan') হলো পাইথনে NaN বা "Not a Number"। এটি একটি বিশেষ ভাসমান সংখ্যা (Floating-point representation), যা এমন কোনো সংখ্যাকে নির্দেশ করে যা অসংজ্ঞায়িত (Undefined) বা গাণিতিকভাবে অসম্ভব।
যেমন: অসীমকে অসীম দিয়ে ভাগ করা (infty / infty) অথবা শূন্যকে শূন্য দিয়ে ভাগ করা (0 / 0)।


import math

nan_value = float('nan')

print("Output Value:", nan_value)
print("Type:", type(nan_value))

# NaN এর একটি বিশেষ বৈশিষ্ট্য!
print("Is NaN equal to NaN?", nan_value == nan_value)
print("Is NaN equal using math.isnan()?", math.isnan(nan_value))





Float Random Number:

Security ছাড়া (Insecure/Normal Random Float)

import random

# 0.0 থেকে 1.0 এর মধ্যে র‍্যান্ডম ফ্লোট
normal_float = random.random()
print("Normal (insecure) float:", normal_float)

# নির্দিষ্ট রেঞ্জের মধ্যে (যেমন 1.5 থেকে 9.5)
normal_range = random.uniform(1.5, 9.5)
print("Normal (insecure) range:", normal_range)


আউটপুট (প্রতিবার ভিন্ন হবে):

Normal (insecure) float: 0.7342156789234567
Normal (insecure) range: 6.291837465123456

এটা random মডিউলের Mersenne Twister অ্যালগরিদম ব্যবহার করে, যা প্রেডিক্টেবল এবং security-sensitive কাজের জন্য উপযুক্ত না।




Security সহ (Secure/Cryptographic Random Float)

import secrets

secure_rng = secrets.SystemRandom()

# 0.0 থেকে 1.0 এর মধ্যে সিকিউর র‍্যান্ডম ফ্লোট
secure_float = secure_rng.random()
print("Secure float:", secure_float)

# নির্দিষ্ট রেঞ্জের মধ্যে (যেমন 1.5 থেকে 9.5)
secure_range = secure_rng.uniform(1.5, 9.5)
print("Secure range:", secure_range)

আউটপুট (প্রতিবার ভিন্ন হবে):

Secure float: 0.4821937465012389
Secure range: 3.847562910384756

এটা অপারেটিং সিস্টেমের CSPRNG (/dev/urandom বা CryptGenRandom) থেকে র‍্যান্ডমনেস নেয়, 
যা প্রেডিক্ট করা প্র্যাক্টিক্যালি অসম্ভব — তাই পাসওয়ার্ড, টোকেন, OTP জেনারেট করার জন্য এটাই ব্যবহার করা উচিত।

