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





name = input("Enter your name: ").strip()

# ১. নাম চেক করা: নাম ফাঁকা কি না বা নামের ভেতরে কোনো সংখ্যা আছে কি না
if name == "" or not name.replace(" ", "").isalpha():
    print("❌ Error: Please enter a valid name (letters only, no numbers)!")
else:
    # ২. বয়স চেক করার জন্য try-except ব্যবহার (যাতে age-এর জায়গায় abc দিলে ক্র্যাশ না করে)
    try:
        age_input = input("Enter your age: ")
        
        # বয়স ফাঁকা রাখা হয়েছে কি না চেক করা
        if age_input.strip() == "":
            print("❌ Error: Age cannot be empty!")
        else:
            age = float(age_input)
            
            # বয়স মাইনাস (-) বা অবাস্তব কিছু দিলে চেক করা
            if age < 0 or age > 150:
                print("❌ Invalid Input! Please enter a realistic age.")
            else:
                status = "(Adult)" if age >= 18 else "(Child)"

                print(f"Hello {name}!")
                print(f"You are {status}")

    except ValueError:
        # বয়সের ঘরে অক্ষর বা 'abc' দিলে এটি ধরবে
        print("❌ Error: Age must be a number, not letters!")


ইউজার নামের জায়গায় সংখ্যা (যেমন: 123) এবং বয়সের জায়গায় অক্ষর বা শব্দ (যেমন: abc) দিলে যাতে প্রোগ্রাম ক্র্যাশ না করে এবং ভুল আউটপুট না আসে,
তার জন্য try-except এবং স্ট্রিংয়ের বিশেষ কিছু ফাংশন (isalpha(), isdigit()) ব্যবহার করে কোডটি প্রফেশনালভাবে সাজিয়ে দেওয়া হলো।


🔍 কোডটি যেভাবে ভুল আটকাচ্ছে:

নামের জায়গায় সংখ্যা দিলে (name.replace(" ", "").isalpha()):
পাইথনের isalpha() চেক করে যে লেখ পুরোটাই অক্ষর দিয়ে তৈরি কি না। ইউজার যদি নামের ঘরে সংখ্যা দেয়, তবে এটি ধরে ফেলবে এবং সুন্দর একটি এরর মেসেজ দেবে।

বয়সের জায়গায় অক্ষর বা abc দিলে (except ValueError):
ইউজার বয়সের ঘরে abc লিখলে পাইথন সাধারণত লাল রঙের এরর দিয়ে বন্ধ হয়ে যেত। কিন্তু এখানে try-except থাকায় প্রোগ্রাম ক্র্যাশ না করে পরিষ্কার বলে দেবে যে বয়সের ঘরে শুধু সংখ্যা লিখতে হবে।

ফাঁকা রাখলে (strip()):
নাম বা বয়স কোথাও ফাঁকা এন্টার চাপলে প্রোগ্রাম সাথে সাথে তা ধরে ফেলবে।






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







text = "hello python"
result = text.isalpha()
print(result)  # False

isalpha() মেথড True রিটার্ন করে শুধুমাত্র তখনই যখন string এ শুধু অক্ষর (letter) থাকে, আর কিছু না — স্পেস, সংখ্যা, বা কোনো চিহ্ন থাকলেই False হয়ে যায়।

এখানে "hello python" এ একটা স্পেস আছে (hello আর python এর মাঝে), তাই False এসেছে। স্পেস কোনো "অক্ষর" না, তাই এটা পুরো string কে "শুধু অক্ষর" থাকার শর্ত ভেঙে দেয়।


print("hello".isalpha())        # True  -> স্পেস নেই
print("hello python".isalpha()) # False -> স্পেসের কারণে
print("hello123".isalpha())     # False -> সংখ্যার কারণে


name = input("Enter your name: ")
age = float(input("Enter your age: "))
status = "(Adult)" if age >= 18 else "(Child)"
print(f"Hello {name}!")
print(f"You are {status}")


সমস্যা: যদি ইউজার ভুলবশত name এর জায়গায় সংখ্যা লেখে (যেমন 25) আর age এর জায়গায় নাম লেখে (যেমন Rahim), তাহলে:

name = "25" — এটা কাজ করবে (error দেবে না, কিন্তু ভুল ডেটা)
age = float("Rahim") — এখানে crash করবে (ValueError)

age = float("Rahim")
# ValueError: could not convert string to float: 'Rahim'



Age এর ক্ষেত্রে — সংখ্যা কিনা validate করা (try-except দিয়ে)

name = input("Enter your name: ")

try:
    age = float(input("Enter your age: "))
except ValueError:
    print("ভুল ইনপুট! বয়স অবশ্যই সংখ্যা হতে হবে")
    exit()

status = "(Adult)" if age >= 18 else "(Child)"
print(f"Hello {name}!")
print(f"You are {status}")

এখানে try-except ব্যবহার করে বলা হচ্ছে — "যদি float() এ রূপান্তর করতে গিয়ে error আসে, তাহলে সুন্দরভাবে মেসেজ দেখাও, প্রোগ্রাম crash না করে।"

name এ সংখ্যা দিলে পাইথন error দেবে না (কারণ input() সবসময় string রিটার্ন করে), তাই এখানে নিজেকে চেক করতে হবে isalpha() বা এই ধরনের মেথড দিয়ে:

Name এর ক্ষেত্রে — সংখ্যা না হয়ে অক্ষর কিনা validate করা


name = input("Enter your name: ")

if not name.replace(" ", "").isalpha():
    print("ভুল ইনপুট! নাম শুধু অক্ষর দিয়ে হতে হবে")
    exit()

try:
    age = float(input("Enter your age: "))
except ValueError:
    print("ভুল ইনপুট! বয়স অবশ্যই সংখ্যা হতে হবে")
    exit()

status = "(Adult)" if age >= 18 else "(Child)"
print(f"Hello {name}!")
print(f"You are {status}")

এখানে name.replace(" ", "") কেন লিখলাম? কারণ নামে স্পেস থাকতে পারে (যেমন "Rahim Ahmed"), আর isalpha() স্পেস দেখলেই False দেয়। তাই আগে স্পেস সরিয়ে তারপর চেক করছি।




exit() এর কাজ

exit() হলো একটা built-in ফাংশন যেটা কল করলে পুরো পাইথন প্রোগ্রাম সাথে সাথে বন্ধ (terminate) হয়ে যায়, বাকি যত কোড নিচে আছে সব বাদ দিয়ে।

print("এই লাইনটা print হবে")
exit()
print("এই লাইনটা কখনো print হবে না")



আগের কোডে exit() কেন ব্যবহার

try:
    age = float(input("Enter your age: "))
except ValueError:
    print("ভুল ইনপুট! বয়স অবশ্যই সংখ্যা হতে হবে")
    exit()

status = "(Adult)" if age >= 18 else "(Child)"
print(f"Hello {name}!")

এখানে যুক্তিটা ছিল — যদি ইউজার ভুল ইনপুট দেয় (যেমন সংখ্যার বদলে নাম লেখে), তাহলে age ভ্যারিয়েবলে কোনো সঠিক মান থাকবে না। 
এই অবস্থায় যদি প্রোগ্রাম চলতেই থাকে, তাহলে নিচের লাইনে age >= 18 চেক করার সময় আবার crash করবে (কারণ age ভ্যারিয়েবলটাই তৈরি হয়নি)। 
তাই error মেসেজ দেখিয়ে exit() দিয়ে প্রোগ্রামটা নিরাপদে বন্ধ করে দেওয়া হচ্ছে।


⚠️ গুরুত্বপূর্ণ সতর্কতা — exit() সবসময় ব্যবহার করা ঠিক না

exit() আসলে মূলত interactive shell/interpreter (যেমন Python console বা Jupyter notebook) এ ব্যবহারের জন্য বানানো হয়েছিল, 
সাধারণ script/production code এ ব্যবহারের জন্য না। এটা site module এর উপর নির্ভর করে, যেটা সবসময় সব environment এ available না-ও থাকতে পারে।


exit()       # শুধু interactive shell এর জন্য বানানো, script এ ব্যবহার না করাই ভালো
quit()       # exit() এর মতোই, এটাও শুধু interactive use এর জন্য
sys.exit()   # Script/production code এর জন্য সঠিক পদ্ধতি




সম্পূর্ণ চূড়ান্ত কোড (Full Robust Version)


# নাম নেওয়া
while True:
    name = input("Enter your name: ").strip()
    if name and name.replace(" ", "").isalpha():
        break
    print("ভুল ইনপুট! নাম শুধু অক্ষর দিয়ে হতে হবে, আবার চেষ্টা করো")

# বয়স নেওয়া
while True:
    age_input = input("Enter your age: ")
    try:
        age = float(age_input)
        if age < 0 or age > 120:
            print("ভুল ইনপুট! বয়স ০ থেকে ১২০ এর মধ্যে হতে হবে")
            continue
        break
    except ValueError:
        print("ভুল ইনপুট! বয়স অবশ্যই সংখ্যা হতে হবে, আবার চেষ্টা করো")

status = "(Adult)" if age >= 18 else "(Child)"
print(f"Hello {name}!")
print(f"You are {status}")
