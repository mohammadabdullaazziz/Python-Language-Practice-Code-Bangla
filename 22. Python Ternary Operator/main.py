Ternary Operator হলো if-else কে এক লাইনে লেখার একটা সংক্ষিপ্ত (shorthand) পদ্ধতি। এটাকে Conditional Expression ও বলা হয়।

"Ternary" শব্দের মানে হলো ৩টা অংশ (operand) নিয়ে কাজ করা — অন্য বেশিরভাগ operator (যেমন +, -) ২টা অংশ নিয়ে কাজ করে (এগুলোকে binary operator বলে),
কিন্তু ternary operator ৩টা অংশ নিয়ে কাজ করে।

Syntax:

[সত্য হলে কি পাবে]  if  [শর্ত]  else  [মিথ্যা হলে কি পাবে]



সাধারণ if-else বনাম টনারি অপারেটর

সাধারণ if-else কোড (৪ লাইন):

age = 20

if age >= 18:
    status = "Adult"
else:
    status = "Minor"

print(status) # Output: Adult


টনারি অপারেটরে (এক লাইন):

age = 20

status = "Adult" if age >= 18 else "Minor"

print(status) # Output: Adult




marks = 40

# সিনট্যাক্স: সত্যের মান + if + শর্ত + else + মিথ্যার মান
status = "Pass" if marks >= 33 else "Fail"

print(status)  # Output: Pass

"পাস (Pass)" করবো যদি (if) মার্ক ৩৩ বা তার বেশি হয়, নাহলে (else) "ফেল (Fail)" করবো।





number = 10
result = "Even" if number % 2 == 0 else "Odd"
print(str(number) + " is " + result)
# Output: 10 is Even




age = 20
eligibility = "Can vote" if age >= 18 else "Can not vote"

print(eligibility)  # Output: Can vote



name = input("Enter your name: ")
age = float(input("Enter your age: "))

status = "(Adult)" if age >= 18 else "(Child)"

print(f"Hello {name}!")
print(f"You are {status}")



user_code = float(input("Enter your 5 digit Code: "))
first_name = "File Open"
last_name = "Failed"

result = first_name if user_code == 12345 else last_name

print(result)




user_code = float(input("Enter your 5 digit code: "))
file_name = "Secret_File.pdf"

access = "File Open" if user_code == 12345 else "Failed"

# f-string এর ভেতরে সরাসরি Ternary Expression
final = f"Access: {access}!\nYour File({file_name}) Now {'Open Your File' if user_code == 12345 else 'Locked Your File'}"

print(final)

🟡 উপায় ২: আলাদা ভেরিয়েবল ব্যবহার করে (সহজে পড়ার জন্য)
কোড যেন দেখতে পরিষ্কার থাকে এবং সহজে বোঝা যায়, সেজন্য দ্বিতীয় কন্ডিশনটি আলাদা একটি ভেরিয়েবলে রেখে সাজানো যেতে পারে:

user_code = float(input("Enter your 5 digit code: "))
file_name = "Secret_File.pdf"

access = "File Open" if user_code == 12345 else "Failed"
file_status = "Open Your File" if user_code == 12345 else "Locked Your File"

final = f"Access: {access}!\nYour File({file_name}) Now {file_status}"

print(final)





username = input("Enter Your Username: ")
name1 = "Mohammad"
name2 = "Arman"

user_access = name1 if username == "password" else name2
print(user_access)
