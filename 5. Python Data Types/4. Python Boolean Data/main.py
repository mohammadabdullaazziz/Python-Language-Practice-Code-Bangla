পাইথনে Boolean (বুলিয়ান) ডেটা টাইপ হলো এমন একটি বিল্ট-ইন ডেটা টাইপ যা কেবল দুটি মান (Value) প্রকাশ করতে পারে: True (সত্য) এবং False (মিথ্যা). 
প্রোগ্রামিংয়ে কোনো শর্ত বা কন্ডিশন পরীক্ষা করার জন্য এটি ব্যবহার করা হয়. পাইথনে এই ডেটা টাইপকে সংক্ষেপে bool বলা হয়.

পাইথনের কেস-সেন্সিটিভিটির কারণে বুলিয়ান লেখার সময় সব সময় প্রথম অক্ষর বড় হাতের (True এবং False) হতে হবে। ছোট হাতের true বা false লিখলে পাইথন এরর (Error) দেখাবে।

পাইথনের bool() ফাংশন দিয়ে যেকোনো মান সত্য নাকি মিথ্যা তা যাচাই করা যায়.

Python-এ True ও False হলো রিজার্ভেড কীওয়ার্ড (সংরক্ষিত শব্দ)।

এই টাইপের নাম bool, এবং এটি নামকরণ করা হয়েছে গণিতবিদ George Boole-এর নামে, যিনি Boolean Algebra তৈরি করেছিলেন।


x = True
y = False

print(type(x))  # <class 'bool'>
print(type(y))  # <class 'bool'>






bool যেভাবে লিখা লাগবে?

# সরাসরি বুলিয়ান মান
is_active = True
is_deleted = False
is_verified = True

# কন্ডিশন থেকে বুলিয়ান
age = 18
is_adult = age >= 18  # True
is_child = age < 10   # False

# টাইপ চেক
print(type(is_active))  # <class 'bool'>




bool-এর বৈশিষ্ট্য

মাত্র ২টি মান  	True বা False
ইমিউটেবল	পরিবর্তন করা যায় না (কিন্তু নতুন ভ্যালু অ্যাসাইন করা যায়)
সংখ্যা হিসেবে	True = 1, False = 0 (গাণিতিক অপারেশনেও কাজ করে)
কেস সংবেদনশীল	true/false কাজ করে না (ছোট হাতের হবে না)




Boolean আসলে Integer-এর subclass
Python-এ bool টাইপটি int টাইপের একটি subclass। অর্থাৎ:

True = 1
False = 0

print(True + True)      # 2
print(True == 1)        # True
print(False == 0)       # True
print(True + 5)         # 6





ফালসি (Falsy) উপাদানসমূহ (যা bool() করলে False আসবে):

শূন্য সংখ্যা: 0, 0.0

খালি টেক্সট বা উপাদান: "" (খালি স্ট্রিং), [] (খালি লিস্ট), {} (খালি ডিকশনারি)

বিশেষ মান: None

print(bool(0))       # False
print(bool(""))      # False
print(bool([]))      # False
print(bool(None))    # False

False             False

0, 0.0            False

"" (খালি string)   False

[] (খালি list)     False

() (খালি tuple)    False

{} (খালি dict/set) False

None               False


print(bool(None))      # False
print(bool(False))     # False
print(bool(0))         # False (শূন্য)
print(bool(0.0))       # False
print(bool(""))        # False (খালি স্ট্রিং)
print(bool([]))        # False (খালি লিস্ট)
print(bool(()))        # False (খালি টাপল)
print(bool({}))        # False (খালি ডিকশনারি)
print(bool(set()))     # False (খালি সেট)





ট্রুথি (Truthy) উপাদানসমূহ (যা bool() করলে True আসবে):

শূন্য ছাড়া যেকোনো সংখ্যা: 1, -5, 3.14

যেকোনো লেখা বা ভরা উপাদান: "Hello", [1, 2], {"a": 1}

print(bool(1))         # True
print(bool(-5))        # True
print(bool("hello"))   # True
print(bool([1, 2]))    # True
print(bool(" "))       # True (স্পেসও একটা character)


print(bool(1))         # True
print(bool(-5))        # True
print(bool(3.14))      # True
print(bool("Hello"))   # True
print(bool([1, 2]))    # True
print(bool((1, 2)))    # True
print(bool({"a": 1}))  # True
print(bool({1, 2}))    # True




bool-এর অপারেশন (লজিক্যাল অপারেটর)

একাধিক বুলিয়ান মানকে একসাথে জুড়ে দিয়ে বড় সিদ্ধান্ত নেওয়ার জন্য তিনটি অপারেটর ব্যবহার করা হয়:

and (এবং): যদি সবগুলো শর্ত সত্য হয়, তবেই ফলাফল True হবে।

or (অথবা): যেকোনো একটি শর্ত সত্য হলেই ফলাফল True হবে।

not (না): এটি সত্যকে মিথ্যা এবং মিথ্যাকে সত্য বানিয়ে দেয় (উল্টে দেয়)।

has_ticket = True
has_nid = False

# and অপারেটর (দুটিই সত্য হতে হবে)
print(has_ticket and has_nid)  # আউটপুট: False (যেহেতু একটি False)

# or অপারেটর (যেকোনো একটি সত্য হলেই হবে)
print(has_ticket or has_nid)   # আউটপুট: True

# not অপারেটর (উল্টে দেওয়া)
print(not has_ticket)          # আউটপুট: False (সত্যকে মিথ্যা বানালো)





বুলিয়ান অপারেটর (Logical Operators)
বুলিয়ান লজিক নিয়ে কাজ করার জন্য পাইথনে তিনটি প্রধান অপারেটর রয়েছে:

and: দুটি শর্তই সত্য হলে True দেয়। 
or: যেকোনো একটি শর্ত সত্য হলেই True দেয়।
not: সত্যকে মিথ্যা এবং মিথ্যাকে সত্যে পরিবর্তন করে।

x = True
y = False

print(x and y)  # আউটপুট: False
print(x or y)   # আউটপুট: True
print(not x)    # আউটপুট: False


a = True
b = False

# ১. AND (দুটোই True হলে True)
print(a and b)  # False
print(a and True)  # True

# ২. OR (যেকোনো একটি True হলে True)
print(a or b)   # True
print(b or False)  # False

# ৩. NOT (উল্টো করে)
print(not a)    # False
print(not b)    # True



# ৪. তুলনামূলক অপারেটর (যেগুলো bool রিটার্ন করে)
x = 10
y = 20
print(x == y)   # False
print(x != y)   # True
print(x < y)    # True
print(x > y)    # False
print(x <= 10)  # True
print(x >= 15)  # False




bool-এর সাথে if-else (সিদ্ধান্ত গ্রহণ)

age = 18
is_student = True

# ১. সরাসরি bool চেক
if is_student:
    print("ছাত্র")  # True
else:
    print("ছাত্র নয়")

# ২. কন্ডিশন চেক
if age >= 18:
    print("প্রাপ্তবয়স্ক")
else:
    print("অপ্রাপ্তবয়স্ক")

# ৩. একাধিক শর্ত (and, or)
if age >= 18 and is_student:
    print("প্রাপ্তবয়স্ক ছাত্র")
elif age >= 18 and not is_student:
    print("প্রাপ্তবয়স্ক (ছাত্র নয়)")
else:
    print("অপ্রাপ্তবয়স্ক")



is_logged_in = True
has_permission = False

if is_logged_in and has_permission:
    print("Access Granted")
else:
    print("Access Denied")

# Output: Access Denied



bool-এর গুরুত্বপূর্ণ টিপস

সরাসরি bool ব্যবহার          if is_active: (ভালো) vs if is_active == True: (খারাপ)
Truthy/Falsy 	             if not data: → ডেটা খালি কিনা চেক করে
বুলিয়ান ফাংশন	             is_valid(), has_permission(), can_access()
বুলিয়ান ভেরিয়েবলের নাম	     is_, has_, can_, should_ দিয়ে শুরু 
None চেক 	                 if user is None: বা if user is not None:




📝 দ্রুত নোট (সংক্ষেপে):

# bool ডেটা টাইপ

✅ মান:
True বা False (মাত্র ২টি)

✅ লজিক্যাল অপারেটর:
and, or, not

✅ তুলনামূলক অপারেটর:
==, !=, <, >, <=, >=

✅ Truthy (True):
- নন-জিরো সংখ্যা
- নন-খালি স্ট্রিং
- নন-খালি কালেকশন

✅ Falsy (False):
- None
- 0, 0.0
- "" (খালি স্ট্রিং)
- [], (), {}, set() (খালি কালেকশন)

✅ মনে রাখবেন:
- True = 1, False = 0 (সংখ্যা হিসেবে)
- if is_active: (সরাসরি) → ভালো
- if is_active == True: → খারাপ



🎯 অ্যাকশন প্ল্যান:

bool দিয়ে বেসিক অপারেশন  (and, or, not)

if-else দিয়ে সিদ্ধান্ত নেওয়ার প্রোগ্রাম 

Truthy/Falsy মান নিয়ে এক্সপেরিমেন্ট 

FastAPI-তে bool প্যারামিটার ও মডেল ব্যবহার

অথেন্টিকেশন বা পারমিশন সিস্টেম বাস্তবায়ন 

ফিচার ফ্ল্যাগ সিস্টেম তৈরি 



পাইথনের ব্যাকএন্ডে True আসলে ইন্টারনালি 1 এবং False আসলে 0 হিসেবে কাজ করে। তাই চাইলে এদের দিয়ে গাণিতিক যোগ-বিয়োগও করা যাবে!

print(True + True)   # 1 + 1 = 2
print(True * 5)      # 1 * 5 = 5
print(False + True)  # 0 + 1 = 1
