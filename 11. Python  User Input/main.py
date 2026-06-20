পাইথনে ইউজারের কাছ থেকে ইনপুট নেওয়ার জন্য input() ফাংশন ব্যবহার করা হয়. এই ফাংশনটি ইউজারের দেওয়া যেকোনো ডেটাকে ডিফল্টভাবে স্ট্রিং (String) বা টেক্সট হিসেবে গ্রহণ করে।

print("=== Please Provide Your Information ===")

# 1. String Inputs (Text)
name = input("Name: ")
dob = input("Date of Birth (DD-MM-YYYY): ")
blood_group = input("Blood Group: ")
religion = input("Religion: ")
country = input("Country: ")
nid_number = input("NID Number: ")
birth_place = input("Birth Place: ")
address = input("Current Address: ")
subject = input("Subject / Department: ")
gmail = input("Gmail Address: ")
phone = input("Phone Number: ")
session = input("Session: ")
current_status = input("Current Status: ")

# 2. Number & Float Inputs (Type Casting)
age = int(input("Age (In Number): "))
height = float(input("Height (In Decimal, e.g.- 5.7): "))
cgpa = float(input("CGPA (In Decimal): "))
account_balance = float(input("Account Balance: "))

# 3. Boolean Input (Yes/No)
married_input = input("Are you married? (yes/no): ")
married = (married_input == "yes") 

# 4. Multiple Inputs separated by comma (List)
skills = input("Your Skills (separated by comma): ").split(",")
hobbies = input("Your Hobbies (separated by comma): ").split(",")
languages = input("Known Languages (separated by comma): ").split(",")


# === Printing all information together ===
print("\n--- Your Profile Summary ---")
print("Name:", name)
print("Date of Birth:", dob)
print("Age:", age)
print("Blood Group:", blood_group)
print("Religion:", religion)
print("Country:", country)
print("NID Number:", nid_number)
print("Birth Place:", birth_place)
print("Current Address:", address)
print("Subject / Department:", subject)
print("Gmail Address:", gmail)
print("Phone Number:", phone)
print("Session:", session)
print("Current Status:", current_status)
print("Height:", height)
print("CGPA:", cgpa)
print("Account Balance:", account_balance)

# Ternary Operator ব্যবহার করে True হলে 'Yes' এবং False হলে 'No' প্রিন্ট হবে
print("Married?:", "Yes" if married else "No")

print("Skills:", skills)
print("Hobbies:", hobbies)
print("Languages:", languages)


যেমনভাবে JS-এ string.padEnd(length, character) কাজ করে, পাইথনেও ঠিক একইভাবে string.ljust(length, character) কাজ করে। এটি লেখার বাম পাশে মূল টেক্সট ঠিক রেখে ডান পাশে খালি জায়গা বা নির্দিষ্ট ক্যারেক্টার দিয়ে দৈর্ঘ্য পূরণ করে।

print("=== Please Provide Your Information ===")

# 1. String Inputs (Text)
name = input("Name: ")
dob = input("Date of Birth (DD-MM-YYYY): ")
blood_group = input("Blood Group: ")
religion = input("Religion: ")
country = input("Country: ")
nid_number = input("NID Number: ")
birth_place = input("Birth Place: ")
address = input("Current Address: ")
subject = input("Subject / Department: ")
gmail = input("Gmail Address: ")
phone = input("Phone Number: ")
session = input("Session: ")
current_status = input("Current Status: ")

# 2. Number & Float Inputs (Type Casting)
age = int(input("Age (In Number): "))
height = float(input("Height (In Decimal, e.g.- 5.7): "))
cgpa = float(input("CGPA (In Decimal): "))
account_balance = float(input("Account Balance: "))

# 3. Boolean Input (Yes/No)
married_input = input("Are you married? (yes/no): ")
married = (married_input == "yes") 

# 4. Multiple Inputs separated by comma (List)
skills = input("Your Skills (separated by comma): ").split(",")
hobbies = input("Your Hobbies (separated by comma): ").split(",")
languages = input("Known Languages (separated by comma): ").split(",")


# === Printing all information together using .ljust() ===
# প্রতিটি লেবেলের দৈর্ঘ্য ২০ ক্যারেক্টার করা হয়েছে, ফলে ক্লোন (:) গুলো একদম সোজা লাইনে থাকবে।

print("\n--- Your Profile Summary ---")
print("Name".ljust(20) + ":", name)
print("Date of Birth".ljust(20) + ":", dob)
print("Age".ljust(20) + ":", age)
print("Blood Group".ljust(20) + ":", blood_group)
print("Religion".ljust(20) + ":", religion)
print("Country".ljust(20) + ":", country)
print("NID Number".ljust(20) + ":", nid_number)
print("Birth Place".ljust(20) + ":", birth_place)
print("Current Address".ljust(20) + ":", address)
print("Subject / Department".ljust(20) + ":", subject)
print("Gmail Address".ljust(20) + ":", gmail)
print("Phone Number".ljust(20) + ":", phone)
print("Session".ljust(20) + ":", session)
print("Current Status".ljust(20) + ":", current_status)
print("Height".ljust(20) + ":", height)
print("CGPA".ljust(20) + ":", cgpa)
print("Account Balance".ljust(20) + ":", account_balance)

# Ternary Operator এর সাথে .ljust()
print("Married?".ljust(20) + ":", "Yes" if married else "No")

print("Skills".ljust(20) + ":", skills)
print("Hobbies".ljust(20) + ":", hobbies)
print("Languages".ljust(20) + ":", languages)

পাইথনে .ljust() মেথডটি মূলত টেক্সট ফরম্যাটিংয়ের জন্য ব্যবহৃত হয়। এর পূর্ণরূপ হলো Left Justify।

string.ljust(width, fillchar)

width (আবশ্যিক):  পুরো স্ট্রিংটির মোট দৈর্ঘ্য কত বড় করতে চাওয়া হসছে (ক্যারেক্টার সংখ্যা)।

fillchar (ঐচ্ছিক): খালি জায়গায়  কী বসাতে চাওয়া হসছে। কিছু না দিলে এটি স্বয়ংক্রিয়ভাবে স্পেস (" ") দিয়ে জায়গা পূরণ করবে।



১. স্পেস দিয়ে খালি জায়গা পূরণ (Default)

একটা শব্দ আছে "Python", যার দৈর্ঘ্য ৬ ক্যারেক্টার। মোট দৈর্ঘ্য ১০ ক্যারেক্টার করতে এবং বাকি ৪টি ঘর খালি রাখতে:

text = "Python"
result = text.ljust(10)

print(result + "Is Awesome")
# Output: Python    Is Awesome
# (এখানে Python এর পর ৪টি স্পেস তৈরি হয়েছে)


২. নির্দিষ্ট ক্যারেক্টার দিয়ে পূরণ
যদি স্পেস না দিয়ে অন্য কিছু (যেমন: ডট ., ড্যাশ -, বা স্টার *) দিয়ে ডানপাশ পূরণ করতে চাওয়া হয়:

text = "Hello"
# মোট দৈর্ঘ্য ১০ বানাবে, বাকি ৫টি ঘর '-' দিয়ে পূরণ করবে
result = text.ljust(10, "-")

print(result)
# Output: Hello-----



কিন্তু সব লেবেলের দৈর্ঘ্য .ljust(15) দিয়ে ১৫ ক্যারেক্টার ফিক্সড করে দিলে ক্লোনগুলো একদম সোজা লাইনে চলে আসে:

print("Name".ljust(15) + ": Abdullah")
print("Roll Number".ljust(15) + ": 5")
print("Blood Group".ljust(15) + ": A+")

Name           : Abdullah
Roll Number    : 5
Blood Group    : A+




একইভাবে ডানপাশে লেখা রেখে বামপাশে স্পেস দিতে চাইলে পাইথনে .rjust() ব্যবহার করা হয়।)

পাইথনে .rjust() মেথডটি ঠিক .ljust()-এর উল্টো কাজ করে। এর পূর্ণরূপ হলো Right Justify।

সহজ কথায়, এটি মূল লেখাকে ডান পাশে (Right) পাঠিয়ে দেয় এবং তার বাম পাশে (Left) নির্দিষ্ট দৈর্ঘ্য পূরণ করার জন্য খালি জায়গা (Space) বা ক্যারেক্টার বসিয়ে দেয়।

string.rjust(width, fillchar)

১. বাম পাশে খালি জায়গা বা স্পেস তৈরি করা (Default)
ধরুন, শব্দ হলো "Python" (দৈর্ঘ্য ৬ ক্যারেক্টার)।  মোট দৈর্ঘ্য ১০ ক্যারেক্টার করতে এবং বাকি ৪টি ঘর বাম পাশে খালি রাখতে:

text = "Python"
result = text.rjust(10)

print(result)
# Output: '    Python' 
# (বাম পাশে ৪টি স্পেস যুক্ত হয়ে লেখাটি ডানে চলে গেছে)


২. নির্দিষ্ট ক্যারেক্টার দিয়ে বাম পাশ পূরণ করা
যদি স্পেস না দিয়ে অন্য কোনো ক্যারেক্টার (যেমন: শূন্য 0 বা স্টার *) দিয়ে বাম পাশ ভরাট করতে:

text = "75"
# মোট দৈর্ঘ্য ৫ বানাবে, বামের ৩টি ঘর '0' দিয়ে পূরণ করবে
result = text.rjust(5, "0")

print(result)
# Output: 00075


print("Name:".rjust(20) + " Mohammad Abdullah")
print("Date of Birth:".rjust(20) + " 15-06-1997")
print("Age:".rjust(20) + " 30")
print("Blood Group:".rjust(20) + " B+")
print("Account Balance:".rjust(20) + " 89.59")

এখানে লেবেলগুলো ডান পাশে সমান লাইনে থাকবে, আর বাম পাশে খালি জায়গা তৈরি হবে:

Name: Mohammad Abdullah
      Date of Birth: 15-06-1997
                Age: 30
        Blood Group: B+
    Account Balance: 89.59




বাস্তব প্রয়োগ এই ট্রিকটি রোল নম্বর (যেমন: 001, 002) বা আইডি নম্বর ফরম্যাট করার সময় প্রচুর ব্যবহৃত হয়।:
রোল নম্বর বা আইডি নম্বর ফরম্যাট করার জন্য .rjust()-এর বাস্তব প্রয়োগের ৩টি উদাহরণ


প্রোগ্রামিংয়ে ডাটাবেজ তৈরি বা ক্যাশ মেমো প্রিন্ট করার সময় এই ট্রিকটি সবচেয়ে বেশি ব্যবহার করা হয়।

১. সাধারণ আইডি নম্বর ফরম্যাটিং (001, 002... তৈরি করা)
লুপ চালিয়ে ১ থেকে ৫ পর্যন্ত স্টুডেন্ট আইডিগুলোকে ৩ ডিজিটের স্ট্যান্ডার্ড ফরম্যাটে (001, 002) রূপান্তর করার উদাহরণ:

print("--- Student ID List ---")

for i in range(1, 6):
    # 'i'-কে প্রথমে স্ট্রিং করে নিলাম, তারপর মোট দৈর্ঘ্য ৩ করতে বামে '0' বসালাম
    student_id = str(i).rjust(3, "0")
    print(f"Student ID: {student_id}")

--- Student ID List ---
Student ID: 001
Student ID: 002
Student ID: 003
Student ID: 004
Student ID: 005


২. ডাইনামিক ইউজার ইনপুট ফরম্যাটিং
ইউজার যখন শুধু একটি সংখ্যা ইনপুট দেবে (যেমন: 7), কোড সেটাকে স্বয়ংক্রিয়ভাবে একটি ৪ ডিজিটের অফিশিয়াল আইডি (ID-0007) বানিয়ে দেবে:

user_input = input("Enter your serial number: ") # ধরুন ইউজার দিল '25'

# বাম পাশে শূন্য (0) বসিয়ে মোট ৪ ডিজিট করা হলো
formatted_number = user_input.rjust(4, "0")

official_id = "ID-" + formatted_number
print("Your Official ID is:", official_id) 
# Output: Your Official ID is: ID-0025


৩. ক্যাশ মেমো বা রসিদ তৈরি (টাকার অংক সোজাসুজি রাখা)
দোকানের রসিদ বা বিল বানানোর সময় টাকার অংকগুলো যেন ডান পাশে সুন্দরভাবে সমান লাইনে থাকে, তার জন্য .rjust() ব্যবহার করা হয়:

item1_price = "150"
item2_price = "2550"
item3_price = "45"

print("--- Cash Memo ---")
# টাকার অংকগুলোকে মোট ৬ ক্যারেক্টার দৈর্ঘ্যে ডানপাশে পুশ করা হয়েছে
print("Rice   : BDT " + item1_price.rjust(6))
print("Laptop : BDT " + item2_price.rjust(6))
print("Pen    : BDT " + item3_price.rjust(6))


--- Cash Memo ---
Rice   : BDT    150
Laptop : BDT   2550
Pen    : BDT     45



💡 পাইথন প্রো-টিপ: শুধু মাত্র শূন্য (0) দিয়ে বাম পাশ পূরণ করার জন্য পাইথনে আরেকটি স্পেশাল মেথড আছে,
যার নাম .zfill()। যেমন: str(5).zfill(3) লিখলেও আউটপুট 005-ই আসবে। এটি মূলত rjust(3, "0")-এরই একটি শর্টকাট।



.split() ------------

পাইথনে .split() মেথডের প্রধান কাজ হলো একটি বড় স্ট্রিং বা লেখাকে টুকরো টুকরো করে একটি তালিকা বা লিস্ট (list) এ রূপান্তর করা।


স্পেস (খালি জায়গা) দেখে টেক্সট আলাদা করা
যদি .split() এর ব্র্যাকেটের ভেতর কিছু না লিখা হয়, তবে এটি স্বয়ংক্রিয়ভাবে যেকোনো ধরনের হোয়াইটস্পেস (স্পেস, ট্যাব বা নতুন লাইন) খুঁজে পায় এবং সেখান থেকে লেখাকে আলাদা করে।

text = "Python is very easy"
result = text.split()

print(result)
# Output: ['Python', 'is', 'very', 'easy']

কখন কাজে লাগে: যখন কোনো প্যারাগ্রাফ থেকে প্রতিটি শব্দকে আলাদা আলাদা করতে চাওয়া হয়।




নির্দিষ্ট ক্যারেক্টার বা চিহ্ন (Delimiter) দেখে আলাদা করা
টেক্সটের ভেতরের শব্দগুলো যদি স্পেস দিয়ে আলাদা না হয়ে কমা (,), ড্যাশ (-), বা স্ল্যাশ (/) দিয়ে যুক্ত থাকে, তবে ব্র্যাকেটের ভেতর সেই চিহ্নটি বলে দিতে হয়।

# উদাহরণ ১: কমা (,) দিয়ে আলাদা করা
skills = "C,JavaScript,Python,HTML"
print(skills.split(","))
# Output: ['C', 'JavaScript', 'Python', 'HTML']

# উদাহরণ ২: জন্মতারিখ থেকে দিন, মাস, বছর আলাদা করা
dob = "15-06-1997"
print(dob.split("-"))
# Output: ['15', '06', '1997']




সর্বোচ্চ কয়টি টুকরো হবে তা নির্ধারণ করা (maxsplit)

এটি একটি অ্যাডভান্সড ফিচার। চাইলে বলে দেওয়া যায় যে পুরো লেখাটিকে সর্বোচ্চ কয়টি টুকরো করা যাবে। এর জন্য maxsplit প্যারামিটার ব্যবহার করা হয়।


text = "Dhaka-Chittagong-Sylhet-Khulna"

# প্রথম ২টি ড্যাশ (-) দেখে আলাদা করবে, বাকিটা একসাথেই রেখে দেবে
result = text.split("-", maxsplit=2)

print(result)
# Output: ['Dhaka', 'Chittagong', 'Sylhet-Khulna']



যদি ইউজার স্পেস দিয়ে একাধিক তথ্য লেখে, তবে .split() কোনো কিছু না বললেই স্বয়ংক্রিয়ভাবে স্পেসগুলো ধরে ডেটা আলাদা করে দেয়।

# ইউজার ইনপুট দিল: Mohammad Abdullah 30
first_name, last_name, age = input("Enter first name, last name and age: ").split()

print("First Name:", first_name)
print("Last Name :", last_name)
print("Age       :", age)

ইনপুট দেওয়ার নিয়ম: Mohammad Abdullah 30 (মাঝখানে স্পেস থাকবে)।


কমা ( , ) দিয়ে ইনপুট আলাদা করা
অনেক সময় ইউজার স্পেস না দিয়ে কমা দিয়ে লিখতে পছন্দ করে (যেমন স্কিল বা হবির ক্ষেত্রে)। তখন ব্র্যাকেটের ভেতর বলে দিতে হয় যে কমা , দেখে আলাদা করতে চাই: .split(",")

# ইউজার ইনপুট দিল: C,JavaScript,Python
skill1, skill2, skill3 = input("Enter 3 skills (separated by comma): ").split(",")

print("Skill 1:", skill1)
print("Skill 2:", skill2)
print("Skill 3:", skill3)

C,JavaScript,Python (কোনো স্পেস ছাড়া কমা দিয়ে)।



এক লাইনে একাধিক সংখ্যা নিয়ে লিস্ট তৈরি করা (map সহ)
এটি সবচেয়ে বেশি ব্যবহৃত হয়। ইউজার এক লাইনে অনেকগুলো সংখ্যা স্পেস দিয়ে লিখবে এবং কোড সেগুলোকে সরাসরি একটি list-এ রূপান্তর করে নেবে:

# ইউজার ইনপুট দিল: 10 20 30 40 50
numbers = list(map(int, input("Enter numbers (separated by space): ").split()))

print("Your List:", numbers)
# Output: Your List: [10, 20, 30, 40, 50]

যদি বাম পাশে ৩টি ভ্যারিয়েবল রাখেন (a, b, c), তাহলে ইউজারকে অবশ্যই ৩টি তথ্যই ইনপুট দিতে হবে। ইউজার যদি ২টি বা ৪টি তথ্য দেয়, তবে পাইথন ValueError এরর দেখাবে।

যদি ইনপুটের সংখ্যা নির্দিষ্ট না থাকে (যেমন ইউজার ৫টাও দিতে পারে, ১০টাও দিতে পারে), তখন ৩ নম্বর উদাহরণের মতো সরাসরি list-এ জমা করাই সবচেয়ে নিরাপদ!





💡 ইন্টারভিউ বা কুইজের জন্য একটি গুরুত্বপূর্ণ ট্রিক:
যদি কোনো স্ট্রিংয়ে পরপর অনেকগুলো স্পেস থাকে, আর সাধারণ .split() ব্যবহার করা হয়, তবে পাইথন বুদ্ধিমানদের মতো অতিরিক্ত সব স্পেস ইগনোর করে শুধু আসল শব্দগুলো নেয়:

text = "Hello     World"  # মাঝে অনেক স্পেস
print(text.split())     # Output: ['Hello', 'World']

'Hello' এর পর কমা ( , ) কেন?
এই কমাটি মূল টেক্সটের বা স্পেসের কমা নয়। এটি হচ্ছে পাইথন লিস্টের নিজস্ব ব্যাকরণ বা নিয়ম (Syntax)।
পাইথনে যখন কোনো লিস্টের ভেতর একাধিক উপাদান বা ডেটা রাখা হয়, তখন একটি ডেটা থেকে আরেকটি ডেটাকে আলাদা করে বোঝানোর জন্য মাঝখানে কমা (,) ব্যবহার করতে হয়।
যেমন,  বাজারে কেনাকাটার তালিকায় যদি থাকে: চাল, ডাল, তেল।
পাইথন সেটাকে লিখবে: ['চাল', 'ডাল', 'তেল']
এখানে 'Hello' এবং 'World' দুটি আলাদা শব্দ (বা উপাদান), তাই পাইথন তাদের মাঝখানে একটি কমা (,) বসিয়ে দেখিয়েছে যে এরা দুজন আলাদা।




যদি ব্র্যাকেটের ভেতর স্পেস নির্দিষ্ট করে দেন—.split(" "), তবে পাইথন প্রতিটা স্পেসের জন্য ফাঁকা উপাদান বা এম্পটি স্ট্রিং ('') তৈরি করবে:
print(text.split(" "))  # Output: ['Hello', '', '', '', '', 'World']

সহজ কথায়: যখন ব্র্যাকেটের ভেতর সুনির্দিষ্টভাবে স্পেস বা ফাঁকা জায়গা বলে দিই (" "), তখন পাইথন আর কোনো চালাকি করে না। সে অন্ধের মতো প্রতি একটা স্পেসের জন্য একবার করে কাটার কাঁচি চালায়।
উদাহরণে "Hello     World" শব্দ দুটির মাঝে মোট ৫টি স্পেস আছে। পাইথন এই ৫টি স্পেসকে কীভাবে কেটে ৪টি খালি জায়গা ('') বানালো, তা নিচে ধাপে ধাপে দেখানো হলো:

কাটার মেকানিজম (ধাপে ধাপে):
১. প্রথম স্পেস: পাইথন "Hello" এর ঠিক পরের প্রথম স্পেসটি পেল। সে সেখানে প্রথম কোপ দিল। বাম পাশে আলাদা হয়ে গেল 'Hello'।
২. দ্বিতীয় স্পেস: এরপর সে আরেকটি স্পেস পেল। এই স্পেস এবং আগের স্পেসের মাঝখানে কি কোনো অক্ষর বা শব্দ আছে? না, কিচ্ছু নেই (ফাঁকা)। তাই পাইথন সেখানে একটি খালি উপাদান বা এম্পটি স্ট্রিং '' তৈরি করল।
৩. তৃতীয় স্পেস: আবার পরের স্পেসটি পেল। আগের স্পেস আর এই স্পেসের মাঝেও কিচ্ছু নেই। তাই আবারও তৈরি হলো আরেকটি ''।
৪. চতুর্থ স্পেস: একই নিয়মে আবারও মাঝখানে কিচ্ছু না থাকায় তৈরি হলো আরেকটি ''।
৫. পঞ্চম স্পেস: এই স্পেসটির বেলাতেও আগের স্পেসের সাথে মাঝখানে কিছু না থাকায় তৈরি হলো শেষ ''।


এরপর পাইথন বাকি অংশ হিসেবে পেয়ে গেল "World"-কে।

গাণিতিক সূত্র (সহজ হিসাব):

শব্দের মাঝে যতগুলো স্পেস (" ") থাকবে, পাইথন যদি সুনির্দিষ্টভাবে স্পেস ধরে কাটে, তবে মাঝখানে তৈরি হওয়া খালি ঘরের সংখ্যা হবে: (মোট স্পেসের সংখ্যা - ১)।
যেহেতু শব্দ দুটির মাঝে মোট ৫টি স্পেস ছিল, তাই সূত্রে ফেলে: 5 - 1 = 4 টি খালি ঘর ('') তৈরি হয়েছে।
যদি মাঝখানে ৩টি স্পেস থাকত, তবে খালি ঘর আসত ২টি ['Hello', '', '', 'World']।

text.split() (ব্র্যাকেট খালি) ➔ সব স্পেসকে একসাথে ১টি দেয়াল ধরে। (স্মার্ট পদ্ধতি)

text.split(" ") (ব্র্যাকেট পূরণ) ➔ প্রতিটি স্পেসকে আলাদা আলাদা করে কাটে, যার ফলে মাঝখানের ফাঁকা জায়গাগুলোও লিস্টে উপাদান হিসেবে ঢুকে পড়ে। (অন্ধ পদ্ধতি)


text = "Mohammad      Abdullah"
print(text.split(" "))

['Mohammad', '', '', '', '', 'Abdullah']

সহজ ব্যাখ্যা (কেন ৫টি খালি ঘর বা '' এলো?):
এখানে মূল টেক্সট "Mohammad      Abdullah"-এর মাঝে মোট ৬টি স্পেস বা খালি জায়গা আছে।
যেহেতু  ব্র্যাকেটের ভেতর নির্দিষ্ট করে স্পেস দিয়ে দেওয়া হয়েছে —.split(" "), পাইথন প্রতিটা স্পেসের পর পর কাটার কাঁচি চালাবে।

১. প্রথম কোপ: "Mohammad"-এর ঠিক পরের প্রথম স্পেসটিতে পাইথন কাটল। বাম পাশে আলাদা হয়ে গেল মূল শব্দ 'Mohammad'।

২. বাকি স্পেসগুলোর খেলা: প্রথম স্পেসের পর আরও ৫টি স্পেস বাকি থাকে।

     নম্বর স্পেস কাটার সময় পাইথন দেখল ১ম ও ২য় স্পেসের মাঝে কোনো অক্ষর নেই, তাই একটি খালি ঘর '' তৈরি হলো।

     নম্বর স্পেস কাটার সময় ২য় ও ৩য় স্পেসের মাঝে কিছু না থাকায় আরেকটি '' তৈরি হলো।

এইভাবে বাকি স্পেসগুলোর মাঝখানের ফাঁকা জায়গার জন্য একে একে মোট ৫টি খালি ঘর ('') তৈরি হবে।
৩. শেষ ধাপ: সব স্পেস পার হয়ে পাইথন পেয়ে গেল "Abdullah"-কে এবং সেটিকে লিস্টের শেষে বসিয়ে দিল।

মাঝখানের খালি ঘরের সংখ্যা = (মোট স্পেসের সংখ্যা - ১)
এখানে মোট স্পেস আছে = ৬টি।
তাহলে মাঝখানে খালি ঘর ('') তৈরি হবে = 6 - 1 = 5 টি।
লিস্টের ভেতরের উপাদানগুলো গুণলে : 'Mohammad' এর পর ঠিক ৫টি খালি স্পেস ('') এসে বসেছে।




.split() নিজে কোনো লিস্ট নয়; এটি একটি ফাংশন বা মেথড (Method)। তবে সহজ কথায়: .split() হলো একটি লিস্ট বানানোর মেশিন।

যখন কোনো স্ট্রিং বা টেক্সটের ওপর এই মেশিনটি চালান, তখন সে সেই টেক্সটটিকে কেটে টুকরো টুকরো করে ফলাফল হিসেবে আপনাকে একটি নতুন লিস্ট (List) উপহার দেয়।

# ১. এটি একটি সাধারণ স্ট্রিং বা টেক্সট
text = "Apple Banana Orange" 

# ২. এখানে .split() হলো একটি মেথড (বা মেশিন), যা টেক্সটকে কাটছে
result = text.split() 

# ৩. এখন 'result' ভ্যারিয়েবলের ভেতর একটি 'লিস্ট' জমা হয়েছে
print(result)       # Output: ['Apple', 'Banana', 'Orange']
print(type(result)) # Output: <class 'list'> (পাইথন বলছে এটা একটা লিস্ট)

text ➔ একটি স্ট্রিং।

.split() ➔ একটি মেথড (যা কাটার কাজ করে)।

result ➔ একটি লিস্ট (যা কাটার পর তৈরি হওয়া ফলাফল)।

তার মানে, .split() কোনো লিস্ট নয়, কিন্তু এর কাজই হলো স্ট্রিংকে কেটে লিস্টে রূপান্তর করা।




