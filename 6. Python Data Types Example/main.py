Template Literals (f-string): জাভাস্ক্রিপ্টে যেভাবে ব্যাকটিক এবং ডলার সাইন দিয়ে `My name is: ${name}` লিখা হত, 
পাইথনে সেটাকে বলা হয় f-string। এটি লেখার নিয়ম হলো স্ট্রিংয়ের শুরুতে একটা f লিখে কোটেশনের ভেতর থার্ড ব্র্যাকেট ব্যবহার করা: f"My name is: {name}"।

# --- Constant Data ---
NAME = "Mohammad Abdullah"
DOB = "15-06-1997"
BLOOD_GROUP = "B+"
RELIGION = "Islam"
COUNTRY = "Bangladesh"
NID_NUMBER = "1997541258745"
BIRTH_PLACE = "Rangpur"

# --- Variable Data ---
age = 30
cgpa = 3.50
address = "Gongachora, Rangpur"
subject = "Backend Engineering"
married = False
account_balance = 89.5982145897
gmail = "programmeraziz216@gmail.com"
phone = "01568451112"
skills = "C, JavaScript, C++, Python"
hobbies = "Coding, Reading, Traveling"
session = "2025-26"
current_status = "Student & Programmer"
language = "Bengali, English"

# --- Complete Output ---
print(f"My name is          : {NAME}")
print(f"My age is           : {age}")
print(f"Date of Birth       : {DOB}")
print(f"Blood Group         : {BLOOD_GROUP}")
print(f"Religion            : {RELIGION}")
print(f"Country             : {COUNTRY}")
print(f"NID Number          : {NID_NUMBER}")
print(f"Birth Place         : {BIRTH_PLACE}")
print("-" * 40) # একটি সুন্দর ডিভাইডার লাইনের জন্য
print(f"CGPA                : {cgpa}")
print(f"Address             : {address}")
print(f"Subject             : {subject}")
print(f"Married Status      : {married}")
print(f"Account Balance     : {account_balance}")
print(f"Gmail               : {gmail}")
print(f"Phone               : {phone}")
print(f"Skills              : {skills}")
print(f"Hobbies             : {hobbies}")
print(f"Session             : {session}")
print(f"Current Status      : {current_status}")
print(f"Language            : {language}")



My name is          : Mohammad Abdullah
My age is           : 30
Date of Birth       : 15-06-1997
Blood Group         : B+
Religion            : Islam
Country             : Bangladesh
NID Number          : 1997541258745
Birth Place         : Rangpur
----------------------------------------
CGPA                : 3.5
Address             : Gongachora, Rangpur
Subject             : Backend Engineering
Married Status      : False
Account Balance     : 89.5982145897
Gmail               : programmeraziz216@gmail.com
Phone               : 01568451112
Skills              : C, JavaScript, C++, Python
Hobbies             : Coding, Reading, Traveling
Session             : 2025-26
Current Status      : Student & Programmer
Language            : Bengali, English






এখানে শুধু age, cgpa, married এবং account_balance ভেরিয়েবলগুলো যেহেতু টেক্সট বা স্ট্রিং নয়, তাই পাইথনের নিয়ম অনুযায়ী সেগুলোকে str() দিয়ে টেক্সটে রূপান্তর করে নেওয়া হয়েছে যাতে প্লাস (+) চিহ্নটি নিখুঁতভাবে কাজ করে।

# --- Constant Data ---
name = "Mohammad Abdullah"
dob = "15-06-1997"
bloodGroup = "B+"
religion = "Islam"
country = "Bangladesh"
nidNumber = "1997541258745"
birthPlace = "Rangpur"

# --- Variable Data ---
age = 30
cgpa = 3.50
address = "Gongachora, Rangpur"
subject = "Backend Engineering"
married = False
accountBalance = 89.5982145897
gmail = "programmeraziz216@gmail.com"
phone = "01568451112"
skills = "C, JavaScript, C++, Python"
hobbies = "Coding, Reading, Traveling"
session = "2025-26"
currentStatus = "Student & Programmer"
language = "Bengali, English"

# --- Simple Output using + ---
print("Name                : " + name)
print("Age                 : " + str(age))
print("Date of Birth       : " + dob)
print("Blood Group         : " + bloodGroup)
print("Religion            : " + religion)
print("Country             : " + country)
print("NID Number          : " + nidNumber)
print("Birth Place         : " + birthPlace)
print("----------------------------------------")
print("CGPA                : " + str(cgpa))
print("Address             : " + address)
print("Subject             : " + subject)
print("Married Status      : " + str(married))
print("Account Balance     : " + str(accountBalance))
print("Gmail               : " + gmail)
print("Phone               : " + phone)
print("Skills              : " + skills)
print("Hobbies             : " + hobbies)
print("Session             : " + session)
print("Current Status      : " + currentStatus)
print("Language            : " + language)


Name                : Mohammad Abdullah
Age                 : 30
Date of Birth       : 15-06-1997
Blood Group         : B+
Religion            : Islam
Country             : Bangladesh
NID Number          : 1997541258745
Birth Place         : Rangpur
----------------------------------------
CGPA                : 3.5
Address             : Gongachora, Rangpur
Subject             : Backend Engineering
Married Status      : False
Account Balance     : 89.5982145897
Gmail               : programmeraziz216@gmail.com
Phone               : 01568451112
Skills              : C, JavaScript, C++, Python
Hobbies             : Coding, Reading, Traveling
Session             : 2025-26
Current Status      : Student & Programmer
Language            : Bengali, English



🐍 সম্পূর্ণ পাইথন কোড (Simple Comma Method)

# --- Constant Data ---
name = "Mohammad Abdullah"
dob = "15-06-1997"
bloodGroup = "B+"
religion = "Islam"
country = "Bangladesh"
nidNumber = "1997541258745"
birthPlace = "Rangpur"

# --- Variable Data ---
age = 30
cgpa = 3.50
address = "Gongachora, Rangpur"
subject = "Backend Engineering"
married = False
accountBalance = 89.5982145897
gmail = "programmeraziz216@gmail.com"
phone = "01568451112"
skills = "C, JavaScript, C++, Python"
hobbies = "Coding, Reading, Traveling"
session = "2025-26"
currentStatus = "Student & Programmer"
language = "Bengali, English"

# --- Simple Output using Comma (,) ---
print("Name                :", name)
print("Age                 :", age)
print("Date of Birth       :", dob)
print("Blood Group         :", bloodGroup)
print("Religion            :", religion)
print("Country             :", country)
print("NID Number          :", nidNumber)
print("Birth Place         :", birthPlace)
print("----------------------------------------")
print("CGPA                :", cgpa)
print("Address             :", address)
print("Subject             :", subject)
print("Married Status      :", married)
print("Account Balance     :", accountBalance)
print("Gmail               :", gmail)
print("Phone               :", phone)
print("Skills              :", skills)
print("Hobbies             :", hobbies)
print("Session             :", session)
print("Current Status      :", currentStatus)
print("Language            :", language)

Name                : Mohammad Abdullah
Age                 : 30
Date of Birth       : 15-06-1997
Blood Group         : B+
Religion            : Islam
Country             : Bangladesh
NID Number          : 1997541258745
Birth Place         : Rangpur
----------------------------------------
CGPA                : 3.5
Address             : Gongachora, Rangpur
Subject             : Backend Engineering
Married Status      : False
Account Balance     : 89.5982145897
Gmail               : programmeraziz216@gmail.com
Phone               : 01568451112
Skills              : C, JavaScript, C++, Python
Hobbies             : Coding, Reading, Traveling
Session             : 2025-26
Current Status      : Student & Programmer
Language            : Bengali, English


ljust() এর পূর্ণরূপ হলো Left Justify। অর্থাৎ, এটি আসল লেখাকে বাম পাশে ঠিক রেখে, ডান পাশে ইচ্ছা অনুযায়ী ফাঁকা জায়গা (Space) বা যেকোনো চিহ্ন বসিয়ে লেখাটিকে বড় বা সমান করে দেয়।

🐍 সম্পূর্ণ পাইথন কোড (ljust()

# --- Constant Data ---
name = "Mohammad Abdullah"
dob = "15-06-1997"
bloodGroup = "B+"
religion = "Islam"
country = "Bangladesh"
nidNumber = "1997541258745"
birthPlace = "Rangpur"

# --- Variable Data ---
age = 30
cgpa = 3.50
address = "Gongachora, Rangpur"
subject = "Backend Engineering"
married = False
accountBalance = 89.5982145897
gmail = "programmeraziz216@gmail.com"
phone = "01568451112"
skills = "C, JavaScript, C++, Python"
hobbies = "Coding, Reading, Traveling"
session = "2025-26"
currentStatus = "Student & Programmer"
language = "Bengali, English"

# --- ljust(20) দিয়ে প্রতিটি লেখার দৈর্ঘ্য ২০ ক্যারেক্টার করা হয়েছে ---
# এটি JS এর padEnd(20, " ") এর মতো কাজ করছে এবং কোনো কনক্যাট ছাড়াই কমা (,) দিয়ে প্রিন্ট হচ্ছে

print("Name".ljust(20), ":", name)
print("Age".ljust(20), ":", age)
print("Date of Birth".ljust(20), ":", dob)
print("Blood Group".ljust(20), ":", bloodGroup)
print("Religion".ljust(20), ":", religion)
print("Country".ljust(20), ":", country)
print("NID Number".ljust(20), ":", nidNumber)
print("Birth Place".ljust(20), ":", birthPlace)
print("-" * 45) # ডিভাইডার লাইন
print("CGPA".ljust(20), ":", cgpa)
print("Address".ljust(20), ":", address)
print("Subject".ljust(20), ":", subject)
print("Married Status".ljust(20), ":", married)
print("Account Balance".ljust(20), ":", accountBalance)
print("Gmail".ljust(20), ":", gmail)
print("Phone".ljust(20), ":", phone)
print("Skills".ljust(20), ":", skills)
print("Hobbies".ljust(20), ":", hobbies)
print("Session".ljust(20), ":", session)
print("Current Status".ljust(20), ":", currentStatus)
print("Language".ljust(20), ":", language)

টেক্সট ছোট হোক বা বড়, সবগুলোর ডান পাশের কোলন (:) একদম সোজা এক লাইনে পুতুলের মতো সাজানো আসবে:

Name                 : Mohammad Abdullah
Age                  : 30
Date of Birth        : 15-06-1997
Blood Group          : B+
Religion             : Islam
Country              : Bangladesh
NID Number           : 1997541258745
Birth Place          : Rangpur
---------------------------------------------
CGPA                 : 3.5
Address              : Gongachora, Rangpur
Subject              : Backend Engineering
Married Status       : False
Account Balance      : 89.5982145897
Gmail                : programmeraziz216@gmail.com
Phone                : 01568451112
Skills               : C, JavaScript, C++, Python
Hobbies              : Coding, Reading, Traveling
Session              : 2025-26
Current Status       : Student & Programmer
Language             : Bengali, English



১ জাভাস্ক্রিপ্টের toFixed() এবং toPrecision() মেথড দুটি দশমিক সংখ্যা (Float) নিয়ে কাজ করার জন্য দারুণ দুটি টুল। পাইথনেও ঠিক একই কাজ করার জন্য খুব সহজ এবং চমৎকার কিছু বিল্ট-ইন উপায় আছে।
পাইথনে এই কাজটি করার জন্য ৩টি জনপ্রিয় উপায় আছে:

ক) f-string ফরম্যাটিং (সবচেয়ে বেশি ব্যবহৃত ও আধুনিক)

স্ট্রিংয়ের ভেতর মান বসানোর সময় :.nf লিখে দিলেই দশমিকের পরের ঘর ফিক্সড হয়ে যায় (এখানে n হলো ঘরের সংখ্যা)।

balance = 89.5982145897

# দশমিকের পর ২ ঘর রাখা (toFixed(2) এর মতো)
print(f"{balance:.2f}")  # আউটপুট: 89.60

# দশমিকের পর ৪ ঘর রাখা (toFixed(4) এর মতো)
print(f"{balance:.4f}")  # আউটপুট: 89.5982

accountBalance = 89.5982145897

# দশমিকের পর ২ ঘর দেখাবে এবং শুরুতে $ থাকবে
print(f"Balance: ${accountBalance:.2f}")  
# আউটপুট: Balance: $89.60


খ) বিল্ট-ইন round() ফাংশন

যদি স্ট্রিং বা প্রিন্ট ছাড়া সরাসরি সংখ্যার মান পরিবর্তন করে অন্য ভেরিয়েবলে রাখতে চাওয়া হয়, তবে round(number, digits) ফাংশন ব্যবহার করা লাগবে।

gpa = 3.786

clean_gpa = round(gpa, 2)
print(clean_gpa)  # আউটপুট: 3.79 (টাইপ কিন্তু float-ই থাকবে)


২. JavaScript-এর toPrecision() এর বিকল্প পাইথনে

জাভাস্ক্রিপ্টে toPrecision(n) এর কাজ হলো— দশমিকের আগে এবং পরে মিলিয়ে মোট কয়টি সিগনিফিকেন্ট ডিজিট বা সার্থক অংক (Significant Digits) থাকবে তা নির্ধারণ করা।

পাইথনে f-string-এর ভেতরে f এর বদলে g ব্যবহার করে হুবহু এই কাজটি করা যায়।

f-string এবং g ফরম্যাট ম্যাজিক

num = 123.4567

# মোট ৪টি সংখ্যা দেখাবে (দশমিকের আগে ৩টি, পরে ১টি)
print(f"{num:.4g}")  # আউটপুট: 123.5

# মোট ২টি সংখ্যা দেখাবে (এটি সায়েন্টিফিক নোটেশনে চলে যাবে JS এর মতোই)
print(f"{num:.2g}")  # আউটপুট: 1.2e+02


পাইথনে String Literal মানে হলো সহজ কথায়— কোডের ভেতরে  যেভাবে সরাসরি কোটেশন চিহ্ন (' ' বা " ") দিয়ে টেক্সট বা স্ট্রিং লিখা হয় ।
পাইথনের একটি অসাধারণ পাওয়ারফুল বৈশিষ্ট্য হলো, এই স্ট্রিংগুলোর একদম শুরুতে বা বাম পাশে (Prefix হিসেবে) ছোট হাতের বা বড় হাতের কিছু 
নির্দিষ্ট ক্যারেক্টার বা লেটার বসিয়ে স্ট্রিংয়ের পুরো আচরণ বদলে দেওয়া যায়। এগুলোকেই বলা হয় String Prefixes। পাইথনে মূলত ৪টি প্রধান প্রিফিক্স আছে।

১. f বা F (Formatted String / f-string)
পাইথনের সবচেয়ে জনপ্রিয় প্রিফিক্স এটি। জাভাস্ক্রিপ্টের Template Literals (ব্যাকটিক ` এবং ${})-এর মতো পাইথনে কোনো ভেরিয়েবলের মান স্ট্রিংয়ের ভেতরে সরাসরি ডায়নামিকালি বসানোর জন্য এটি ব্যবহার করা হয়।

name = "Aziz"
age = 28

# f-string এর ব্যবহার
message = f"My name is {name} and next year I will be {age + 1}."
print(message)

My name is Aziz and next year I will be 29.

💡 জাভাস্ক্রিপ্টের সাথে মিল: JavaScript-এ যেভাবে ব্যাকটিকের ভেতর `${age + 1}` লিখে স্ট্রিংয়ের ভেতরেই যোগ-বিয়োগ করতে পারা যায়, পাইথনে এই {age + 1} হুবহু একই কাজ করছে।


২. r বা R (Raw String)

যে স্ট্রিংয়ের ভেতর \n বা \t দিলে সেগুলো স্পেশাল কাজ (Escape Character) করে। কিন্তু যদি চান পাইথন এগুলোকে স্পেশাল কিছু না ভেবে একদম সাধারণ টেক্সট হিসেবে পড়ুক, তখন স্ট্রিংয়ের আগে r বসাতে হয়।

কাজ: এসকেপ ক্যারেক্টারগুলোর পাওয়ার নষ্ট করে দিয়ে সাধারণ টেক্সট হিসেবে প্রিন্ট করা (ফাইল পাথ বা উইন্ডোজ ডিরেক্টরির জন্য বেস্ট)।

# সাধারণ স্ট্রিংয়ে \n লাইন ভেঙে দেয়
print("Hello\nWorld") 

# Raw String ব্যবহারে \n এর পাওয়ার হাওয়া!
print(r"Hello\nWorld")

Hello
World
Hello\nWorld



৩. b বা B (Byte String)
সাধারণত পাইথনের সব স্ট্রিং হলো Unicode (ইউনিকোড) বা টেক্সট ফরম্যাট। কিন্তু  যদি কোনো স্ট্রিংয়ের আগে b বসিয়ে দেন, তবে সেটি সাধারণ টেক্সট না থেকে কম্পিউটারের সরাসরি বোঝার মতো Bytes (বাইটস)-এ রূপান্তর হয়ে যায়।

কাজ: নেটওয়ার্কে ডেটা পাঠানো, ফাইল হ্যান্ডলিং বা ক্রিপ্টোগ্রাফির মতো ব্যাকএন্ডের একদম কোর লেভেলের কাজে এটি লাগে। এর ভেতরে শুধু ASCII ক্যারেক্টার থাকতে পারে।

normal_str = "Hello"
byte_str = b"Hello"

print(type(normal_str))  # আউটপুট: <class 'str'>
print(type(byte_str))    # আউটপুট: <class 'bytes'>


৪. u বা U (Unicode String)
পাইথন ২-এর জামানায় সাধারণ স্ট্রিংগুলো ইউনিকোড ছিল না। তখন বাংলা বা অন্যান্য ভাষা সাপোর্ট করানোর জন্য স্ট্রিংয়ের আগে আলাদা করে u লিখতে হতো।

কাজ: পাইথন ৩-এ এটি এখন আর কোনো কাজেই লাগে না! কারণ পাইথন ৩-এর সব সাধারণ স্ট্রিং এমনিতেই বাই-ডিফল্ট ইউনিকোড। তবে পুরনো কোডের সাথে মিল রাখার জন্য পাইথন এখনো এটি সাপোর্ট করে 

# দুটির কাজ এখন হুবহু এক, কোনো পার্থক্য নেই
text1 = "বাংলা"
text2 = u"বাংলা"

🔥 অ্যাডভান্সড ট্রিক: একসাথে দুটি প্রিফিক্স ব্যবহার (Prefix Combination)

চাইলে প্রয়োজন অনুযায়ী দুটি প্রিফিক্স একসাথেও ব্যবহার করা যাবে! যেমন— একই সাথে একটি ফরম্যাটেড স্ট্রিং চান (f) এবং চান সেখানে এসকেপ ক্যারেক্টারগুলোও নিষ্ক্রিয় থাকুক (r)। তখন একসাথে fr"" বা rf"" লিখা যাবে।

১. f (Formatted): পাইথনকে বলে, "ভেতরের সেকেন্ড ব্র্যাকেট {} এর কাজ করো (ভেরিয়েবলের মান বসাও)।"
2. r (Raw): পাইথনকে বলে, "ভেতরের ব্যাকস্ল্যাশ \ এর কোনো পাওয়ার থাকবে না (যেমন \n দিলে নতুন লাইন তৈরি হবে না, ওটা সাধারণ টেক্সটের মতো বসে থাকবে)।"

যখন এই দুটিকে একসাথে rf বা fr লিখা হবে, তখন পাইথন এই দুটি কাজই একই সাথে একই লাইনে করবে।

folder = "Python_Files"

# একই সাথে f এবং r এর ম্যাজিক
path = rf"C:\Users\{folder}\new_line_\test.txt"
print(path)

C:\Users\Python_Files\new_line_\test.txt

কম্পিউটারে Python_Files নামে একটি ফোল্ডার আছে। সেই ফোল্ডারের ভেতরে থাকা একটি টেক্সট ফাইলের পাথ (Path) বা ঠিকানা প্রিন্ট করতে চাইলে ।

সাধারণত উইন্ডোজ কম্পিউটারে ফোল্ডারের ঠিকানাগুলো দেখতে এমন হয়: C:\Users\Python_Files\new_folder\test.txt এই ঠিকানার ভেতর কিন্তু \new_folder লিখতে গিয়ে একটা \n চলে এসেছে!

folder_name = "Python_Files"

# উপায় ১: শুধু 'f' ব্যবহার করলে (সমস্যা হবে!)
# কারণ \n দেখে পাইথন লাইনটা ভেঙে দেবে, ফোল্ডারের নাম ঠিকঠাক বসলেও পাথ নষ্ট হয়ে যাবে।
print(f"C:\Users\{folder_name}\new_folder\test.txt")


# উপায় ২: শুধু 'r' ব্যবহার করলে (আরেক সমস্যা!)
# এবার \n এর পাওয়ার নষ্ট হবে ঠিকই, কিন্তু {folder_name} আর ভেরিয়েবলের মান বসাবে না, সরাসরি ব্র্যাকেটটাই প্রিন্ট হবে।
print(r"C:\Users\{folder_name}\new_folder\test.txt")


# উপায় ৩: 'rf' বা 'fr' একসাথে ব্যবহার করলে (ম্যাজিক! একদম নিখুঁত)
# এটি একই সাথে ভেরিয়েবলের মানও বসাবে, আবার \n কে লাইনও ভাঙতে দেবে না।
print(rf"C:\Users\{folder_name}\new_folder\test.txt")

উপায় ১ এর আউটপুট (লাইন ভেঙে গেছে):
C:\Users\Python_Files
ew_folder\test.txt

উপায় ২ এর আউটপুট (ভেরিয়েবলের মান বসেনি):

C:\Users\{folder_name}\new_folder\test.txt

উপায় ৩ এর আউটপুট (rf কম্বিনেশন - একদম পারফেক্ট):

C:\Users\Python_Files\new_folder\test.txt

একই সাথে ভেরিয়েবলের মানও বসাতে হয় (f), আবার ব্যাকস্ল্যাশের (\) ঝামেলাও এড়াতে হয় (r), তখনই  rf বা fr ব্যবহার করা হয়। 


মিনি প্রজেক্ট 💻 সহজ নিয়মে মিনি স্টুডেন্ট প্রোফাইল

print("=== মিনি স্টুডেন্ট প্রোফাইল ম্যানেজমেন্ট ===")

# --- স্টুডেন্ট ১ এর ডেটা ---
# ১. নাম ও ঠিকানা স্ট্রিং (Immutable) হিসেবে নিলাম
name1 = "Mohammad Abdullah"
address1 = "Gongachora, Rangpur"

# ২. নাম ও ঠিকানাকে একটা টুপলে (Immutable Sequence) লক করলাম
info_student1 = (name1, address1)
age1 = 29
cgpa1 = 3.50


# --- স্টুডেন্ট ২ এর ডেটা ---
name2 = "Aziz"
address2 = "Dhaka, Bangladesh"

info_student2 = (name2, address2)
age2 = 30
cgpa2 = 3.85


# --- ডাটাবেজ (Mutable List) ---
# এবার এই দুইজনের পুরো প্রোফাইলকে আমরা একটি মেইন লিস্টের ভেতর সিরিয়ালি সাজিয়ে রাখলাম
student_database = [info_student1, age1, cgpa1, info_student2, age2, cgpa2]

# --------------------------------------------------
print("\n💻 ডাটাবেজ (List) থেকে ইনডেক্স ধরে ডেটা দেখানো হচ্ছে:\n")

# আমরা যেহেতু সিকোয়েন্সের ইনডেক্সিং [0, 1, 2] শিখেছি, তাই সরাসরি ইনডেক্স ধরে প্রিন্ট করবো
print("👤 ১ম স্টুডেন্টের নাম ও ঠিকানা (টুপল):", student_database[0])
print("🎂 ১ম স্টুডেন্টের বয়স :", student_database[1])
print("🎓 ১ম স্টুডেন্টের CGPA :", student_database[2])

print("-" * 40)

print("👤 ২য় স্টুডেন্টের নাম ও ঠিকানা (টুপল):", student_database[3])
print("🎂 ২য় স্টুডেন্টের বয়স :", student_database[4])
print("🎓 ২য় স্টুডেন্টের CGPA :", student_database[5])


=== মিনি স্টুডেন্ট প্রোফাইল ম্যানেজমেন্ট ===

💻 ডাটাবেজ (List) থেকে ইনডেক্স ধরে ডেটা দেখানো হচ্ছে:

👤 ১ম স্টুডেন্টের নাম ও ঠিকানা (টুপল): ('Mohammad Abdullah', 'Gongachora, Rangpur')
🎂 ১ম স্টুডেন্টের বয়স : 29
🎓 ১ম স্টুডেন্টের CGPA : 3.5
----------------------------------------
👤 ২য় স্টুডেন্টের নাম ও ঠিকানা (টুপল): ('Aziz', 'Dhaka, Bangladesh')
🎂 ২য় স্টুডেন্টের বয়স : 30
🎓 ২য় স্টুডেন্টের CGPA : 3.85
