পাইথনে কোনো শর্তের ওপর ভিত্তি করে সিদ্ধান্ত নেওয়ার জন্য if এবং else স্টেটমেন্ট ব্যবহার করা হয়।

সহজ কথায়: "যদি (if) শর্তটি সত্য হয়, তবে এই কাজ করো; তা না হলে (else), অন্য কাজ করো।"


if-else এর মূল গঠন (Syntax)

if শর্ত (Condition):
    # শর্ত সত্য (True) হলে এই ব্লকের কোড চলবে
else:
    # শর্ত মিথ্যা (False) হলে এই ব্লকের কোড চলবে



if-else নিজে সরাসরি True বা False রিটার্ন (Return) করে না।

if-else মূলত সিদ্ধান্ত নিয়ে কোড চালানোর (Execute করার) কাজ করে।


if এর পাশের শর্তটি (Condition):

শর্ত নিজে হিসাব করে True বা False তৈরি করে।

যেমন: marks >= 40 — এটি হিসাব করে পাইথন পায় True অথবা False।


if-else এর কাজ:if-else শুধু ওই রেজাল্টটা দেখে সিদ্ধান্ত নেয়:শর্ত True হলে if-এর ভেতরের কোড চালায়
।শর্ত False হলে else-এর ভেতরের কোড চালায়।




marks = 65

if marks >= 40:
    print("Congratulations! You passed.")
else:
    print("Sorry! You failed.")

Congratulations! You passed.


গুরুত্বপূর্ণ বিষয় (Indentation/ইনডেন্টেশন):

পাইথনে if বা else-এর লাইনের শেষে একটি ক্লোন (:) দিতে হয় এবং ভেতরের কোডগুলোকে ৪টি স্পেস (বা একটি Tab) ডানে সরিয়ে লিখতে হয়। একে ইনডেন্টেশন বলে।


১. কোলন (:) কেন দিতে হয়?
পাইথনে কোলন (:) দিয়ে পাইথন ইন্টারপ্রেটারকে (Python Interpreter) বলা হয়: "শর্ত লেখা শেষ, এবার নতুন একটি কোড ব্লক শুরু হতে যাচ্ছে।"


যখন বলা হয় if marks >= 40:, কোলনটি মূলত ইঙ্গিত দেয়—"যদি মার্কস ৪০ বা তার বেশি হয়, তবে..."

পাইথন বোঝে যে এই কোলনের পরেই এমন কিছু নির্দেশ বা কোড আসবে যা এই শর্তটি সত্য (True) হলেই কেবল চালু করা উচিত।

একইভাবে else: এর কোলনটির মানে হলো—"অন্যথায় (যদি উপরের শর্ত মিথ্যা হয়), তবে..."

সংক্ষেপে: কোলন (:) হলো একটি দরজার মতো, যা নির্দেশ করে যে এর ভেতরে নতুন একটি কোডের ব্লক বা কাজ রয়েছে।


২. ৪টি স্পেস বা ১টি ট্যাব ডানে সরিয়ে কেন লিখতে হয়? (Indentation)

প্রোগ্রামিংয়ের ভাষায় কোডকে এভাবে ডানে সরিয়ে লেখাকে Indentation (ইনডেন্টেশন) বলা হয়।

অন্যান্য অনেক প্রোগ্রামিং ভাষায় (যেমন: C, C++, Java, JavaScript) একটি শর্তের ভেতরের কোড বোঝাতে কার্লি ব্র্যাকেট {} ব্যবহার করা হয়। কিন্তু পাইথনে কোনো ব্র্যাকেট ব্যবহার করা হয় না।

এর বদলে পাইথন ডানের খালি জায়গা (Space) দেখে বুঝতে পারে কোনটা কার ভেতরের কোড!


উদাহরণ দিয়ে

marks = 65

if marks >= 40:
    print("Congratulations! You passed.")  # এটি if-এর ভেতরে
    print("Great job!")                    # এটিও if-এর ভেতরে

print("Program finished.")                  # এটি if-এর বাইরে



ভেতরের অংশ: print("Congratulations! You passed.") লাইনটির আগে ৪টি স্পেস আছে, তাই পাইথন জানে এই লাইনটি শুধু তখনই চলবে যখন marks >= 40 সত্য হবে।

বাইরের অংশ: print("Program finished.") একদম বাম পাশ থেকে শুরু হয়েছে, কোনো স্পেস নেই। তাই পাইথন বোঝে এটি if-এর ভেতরের কোড নয়। মার্কস ৪০-এর কম হোক বা বেশি হোক, এই লাইনটি সবসময়ই প্রিন্ট হবে।

JavaScript, C, C++, C# বা Java-র মতো ভাষায় যে কাজ করার জন্য কার্লি ব্র্যাকেট {} ব্যবহার করা হয়, পাইথনে ঠিক সেই একই কাজ করার জন্য কোলন : এবং ইনডেন্টেশন (ডানে স্পেস দেওয়া) ব্যবহার করা হয়।


  
(Even or Odd Check):

number = 7

if number % 2 == 0:
    print("The number is Even.")
else:
    print("The number is Odd.")

The number is Odd.



  
age = 20
has_nid = True

if age >= 18 and has_nid:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")



ওয়েবসাইট লগইন সিস্টেম (Login Validation) ইউজারনেম এবং পাসওয়ার্ড দুটিই সঠিক হলে লগইন করতে দেবে।

username = "admin"
password = "12345password"

if username == "admin" and password == "12345password":
    print("Login successful! Welcome to your dashboard.")
else:
    print("Login failed! Invalid username or password.")

Login successful! Welcome to your dashboard.








String, Number, এবং Boolean যা যা আমরা ইতিমধ্যে শিখেছি, সেগুলো দিয়ে সহজ একটি if-else কোড

# 1. String Test (লেখা থাকলে True)
user_name = "Alex"

if user_name:
    print("1. Name found: Welcome, Alex!")
else:
    print("1. Name missing: Please enter your name.")


# 2. Empty String Test (খালি টেক্সট হলে False)
email_address = ""

if email_address:
    print("2. Email found: Proceed to next step.")
else:
    print("2. Email missing: Email address is required!")


# 3. Number Test (০ ছাড়া যেকোনো সংখ্যা True)
wallet_balance = 500

if wallet_balance:
    print("3. Balance status: You have money in your wallet.")
else:
    print("3. Balance status: Your wallet is empty (0 balance).")


# 4. Zero Number Test (০ হলে False)
discount_amount = 0

if discount_amount:
    print("4. Discount status: Discount applied!")
else:
    print("4. Discount status: No discount for this purchase.")


# 5. Boolean Test (সরাসরি True / False)
is_account_active = True

if is_account_active:
    print("5. Account status: Your account is active.")
else:
    print("5. Account status: Your account is suspended.")


1. Name found: Welcome, Alex!
2. Email missing: Email address is required!
3. Balance status: You have money in your wallet.
4. Discount status: No discount for this purchase.
5. Account status: Your account is active.


💡 সংক্ষেপে যে ৩টি জিনিস:

String: টেক্সট থাকলে True, একদম খালি "" হলে False

Number: যেকোনো সংখ্যা থাকলে True, শুধু 0 হলে False

Boolean: True থাকলে True, False থাকলে False





পাইথনে String Methods (যেমন: .isupper(), .isnumeric(), .startswith(), .lower() ইত্যাদি) মূলত কোনো টেক্সট বা ডাটা সঠিক বিন্যাসে আছে কি না তা যাচাই করার জন্য সবচেয়ে বেশি ব্যবহৃত হয়। 
এগুলো সরাসরি True অথবা False রিটার্ন করে, যা if-else কন্ডিশনে ব্যবহার করা খুব সহজ।


# Example 1: .isupper() - Check if all characters are UPPERCASE


promo_code = "SAVE50"

if promo_code.isupper():
    print("1. Promo code format valid: All letters are UPPERCASE.")
else:
    print("1. Invalid promo code! Must be written in capital letters.")




# Example 2: .islower() - Check if all characters are lowercase

user_handle = "john_doe"

if user_handle.islower():
    print("2. Handle approved: All characters are lowercase.")
else:
    print("2. Invalid handle! Capital letters are not allowed.")



# Example 3: .isnumeric() - Check if string contains only numbers

phone_input = "01712345678"

if phone_input.isnumeric():
    print("3. Phone number valid: Contains only numeric digits.")
else:
    print("3. Invalid phone number! Letters or symbols are not allowed.")



# Example 4: .isalpha() - Check if string contains only alphabets

first_name = "Alex"

if first_name.isalpha():
    print("4. Name format valid: Contains only letters.")
else:
    print("4. Invalid name! Numbers or spaces are not allowed.")



# Example 5: .isalnum() - Check if string contains letters and/or numbers (No spaces/symbols)

account_id = "User123"

if account_id.isalnum():
    print("5. Account ID valid: Alphanumeric characters detected.")
else:
    print("5. Invalid ID! Special characters or spaces found.")



# Example 6: .startswith() - Check starting text

website_url = "https://google.com"

if website_url.startswith("https://"):
    print("6. Connection secure: URL starts with https://")
else:
    print("6. Insecure connection! Missing https:// prefix.")



# Example 7: .endswith() - Check ending text

user_email = "alex@gmail.com"

if user_email.endswith("@gmail.com"):
    print("7. Domain verified: Gmail address accepted.")
else:
    print("7. Access restricted: Only Gmail accounts allowed.")


# Example 8: .strip() - Remove accidental extra spaces

search_query = "   laptop   "

# Removing spaces first, then checking if string is non-empty
cleaned_query = search_query.strip()

if cleaned_query:
    print("8. Search query processed: Searching for '" + cleaned_query + "'")
else:
    print("8. Search failed: Please type a search word.")



# Example 9: .lower() - Normalizing string comparison

security_answer = "BANGLADESH"

# Converting user input to lowercase before comparing
if security_answer.lower() == "bangladesh":
    print("9. Security check passed: Answer matches.")
else:
    print("9. Security check failed: Incorrect answer.")



1. Promo code format valid: All letters are UPPERCASE.
2. Handle approved: All characters are lowercase.
3. Phone number valid: Contains only numeric digits.
4. Name format valid: Contains only letters.
5. Account ID valid: Alphanumeric characters detected.
6. Connection secure: URL starts with https://
7. Domain verified: Gmail address accepted.
8. Search query processed: Searching for 'laptop'
9. Security check passed: Answer matches.




💡 সহজে মনে রাখার সামারি:
isupper() / islower(): ক্যাপিটাল নাকি স্মল লেটার যাচাই করে।

isnumeric() / isalpha() / isalnum(): শুধু সংখ্যা, শুধু অক্ষর, নাকি সংখ্যা-অক্ষরের মিশ্রণ তা চেক করে।

startswith() / endswith(): শুরু বা শেষের ফরম্যাট মেলাতে ব্যবহার হয়।

strip() / lower(): স্পেস দূর করতে এবং ছোট হাতের করে নিরপেক্ষ তুলনা (Case-insensitive comparison) করতে ব্যবহৃত হয়।





(সর্বদা not আগে, মাঝে and, আর or সবার শেষে।)



ব্যাংক থেকে টাকা তোলার কোড (ATM Withdrawal) এখানে দুটি বিষয় চেক করা হবে: তোলা টাকা মোট ব্যালেন্সের চেয়ে কম বা সমান কি না এবং উত্তোলনের পরিমাণ ০-এর বেশি কি না।

balance = 5000
withdraw_amount = 1200

if withdraw_amount > 0 and withdraw_amount <= balance:
    print("Transaction successful! Please collect your cash.")
else:
    print("Transaction failed! Insufficient balance or invalid amount.")


Transaction successful! Please collect your cash.





অনলাইন কেনাকাটায় ফ্রি ডেলিভারি (Discount / Free Delivery

পণ্য যদি ১০০০ টাকার বেশি হয় অথবা মেম্বারশিপ প্রিমিয়াম (is_premium = True) হয়, তবে ফ্রি ডেলিভারি পাবে।

cart_total = 800
is_premium_member = True

if cart_total >= 1000 or is_premium_member:
    print("You qualify for FREE Delivery!")
else:
    print("Delivery fee added to your bill.")

You qualify for FREE Delivery!




অনলাইন শপিং ডিসকাউন্ট এবং শিপিং সিস্টেম

শর্ত বা লজিক:

একজন ক্রেতা ফ্রি শিপিং পাবেন যদি:

তিনি একজন প্রিমিয়াম মেম্বার হন (is_premium = True)
অথবা
তার কেনাকাটার পরিমাণ ৫০০ টাকার বেশি হয় এবং তিনি কোনো স্পেশাল কুপন কোড ব্যবহার না করেন (not has_special_coupon) [কুপন থাকলে ফ্রি শিপিংয়ের বদলে আলাদা ডিসকাউন্ট মেলে]।

is_premium = False
cart_total = 600
has_special_coupon = False

# and, or, not একসাথে ব্যবহার
if is_premium or (cart_total > 500 and not has_special_coupon):
    print("Eligible for FREE Shipping!")
else:
    print("Standard shipping fee applied.")






স্মার্ট হোম সিকিউরিটি অ্যালার্ম সিস্টেম

শর্ত বা লজিক:

একটি বাড়ির সিকিউরিটি অ্যালার্ম বেজে উঠবে যদি:

রাতে কোনো দরজার সেন্সর ট্রিপ হয় (door_sensor = True এবং is_night = True)

অথবা

গতির সেন্সর ধরা পড়ে (motion_detected = True) কিন্তু বাড়ির মালিক উপস্থিত না থাকেন (not owner_present)।

door_sensor = False
is_night = True
motion_detected = True
owner_present = False

# and, or, not একসাথে
if (door_sensor and is_night) or (motion_detected and not owner_present):
    print("ALARM! Security breached!")
else:
    print("System normal. All secure.")




রেজিস্ট্রেশন ফরম যাচাই (String Method + and + not)

এখানে চেক করা হচ্ছে: ইউজারনেমটি কি শুধুমাত্র অক্ষর (isalpha()), দৈর্ঘ্য কি বড়, এবং এটি কি খালি নয়?

username_input = "Alex"

# and এবং not এর ব্যবহার
if username_input.isalpha() and not username_input.isspace() and len(username_input) >= 3:
    print("1. Registration success: Username is valid.")
else:
    print("1. Registration failed: Username must contain only letters and be at least 3 characters.")


1. Registration success: Username is valid.




ওয়েবসাইট ফাইল টাইপ যাচাই (String Method + or)

একটি ফাইল আপলোড করতে দেওয়া হবে যদি সেটি ছবি হয় (মানে ডোমেইন/ফাইল এক্সটেনশন .jpg বা .png দিয়ে শেষ হয়)।

file_name = "profile_picture.jpg"

# .endswith() এর সাথে or এর ব্যবহার
if file_name.endswith(".jpg") or file_name.endswith(".png"):
    print("2. Upload success: Image format supported.")
else:
    print("2. Upload failed: Only .jpg and .png files are allowed.")


2. Upload success: Image format supported.




পাসওয়ার্ড সুরক্ষা পরীক্ষা (and + not + String Methods)

পাসওয়ার্ডে কোনো স্পেস থাকতে পারবে না (not contains space), সব অক্ষর স্মল লেটার হতে পারবে না (not islower), এবং নম্বর থাকতে পারবে না বলা যাবে না।

password_input = "Admin123"

# and, not এবং string methods একসাথে
if not password_input.islower() and not password_input.isupper() and not password_input.isnumeric():
    print("3. Password strong: Contains mixed character types.")
else:
    print("3. Password weak: Must mix uppercase, lowercase, or numbers.")

3. Password strong: Contains mixed character types.




অফিসিয়াল ইমেইল এবং ফোন নম্বর চেক (and + or + not)

ব্যবসার ইমেইল অবশ্যই @company.com হতে হবে অথবা ফোন নম্বর সংখ্যা হতে হবে, কিন্তু কোনোটিই খালি হতে পারবে না (not).

contact_email = "employee@company.com"
contact_phone = "01700000000"

if (contact_email.endswith("@company.com") or contact_phone.isnumeric()) and not (contact_email == "" and contact_phone == ""):
    print("4. Verification passed: Contact information accepted.")
else:
    print("4. Verification failed: Provide a valid company email or phone number.")

4. Verification passed: Contact information accepted.



ড্রাইভিং ফিটনেস চেক (and + not)
বয়স ১৮-এর বেশি হতে হবে, চোখের দৃষ্টি ড্রাইভিং টেস্টে পাস হতে হবে (has_passed_vision = True), এবং কোনো ট্রাফিক ভায়োলেশন থাকা যাবে না (not has_traffic_violations).

driver_age = 25
has_passed_vision = True
has_traffic_violations = False

# and এর সাথে not এর ব্যবহার
if driver_age >= 18 and has_passed_vision and not has_traffic_violations:
    print("5. Driver eligible: License renewal approved.")
else:
    print("5. Driver ineligible: Failed requirements or has violation history.")

5. Driver eligible: License renewal approved.




ব্যাংক ক্রেডিট কার্ড আবেদন (and + or + not জটিল লজিক)
আবেদনকারী কার্ড পাবেন যদি:

তার বেতন ৫০,০০০ টাকা বা বেশি হয় এবং ক্রেডিট স্কোরে কোনো লাল দাগ না থাকে (not has_bad_credit)

অথবা

তিনি ব্যাংকের ভিআইপি গ্রাহক হন (is_vip_customer = True)


monthly_salary = 60000
has_bad_credit = False
is_vip_customer = False

# and, or, not এর একসাথে ব্যবহার
if (monthly_salary >= 50000 and not has_bad_credit) or is_vip_customer:
    print("6. Credit card status: Approved!")
else:
    print("6. Credit card status: Rejected due to low salary or bad credit history.")


6. Credit card status: Approved!


💡 তিনটি লজিক্যাল অপারেটর সংক্ষেপে:

and: দুটি বা সবকটি শর্ত সত্য হলে কাজ করবে।

or: যেকোনো একটি শর্ত সত্য হলেই কাজ করবে।

not: শর্তটিকে ঠিক উল্টে দেবে (True কে False, আর False কে True)।
