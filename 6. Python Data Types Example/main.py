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


