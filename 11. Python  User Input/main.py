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
