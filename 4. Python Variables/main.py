ভেরিয়েবল:

ভেরিয়েবল হলো একটি নামযুক্ত বাক্স যেখানে ডেটা বা তথ্য সংরক্ষণ করা হয়।
Python variable মানে হলো এমন একটি নামযুক্ত জায়গা, যেখানে কোনো মান রাখা হয় এবং পরে সেই মান ব্যবহার করা যায়। সহজভাবে বললে, variable হলো ডেটা রাখার কন্টেইনারের মতো।


Variable কেন লাগে: 

প্রোগ্রামে ডেটা সংরক্ষণ করতে।

বারবার একই মান লিখতে না হয়ে নাম দিয়ে ব্যবহার করতে।

মান বদলালে সহজে আপডেট করতে।


ভেরিয়েবল তৈরি করা
পাইথনে ভেরিয়েবল ডিক্লেয়ার করার জন্য কোনো কমান্ড নেই। Python-এ ভ্যারিয়েবল ঘোষণা করার সময় আলাদা করে টাইপ লিখতে হয় না। সরাসরি মান দিয়ে দিলেই Python বুঝে নেয়।

ভেরিয়েবলকে কোনো নির্দিষ্ট টাইপ দিয়ে ডিক্লেয়ার করার প্রয়োজন নেই, এবং সেট করার পরেও সেগুলোর টাইপ পরিবর্তন করা যেতে পারে। 
Python-এ ভেরিয়েবল তৈরি করা খুবই সহজ। অন্যান্য অনেক প্রোগ্রামিং ভাষার মতো এখানে ডেটা টাইপ (যেমন: int, string) আগে থেকে ঘোষণা করতে হয় না। 
যখনই কোনো ভেরিয়েবলে মান অ্যাসাইন (Assign) করা হয় , সেটি স্বয়ংক্রিয়ভাবে তৈরি হয়ে যাবে। এর জন্য = (assignment operator) ব্যবহার করা হয়। 

name = "Abdullah"       # এখানে name একটি ভেরিয়েবল, যা টেক্সট (String) ধরে রেখেছে
age = 29                # এখানে age একটি ভেরিয়েবল, যা পূর্ণসংখ্যা (Integer) ধরে রেখেছে
gpa = 3.85              # এখানে gpa একটি ভেরিয়েবল, যা দশমিক সংখ্যা (Float) ধরে রেখেছে

# ভেরিয়েবলগুলো প্রিন্ট 
print(name)
print(age)
print(gpa)




name = "Abdullah"
age = 30
height = 5.2

print("My name is " + name + " and I am " + str(age) + " years old. My height is " + str(height) + " feet.")

print(f"My name is {name} and I am {age} years old. My height is {height} feet.")

print(f'My name is {name} and I am {age} years old. My height is {height} feet.')

print(f'''My name is {name} 
and I am {age} years old. 
My height is {height} feet.''')

print(f"""My name is {name} 
and I am {age} years old. 
My height is {height} feet.""")


 ভিতরে Single Quote থাকলে Double ব্যবহার 

text = "He said, 'Python is awesome!'"
print(f'{text}')  # এখানে Double ভালো



ভিতরে Double Quote থাকলে Single ব্যবহার 

text = 'She told me, "Learn Python!"'
print(f'{text}')  # এখানে Single 



মাল্টিলাইন টেক্সট (যেমন ইমেইল বা লম্বা মেসেজ)

message = f'''Dear {name},
Your age is {age} and height is {height} feet.
Thank you!'''
print(message)


f-string-এর ভিতরে f-string (নেস্টেড)

person = "Abdullah"
print(f'My name is {f"Mr. {person}"}')  # ভিতরে Double, বাইরে Single



f-string-এর ভিতরে একই ধরনের Quote ব্যবহার করা যাবে না

# ❌ ভুল (ভিতরে-বাইরে একই Quote)
print(f'My name is {name} and I'm {age}')  # Syntax Error!

# ✅ ঠিক (ভিতরে Single, বাইরে Double)
print(f"My name is {name} and I'm {age}")


f-string-এ Escape Character (\) ব্যবহার 

print(f'My name is {name}. I\'m {age} years old.')  # \' দিয়ে Single এস্কেপ




name = "Abdullah"
age = 30
height = 5.2

print("Name:", name)
print("Age:", age)
print("Height:", height)

print("Name:" + name)
print("Age:" + str(age))
print("Height:" + str(height))





ভেরিয়েবলের নাম:

একটি ভেরিয়েবলের সংক্ষিপ্ত নাম (যেমন x এবং y) অথবা আরও বর্ণনামূলক নাম (age, carname, total_volume) থাকতে পারে।


পাইথন ভেরিয়েবলের নিয়মাবলী:

একটি ভেরিয়েবলের নাম অবশ্যই একটি অক্ষর বা আন্ডারস্কোর (underscore) অক্ষর দিয়ে শুরু হতে হবে।
একটি ভেরিয়েবলের নাম কোনো সংখ্যা দিয়ে শুরু হতে পারে না।
একটি ভেরিয়েবলের নামে শুধুমাত্র আলফানিউমেরিক অক্ষর এবং আন্ডারস্কোর (A-z, 0-9, এবং _) থাকতে পারে।
ভেরিয়েবলের নাম কেস-সেনসিটিভ (case-sensitive) হয় (age, Age এবং AGE তিনটি ভিন্ন ভেরিয়েবল)।  Name আর name দুটো আলাদা ভেরিয়েবল! সঠিক: my_var = 10, _var = 5 ভুল: 1st_number = 10

একটি ভেরিয়েবলের নাম পাইথনের কোনো কীওয়ার্ড হতে পারে না। রিজার্ভড কিওয়ার্ড (Reserved Keywords): Python-এর নিজস্ব কিছু সংরক্ষিত শব্দ আছে 
(যেমন: if, else, print, while, for)। এগুলোকে ভেরিয়েবলের নাম হিসেবে ব্যবহার করা যাবে না।


Legal variable names:

myvar = "Abdullah"
my_var = "Abdullah"
_my_var = "Abdullah"
myVar = "Abdullah"
MYVAR = "Abdullah"
myvar2 = "Abdullah"



Illegal variable names:

2myvar = "Abdullah"
my-var = "Abdullah"
my var = "Abdullah"

my_name = "Abdullah"    # ✅ সঠিক
myName = "Abdullah"     # ✅ সঠিক (camelCase)
_name = "Abdullah"      # ✅ সঠিক
2name = "Abdullah"     # ❌ ভুল — সংখ্যা দিয়ে শুরু করা যাবে না
my-name = "Abdullah"  # ❌ ভুল — হাইফেন ব্যবহার করা যাবে না
class = "Abdullah"      # ❌ ভুল — reserved keyword ব্যবহার করা যাবে না



ডাইনামিক টাইপিং (Dynamic Typing)
Python একটি ডাইনামিকালি টাইপড ভাষা। এর মানে হলো,  একটি ভেরিয়েবলে প্রথমে এক ধরণের ডেটা রাখার পর পরবর্তীতে একই ভেরিয়েবলে অন্য ধরণের ডেটা রাখা যায়। 
Python নিজে থেকেই তার টাইপ বদলে নেয়।

x = 10          # x এখন একটি Integer (পূর্ণসংখ্যা)
print(x)

x = "Hello"     # x-এর ভেতরে এবার String (টেক্সট) রাখা হলো 
print(x)



একাধিক শব্দের ভেরিয়েবলের নাম
একাধিক শব্দযুক্ত ভেরিয়েবলের নাম পড়া কঠিন হতে পারে।
এগুলোকে আরও সহজে পঠনযোগ্য করার জন্য কয়েকটি কৌশল ব্যবহার করা যাবে:

ক্যামেল কেস (Camel Case)
প্রথম শব্দটি ছাড়া প্রতিটি শব্দ বড় হাতের অক্ষর দিয়ে শুরু হয়:
myVariableName = "Abdullah"

প্যাসকেল কেস (Pascal Case)
প্রতিটি শব্দ বড় হাতের অক্ষর দিয়ে শুরু হয়:
MyVariableName = "Abdullah"

স্নেক কেস (Snake Case)
প্রতিটি শব্দ একটি আন্ডারস্কোর (underscore) অক্ষর দ্বারা আলাদা করা হয়:
my_variable_name = "Abdullah"



একাধিক ভেরিয়েবলে একাধিক মান
পাইথন এক লাইনে একাধিক ভেরিয়েবলে মান অ্যাসাইন করার সুযোগ দেয়:

উদাহরণ: 
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z

a, b, c = 5, 10, 15
print(a) # আউটপুট: 5
print(b) # আউটপুট: 10
print(c) # আউটপুট: 15
      



      
একই মান একাধিক ভেরিয়েবলে 
এবং একই মান এক লাইনে একাধিক ভেরিয়েবলে অ্যাসাইন করা যাবে :

উদাহরণ
x = y = z = "Orange"
print(x)
print(y)
print(z)




x = y = z = "Mango"
print(x) # আউটপুট: Mango
print(y) # আউটপুট: Mango
print(z) # আউটপুট: Mango



একটি কালেকশন আনপ্যাক করা
যদি একটি লিস্ট, টাপল ইত্যাদিতে একাধিক ভ্যালুর একটি কালেকশন থাকে, তাহলে পাইথন সেই ভ্যালুগুলোকে ভেরিয়েবলে বের করে আনার সুযোগ দেয়। একে আনপ্যাকিং বলা হয়।

উদাহরণ

একটি লিস্ট আনপ্যাক:

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)



আউটপুট ভেরিয়েবল
ভেরিয়েবল আউটপুট করার জন্য প্রায়শই print() ফাংশন ব্যবহার করা হয়।
Example
x = "Python is awesome"
print(x)



print() ফাংশনে, কমা দিয়ে আলাদা করে একাধিক ভেরিয়েবল আউটপুট করা যায়:
 
উদাহরণ
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)




একাধিক ভেরিয়েবল আউটপুট করতে + অপারেটরটিও ব্যবহার করা যায়:

উদাহরণ 
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)




print() ফাংশনে একাধিক ভেরিয়েবল আউটপুট করার সবচেয়ে ভালো উপায় হলো সেগুলোকে কমা দিয়ে আলাদা করা, যা বিভিন্ন ডেটা টাইপও সমর্থন করে:

উদাহরণ
x = 5
y = "Abdullah"
print(x, y)



ভেরিয়েবলের ডেটা টাইপ চেক করা
কোনো ভেরিয়েবলে বর্তমানে কী ধরণের ডেটা আছে তা জানার জন্য type() ফাংশন ব্যবহার করা হয়।

name = "Abdullah"
score = 95
height = 5.8


print(type(name))   # আউটপুট: <class 'str'> (String)
print(type(score))  # আউটপুট: <class 'int'> (Integer)
print(type(height)) # আউটপুট: <class 'float'> (Float)

