int হলো Python-এর পূর্ণসংখ্যা (Integer) ডেটা টাইপ। Python-এ int বা Integer ডেটা টাইপ বলতে মূলত পূর্ণসংখ্যা বোঝায়। অর্থাৎ, যেকোনো ধনাত্মক (positive), ঋণাত্মক (negative) বা শূন্য (zero) সংখ্যা—
যার মধ্যে কোনো দশমিক অংশ থাকে না, তা-ই হলো int।

int (Integer) এটি সম্পূর্ণ Immutable (অপরিবর্তনযোগ্য)।



যেমন: ১০, -৫, ০, ১২৩৪৫৬ ইত্যাদি সবই Python-এ Integer।


Python-এ int-এর আকারের কোনো সীমা নেই— যত বড় সংখ্যাই দেওয়া হক না কেন, Python তা ধরে রাখতে পারে (শুধু মেমোরি থাকতে হবে)।

Python-এ ইন্টিজার ভেরিয়েবল তৈরি করা খুবই সহজ। আপনাকে কোনো ডাটা টাইপ নির্দিষ্ট করে দিতে হয় না:

a = 25       # ধনাত্মক পূর্ণসংখ্যা
b = -105     # ঋণাত্মক পূর্ণসংখ্যা
c = 0        # শূন্য





C বা Java-র মতো ল্যাঙ্গুয়েজে যেখানে একটি সাধারণ ইন্টিজার রাখতে মাত্র ৪ বাইট (৩২ বিট) বা ৮ বাইট (৬৪ বিট) জায়গা লাগে, 
সেখানে Python ৩-এ একটি সাধারণ 0 বা 25 এর মতো ছোট সংখ্যা মেমোরিতে রাখতেও ২৮ বাইট (২২৪ বিট) জায়গা নেয়।

কেন এত বেশি জায়গা লাগে? (The Overhead)
Python-এ সবকিছুই আসলে এক একটি Object (অবজেক্ট)।  যখন x = 25 লিখা হয়, Python মেমোরিতে শুধু 25 সংখ্যাটি রাখে না, বরং সেই সংখ্যার সাথে আরও অনেক অতিরিক্ত তথ্য (Metadata) গুছিয়ে রাখে।

CPython (Python-এর অফিশিয়াল ইমপ্লিমেন্টেশন)-এর ব্যাকএন্ডে একটি int অবজেক্ট মূলত ৪টি জিনিস নিয়ে তৈরি হয়:

১. ob_refcnt (৮ বাইট): এটি হলো রেফারেন্স কাউন্ট। এই অবজেক্টটি কোডের কয়টি জায়গায় ব্যবহৃত হচ্ছে, Python তার হিসাব রাখে (Garbage Collection-এর জন্য)।
২. ob_type (৮ বাইট): এটি একটি পয়েন্টার, যা নির্দেশ করে এটি কী ধরনের অবজেক্ট (যেমন এখানে এটি যে <class 'int'>, সেই তথ্য)।
৩. ob_size (৮ বাইট): সংখ্যাটি কত বড় এবং সাইন কী (পজিটিভ নাকি নেগেটিভ), তা ধারণ করে।
৪. ob_digit (৪ বাইট): এই অংশে আসল সংখ্যাটি (যেমন: 25) বাইনারি আকারে জমা থাকে।

তাহলে মোট হিসাবটি দাঁড়ায়:
৮ বাইট + ৮ বাইট + ৮ বাইট + ৪ বাইট = ২৮ বাইট (২২৪ বিট)





Python-এর বিল্ট-ইন sys মডিউলের getsizeof() ফাংশন ব্যবহার করে যেকোনো ভেরিয়েবল মেমোরিতে কত বাইট জায়গা নিচ্ছে তা সরাসরি দেখা যায়:

import sys

# শূন্য (0) এর জন্য সাইজ পরীক্ষা
print(sys.getsizeof(0))   # আউটপুট আসবে: 28 (বাইট)

# ২৫ এর জন্য সাইজ পরীক্ষা
print(sys.getsizeof(25))  # আউটপুট আসবে: 28 (বাইট)


যেহেতু Python-এ ইন্টিজারের সাইজ ফিক্সড না (Arbitrary Precision), তাই সংখ্যা যত বড় হতে থাকে, Python মেমোরিতে ob_digit-এর জন্য ৪ বাইট করে জায়গা বাড়াতে থাকে।

sys.getsizeof(0) --- 28 Bytes
sys.getsizeof(230) -- 32 Bytes (সংখ্যাটি বড় হওয়ায় আরও ৪ বাইট যোগ হয়েছে)

sys.getsizeof(260) --- 36 Bytes





অন্যান্য প্রোগ্রামিং ল্যাঙ্গুয়েজে (যেমন C, C++ বা Java) ইন্টিজারের একটি নির্দিষ্ট সীমা থাকে (যেমন ৩২-বিট বা ৬৪-বিট)। কিন্তু Python 3-এ ইন্টিজারের কোনো নির্দিষ্ট মেমোরি লিমিট নেই!

# আপনি চাইলে যত খুশি বড় সংখ্যা লিখতে পারেন:
huge_number = 1234567890123456789012345678901234567890
print(type(huge_number))  # এটিও <class 'int'> দেখাবে





বড় সংখ্যা সহজে পড়ার ট্রিক (Underscores in Numbers)

যখন অনেক বড় কোনো সংখ্যা দেওয়া হবে, তখন পড়ার সুবিধার জন্য সংখ্যাগুলোর মাঝে আন্ডারস্কোর (_) ব্যবহার করা যাবে। Python হিসাব করার সময় এই আন্ডারস্কোরগুলোকে ইগনোর বা উপেক্ষা করে।

money = 10_00_000  # পড়ার সুবিধার্থে ১ লাখ এভাবে লেখা হয়েছে
print(money)       # আউটপুট দেখাবে: 1000000



int যেভাবে লিখা লাগে?

a = 10          # ধনাত্মক পূর্ণসংখ্যা
b = -5          # ঋণাত্মক পূর্ণসংখ্যা
c = 0           # শূন্য
d = 1_000_000   # আন্ডারস্কোর দিয়ে বড় সংখ্যা পড়তে সহজ (Python এটা 1000000 ধরবে)
e = 0b1010      # বাইনারি (২-ভিত্তিক) → ১০
f = 0o12        # অক্টাল (৮-ভিত্তিক) → ১০
g = 0xA         # হেক্সাডেসিমেল (১৬-ভিত্তিক) → ১০




int-এর বৈশিষ্ট্য

ইমিউটেবল (Immutable)	একবার তৈরি হলে পরিবর্তন করা যায় না। নতুন ভ্যালু দিলে নতুন অবজেক্ট তৈরি হয়।
আকারের সীমা নেই	C, Java-র মতো সীমা নেই (যেমন: ২৩২-১)। আপনি চাইলে ১০০০ ডিজিটের সংখ্যাও রাখতে পারেন।
যেকোনো ভিত্তিতে লেখা যায়	বাইনারি (0b), অক্টাল (0o), হেক্সাডেসিমেল (0x)




int-এর অপারেশন (গাণিতিক কাজ)

a = 10
b = 3

print(a + b)    # যোগ → 13
print(a - b)    # বিয়োগ → 7
print(a * b)    # গুণ → 30
print(a / b)    # ভাগ (float রিটার্ন করে) → 3.333...
print(a // b)   # পূর্ণসংখ্যা ভাগ (floor division) → 3
print(a % b)    # ভাগশেষ (modulus) → 1
print(a ** b)   # পাওয়ার (ঘাত) → 10^3 = 1000
print(-a)       # নেগেটিভ → -10
print(abs(-a))  # পরম মান → 10



int vs float (পার্থক্য)

বিষয়	       int	     float

দশমিক	     নেই	     আছে
মেমোরি	     কম	     বেশি
স্পিড	       দ্রুত	     ধীর
JSON-এ	     সংখ্যা	     সংখ্যা
কখন ব্যবহার করবেন?	ID, বয়স, কাউন্ট, পেজ          	দাম, রেটিং, ট্যাক্স




ডিভিশন বা ভাগের ক্ষেত্রে সতর্কতা (Division behavior)

পাইথনে দুটি ইন্টিজার সংখ্যাকে ভাগ করলে আউটপুট সবসময় একটি float (দশমিক সংখ্যা) আসে, এমনকি ভাগফল মিলে গেলেও।

result = 10 / 2
print(result) # আউটপুট: 5.0 (এটি float)



যদি ভাগফলের দশমিক অংশ বাদ দিয়ে শুধু পূর্ণসংখ্যাটি আসুক (Integer Division), তবে  দুটি স্ল্যাশ (//) ব্যবহার করতে হবে:

result = 10 // 2
print(result) # আউটপুট: 5 (এটি int)



Unlimited Precision (অসীম নির্ভুলতা)

# Python-এ int-এর কোনো সীমা নেই (C/C++/Java-এর মতো নয়)
small_number = 42
big_number = 10**100  # 1 এর সাথে 100টি শূন্য
huge_number = 10**1000  # 1 এর সাথে 1000টি শূন্য - Python এটা হ্যান্ডেল করতে পারে!

print(f"Small: {small_number}")
print(f"Big: {big_number}")
print(f"Huge: {huge_number}")

# Memory ব্যবহারের পরিমাণ
import sys
print(f"Small number memory: {sys.getsizeof(small_number)} bytes")
print(f"Big number memory: {sys.getsizeof(big_number)} bytes")
print(f"Huge number memory: {sys.getsizeof(huge_number)} bytes")



Immutable (অপরিবর্তনীয়)

# int immutable - মান পরিবর্তন করা যায় না
x = 10
print(f"x এর address: {id(x)}")

x = x + 5  # নতুন int object তৈরি হয়
print(f"x এর নতুন address: {id(x)}")

# পুরনো object অপরিবর্তিত থাকে (গারবেজ কালেক্টর মুছে ফেলে)






int Operations (গাণিতিক অপারেশন)
Basic Arithmetic

a = 10
b = 3

# Addition
print(f"Addition: {a + b}")  # 13

# Subtraction
print(f"Subtraction: {a - b}")  # 7

# Multiplication
print(f"Multiplication: {a * b}")  # 30

# Division (ফলাফল float হয়)
print(f"Division: {a / b}")  # 3.3333333333333335

# Floor Division (পূর্ণসংখ্যা বিভাজন)
print(f"Floor Division: {a // b}")  # 3

# Modulus (ভাগশেষ)
print(f"Modulus: {a % b}")  # 1

# Exponentiation (পাওয়ার)
print(f"Power: {a ** b}")  # 1000

# Negative numbers
print(f"Negative: {-a}")  # -10
print(f"Absolute: {abs(-10)}")  # 10





Bitwise Operations (বিটওয়াইজ অপারেশন)

a = 5  # 0101
b = 3  # 0011

# AND (&)
print(f"AND: {a & b}")  # 1 (0001)

# OR (|)
print(f"OR: {a | b}")  # 7 (0111)

# XOR (^)
print(f"XOR: {a ^ b}")  # 6 (0110)

# NOT (~)
print(f"NOT: {~a}")  # -6

# Left Shift (<<)
print(f"Left Shift: {a << 1}")  # 10 (1010)

# Right Shift (>>)
print(f"Right Shift: {a >> 1}")  # 2 (0010)

# Bitwise operations in binary format
print(f"Binary of 5: {bin(5)}")  # 0b101
print(f"Binary of 3: {bin(3)}")  # 0b11
print(f"5 & 3: {bin(5 & 3)}")  # 0b1





Comparison Operations

a = 10
b = 20

# Equal to
print(f"Equal: {a == b}")  # False

# Not equal to
print(f"Not equal: {a != b}")  # True

# Greater than
print(f"Greater: {a > b}")  # False

# Less than
print(f"Less: {a < b}")  # True

# Greater than or equal
print(f"Greater or equal: {a >= b}")  # False

# Less than or equal
print(f"Less or equal: {a <= b}")  # True

# Chained comparison
x = 5
print(f"1 < x < 10: {1 < x < 10}")  # True
print(f"1 < x < 3: {1 < x < 3}")  # False




int Methods এবং Built-in Functions

Conversion Methods

num = 42

# বিভিন্ন বেসে কনভার্ট
print(f"Binary: {bin(num)}")      # 0b101010
print(f"Octal: {oct(num)}")       # 0o52
print(f"Hexadecimal: {hex(num)}")  # 0x2a

# String representation
print(f"String: {str(num)}")      # '42'

# Format with different bases
print(f"Binary format: {format(num, 'b')}")   # 101010
print(f"Octal format: {format(num, 'o')}")    # 52
print(f"Hex format: {format(num, 'x')}")      # 2a
print(f"Hex uppercase: {format(num, 'X')}")   # 2A


Type Checking

# isinstance() ব্যবহার
num = 42
print(f"Is int: {isinstance(num, int)}")  # True
print(f"Is float: {isinstance(num, float)}")  # False
print(f"Is number: {isinstance(num, (int, float))}")  # True

# type() ব্যবহার
print(f"Type: {type(num)}")  # <class 'int'>
print(f"Is type int: {type(num) == int}")  # True


Mathematical Functions

import math

num = -42.7

# Absolute value
print(f"Absolute: {abs(num)}")  # 42.7

# Power
print(f"Power: {pow(2, 10)}")  # 1024

# Square root
print(f"Square root: {math.sqrt(16)}")  # 4.0

# Factorial
print(f"Factorial: {math.factorial(5)}")  # 120

# GCD (Greatest Common Divisor)
print(f"GCD: {math.gcd(12, 18)}")  # 6

# Ceiling and Floor
print(f"Ceiling: {math.ceil(3.14)}")  # 4
print(f"Floor: {math.floor(3.14)}")  # 3


Naming Conventions

# ✅ ভালো প্র্যাকটিস
user_age = 25
total_count = 100
MAX_LIMIT = 1000  # Constants uppercase

# ❌ খারাপ প্র্যাকটিস
a = 25  # অর্থহীন নাম
UserAge = 25  # ক্যামেল কেস (Python-এ স্নেক কেস ব্যবহার)



🔢 ৪টি ভিন্ন নাম্বারিং সিস্টেম (Number Systems)
Binary (বাইনারি - ২ ভিত্তিক):
Octal (অক্টাল - ৮ ভিত্তিক):
Hexadecimal (হেক্সাডেসিমাল - ১৬ ভিত্তিক):
পাইথনের int শুধু চেনা ডেসিমাল (১০ ভিত্তিক) সংখ্যাই নয়, বরং বাইনারি, অক্টাল বা হেক্সাডেসিমাল সংখ্যাকেও রিপ্রেজেন্ট করতে পারে। সাইবার সিকিউরিটির জন্য এটি জানা খুব দরকারী:





random কী?

random হলো Python-এর একটি বিল্ট-ইন মডিউল যা র‍্যান্ডম (অনির্দিষ্ট/যাদৃচ্ছ) সংখ্যা তৈরি করার জন্য ব্যবহৃত হয়।

এটি কোনো ডেটা টাইপ নয়, এটি একটি মডিউল (লাইব্রেরি)।

গেম, সিমুলেশন, লটারি, টেস্টিং, ডেটা সায়েন্স—সব জায়গায় কাজে লাগে।

সিকিউরিটি-সংবেদনশীল কাজে (পাসওয়ার্ড, টোকেন) random ব্যবহার না—সেই কাজে secrets মডিউল ব্যবহার করা লাগবে।

