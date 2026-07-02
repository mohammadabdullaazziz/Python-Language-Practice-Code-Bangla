str (String): পাইথনে যেকোনো ধরনের লেখা, টেক্সট, অক্ষর, শব্দ বা বাক্যকে স্ট্রিং বলা হয়।

এটি ইমিউটেবল (Immutable) — অর্থাৎ একবার তৈরি করলে এর ভেতরের কোনো অক্ষর পরিবর্তন করা যায় না।

সিঙ্গেল কোটেশন (' ') বা ডাবল কোটেশন (" ") এর ভিতরে লিখতে হয়।

Python-এ স্ট্রিং Unicode সাপোর্ট করে, তাই বাংলা, আরবি, ইংরেজি—সব ভাষাই লেখা যায়।

"Python"
"Hello World"
"Bangladesh"
"12345" (এটি দেখতে সংখ্যা হলেও কোটেশনের কারণে String)




যখন কোনো লেখাকে Single Quote (' '), Double Quote (" ") অথবা Triple Quote (''' ''' / """ """) এর মধ্যে লেখা হয়, তখন সেটি String হয়।

name = "Arman"
country = 'Bangladesh'

print(name)
print(country)


String তৈরি করার ৩টি উপায়

১. Double Quote

language = "Python"

২. Single Quote

language = 'Python'

৩. Triple Quote

একাধিক লাইনের (Multi-line) String লেখার জন্য।

message = """
Hello
Welcome to Python
Programming
"""

print(message)




# কোটেশন চিহ্নের ভেতর নাম এবং ঠিকানা রাখা হলো
user_name = "Mohammad Abdullah"
user_address = 'Gongachora, Rangpur'

# স্ক্রিনে প্রিন্ট করে দেখা
print("Name:", user_name)
print("Address:", user_address)

print("-" * 30)

# পাইথনের কাছে এর আসল জাত বা ডাটা টাইপ চেক করা
print("user_name Data Type:", type(user_name))

Name: Mohammad Abdullah
Address: Gongachora, Rangpur
------------------------------
user_name Data Type: <class 'str'>

Reassign-------

# ধাপ ১: প্রথমে নাম এবং ঠিকানা সেট 
user_name = "Mohammad Abdullah"
user_address = "Gongachora, Rangpur"

print("--- প্রথম বারের ডেটা ---")
print("Name:", user_name)
print("Address:", user_address)

print("-" * 30)

# ধাপ ২: এবার  Re-assign (নতুন মান দিয়ে প্রতিস্থাপন) 
user_name = "Aziz"
user_address = "Rangpur, Bangladesh"

print("--- Re-assign করার পরের ডেটা ---")
print("Name:", user_name)
print("Address:", user_address)

মেমোরি ইমিউটেবিলিটি (Immutability)
পাইথনে স্ট্রিং হলো Immutable। এর মানে হলো, একবার মেমোরিতে একটা স্ট্রিং তৈরি হয়ে গেলে তাকে আর টেনে-হিঁচড়ে পরিবর্তন করা বা তার ভেতরের কোনো অক্ষর মুছে ফেলা যায় না। 
যদি ওটা বদলাতে চাওয়া হয়, পাইথন মেমোরিতে সম্পূর্ণ নতুন আরেকটা স্ট্রিং অবজেক্ট তৈরি করে নেয়। 

স্ট্রিংয়ের ভেতরের প্রতিটি অক্ষরের একটি নির্দিষ্ট রোল নম্বর বা ঠিকানা থাকে, যাকে প্রোগ্রামিংয়ে Index বলা হয়। পাইথনে এই গোনা শুরু হয় 0 (শূন্য) থেকে।

সংখ্যা বনাম স্ট্রিং (খুব জরুরি খটকা)
কোটেশনের ভেতর যা-ই লিখা হবে , পাইথন চোখ বন্ধ করে তাকে লেখা বা স্ট্রিং ভেবে নেবে।

age = 25  এটি একটি Integer (পূর্ণসংখ্যা, যা দিয়ে যোগ-বিয়োগ করা যাবে)।
age = "25" এটি একটি String (টেক্সট, পাইথন একে সংখ্যা মনে করবে না, তাই এটি দিয়ে কোনো গাণিতিক হিসাব করা যাবে না)।

পাইথনে একটা স্ট্রিং তৈরি করলেই, তার ভেতর কোনো অক্ষর না লিখলেও (খালি স্ট্রিং ""), পাইথন ইঞ্জিনের ব্যাকগ্রাউন্ড ট্র্যাকিংয়ের জন্য
মেমোরিতে সর্বনিম্ন ৪৯ বাইট থেকে ৮০ বাইট বেস বা হেডার জায়গা আগে থেকেই বুক হয়ে যায়। 
সংস্কৃতির ওপর ভিত্তি করে এটি সাধারণত ৪৯ বাইট (বা ৩৯২ বিট) হয়ে থাকে।

সাধারণ ইংরেজি অক্ষর (Latin-1 / ASCII)  প্রতি অক্ষরে ১ বাইট (৮ বিট) যদি শুধু সাধারণ ইংরেজি নাম,
সংখ্যা বা চিহ্ন লিখা হয় (যেমন: Mohammad Abdullah), তবে প্রতি ১টি অক্ষরের জন্য মেমোরিতে মাত্র ১ বাইট করে জায়গা যোগ হবে।

জটিল বা বিশেষ ইমোজি / প্রতীক (UCS-4) প্রতি অক্ষরে ৪ বাইট (৩২ বিট)খুবই রেয়ার বা জটিল কোনো প্রতীক বা বড় ইমোজি ব্যবহার করলে প্রতি অক্ষরের জন্য ৪ বাইট করে জায়গা লাগবে।

কোনো অক্ষর নেই ("")
অক্ষরের সংখ্যা = 0
হিসাব: 49 + (0 * 1) = 49 বাইট।

মেমোরি সাইজ ৪৯ বাইট

শুধু A লিখলেন ("A")

অক্ষরের সংখ্যা = 1
হিসাব: 49 + (1 * 1) = 50 বাইট।
মেমোরি সাইজ  ৫০ বাইট


 নাম লিখা হল ("Mohammad")

এখানে মোট ৮টি অক্ষর আছে (M, o, h, a, m, m, a, d)।অক্ষরের সংখ্যা = 8

হিসাব: 49 + (8 * 1) = 49 + 8 = 57 বাইট।
মেমোরি সাইজ ৫৭ বাইট
বেস হেডার (৪৯ বাইট) হলো পাইথনের নিজের ট্যাক্স বা মেমোরি ফি, যা সে প্রতিটা স্ট্রিং অবজেক্টের জন্য শুরুতেই কেটে নেয়। আর এরপর যতগুলো ল্যাটিন-১ বা ইংরেজি ক্যারেক্টার , 
সেগুলো ওই ৪৯ এর পিঠের ওপর ১ বাইট করে প্লাস বা অ্যাড (Add) হতে থাকে।





String (str) — অক্ষরের ধারাবাহিক মালা:

স্ট্রিং হলো ক্যারেক্টার বা অক্ষরের একটি সিকোয়েন্স। মেমোরিতে এটি Immutable বা অপরিবর্তনশীল— 
এর মানে হলো, একবার একটি স্ট্রিং তৈরি করলে তার ভেতরের কোনো নির্দিষ্ট অক্ষরকে সরাসরি পাল্টে ফেলা যায় না (যেমন: name[0] = "M" করা যাবে না, পুরো স্ট্রিংটাই বদলে ফেলতে হবে)।

ব্যবহার: টেক্সট, নাম বা ঠিকানা জমা রাখতে।

কোড: name = "Abdullah"


সাধারণ টেক্সট এবং ডায়ালগ (Quotes-এর ব্যবহার) স্ট্রিং লেখার জন্য সিঙ্গেল কোট (' ') বা ডাবল কোট (" ") 
দুটোই ব্যবহার করা যাবে। তবে লেখার ভেতরে যদি কোনো কোটেশন থাকে, তখন দুটোর মিশ্রণ ব্যবহার করতে হয়।

dialogue = "He said, 'Python is awesome!'"
print(dialogue)

বহু লাইনের টেক্সট (Multiline String)
যদি কোনো বড় প্যারাগ্রাফ বা কবিতার মতো একাধিক লাইনের টেক্সট একটা ভেরিয়েবলে রাখতে চাওয়া হয় , তখন তিনটি ডাবল কোট (""" """) বা তিনটি সিঙ্গেল কোট (''' ''') ব্যবহার করতে হয়।

address = """গ্রাম: শান্তিনগর,
পোস্ট: রূপগঞ্জ,
জেলা: ঢাকা।"""

print(address)
# আউটপুটে যেভাবে লাইন ভেঙে লেখা হয়েছে, ঠিক সেভাবেই প্রিন্ট হবে।


স্ট্রিং জোড়া দেওয়া (String Concatenation)
অনেক সময় দুটো আলাদা টেক্সট একসাথে জুড়ে দিতে হয়। Python-এ যোগ চিহ্ন (+) ব্যবহার করে খুব সহজেই দুটি স্ট্রিংকে একসাথে জোড়া দেওয়া যায়।

first_name = "Abdullah"
last_name = "Ebny Aziz"

# মাঝখানে একটি স্পেস দিয়ে দুটি স্ট্রিং যোগ করা হলো
full_name = first_name + " " + last_name

print("User Name:", full_name)
# আউটপুট: ব্যবহারকারীর পুরো নাম: Abdullah Ebny Aziz


স্ট্রিং-এর ভেতরে ভেরিয়েবল বসানো (f-String) একটা নাম এবং একটা বয়স আছে। এগুলোকে একটি সুন্দর বাক্যের ভেতর ঢুকিয়ে প্রিন্ট করতে । 
আধুনিক Python-এ এর জন্য সবচেয়ে সহজ উপায় হলো f-string (স্ট্রিং-এর শুরুতে একটি f লিখে ভেতরে {} দিয়ে ভেরিয়েবল বসানো)।

user_name = "Abdullah"
country = "Bangladesh"

# f-string এর জাদু
message = f"Hello, I am {user_name} and I live in {country}."

print(message)
# আউটপুট: Hello, I am Abdullah and I live in Bangladesh.


সংখ্যার মতো দেখতে স্ট্রিং (মনে রাখার মতো বিষয়)
কোডিংয়ে কোনো সংখ্যাকে যদি  কোটেশন ("") চিহ্নের ভেতরে লিখা হয় , Python কিন্তু তখন আর তাকে সংখ্যা বা গণিত করার উপাদান ভাববে না। সেটিকেও একটি স্ট্রিং বা টেক্সট হিসেবে ধরবে।

num1 = "10"  # এটি একটি স্ট্রিং
num2 = "20"  # এটিও একটি স্ট্রিং

result = num1 + num2
print(result) 
# আউটপুট আসবে: 1020 (কারণ সে সংখ্যা দুটিকে যোগ না করে টেক্সটের মতো জোড়া দিয়েছে)


স্ট্রিং মেমোরিতে অক্ষরের মালা হিসেবে থাকে বলে চাইলে এর দৈর্ঘ্য বা কয়টি অক্ষর আছে তা len() ফাংশন দিয়ে সহজেই মেপে দেখা যায়:

text = "Python"
print(len(text)) # আউটপুট আসবে: 6  ------------------- Python-এ অফিশিয়ালি কমেন্ট বা মন্তব্য লেখার একমাত্র প্রতীক হলো হ্যাশ চিহ্ন (#)।




str-এর গুরুত্বপূর্ণ বৈশিষ্ট্য

ইমিউটেবল	        পরিবর্তন করা যায় না (নতুন স্ট্রিং তৈরি হয়)
ইন্ডেক্সিং	          ০ থেকে শুরু (ঋণাত্মক ইন্ডেক্সও কাজ করে)
স্লাইসিং	          অংশবিশেষ বের করা যায় ([start:end:step])
কনকাটেনেশন	      + দিয়ে জোড়া লাগানো যায়
রিপিটেশন	        * দিয়ে পুনরাবৃত্তি করা যায়
লেন্থ	              len() দিয়ে দৈর্ঘ্য বের করা যায়
ইটারেবল	          লুপ চালানো যায়


str-এর বেসিক অপারেশন

text = "Hello Python"

# ১. লেন্থ (দৈর্ঘ্য)
print(len(text))  # ১২

# ২. ইন্ডেক্সিং (০ থেকে শুরু)
print(text[0])    # 'H'
print(text[-1])   # 'n' (শেষের অক্ষর)

# ৩. স্লাইসিং (অংশবিশেষ)
print(text[0:5])  # 'Hello'
print(text[6:])   # 'Python'
print(text[::-1]) # 'nohtyP olleH' (উল্টো)

# ৪. কনকাটেনেশন (+)
first = "Hello"
last = "World"
full = first + " " + last  # 'Hello World'

# ৫. রিপিটেশন (*)
print("Hi" * 3)   # 'HiHiHi'

# ৬. মেম্বারশিপ (in / not in)
print('P' in text)   # True
print('X' not in text)  # True


str-এর গুরুত্বপূর্ণ মেথডসমূহ

🔹 A. কেস কনভার্শন

text = "Hello Python"

print(text.upper())      # 'HELLO PYTHON'
print(text.lower())      # 'hello python'
print(text.capitalize()) # 'Hello python'
print(text.title())      # 'Hello Python'
print(text.swapcase())   # 'hELLO pYTHON'


🔹 B. চেক করা (বুলিয়ান)

text = "Hello123"

print(text.isalpha())    # False (সংখ্যা আছে)
print(text.isdigit())    # False (অক্ষর আছে)
print(text.isalnum())    # True (অক্ষর+সংখ্যা)
print(text.isupper())    # False
print(text.islower())    # False
print(text.isspace())    # False


🔹 C. খোঁজা ও রিপ্লেস করা

text = "Hello World, Hello Python"

print(text.find("World"))    # ৬ (ইন্ডেক্স)
print(text.find("Java"))     # -১ (পায়নি)
print(text.index("World"))   # ৬ (পায়নি হলে Error)
print(text.count("Hello"))   # ২
print(text.replace("Hello", "Hi"))  # 'Hi World, Hi Python'



🔹 D. স্প্লিট ও জয়েন

text = "apple,banana,cherry"

# স্প্লিট (লিস্ট বানায়)
fruits = text.split(",")  # ['apple', 'banana', 'cherry']
print(fruits)

# জয়েন (স্ট্রিং বানায়)
new_text = "-".join(fruits)  # 'apple-banana-cherry'
print(new_text)

# স্প্লিট (সাদা স্পেস দিয়ে)
words = "Hello Python World".split()  # ['Hello', 'Python', 'World']



🔹 E. স্ট্রিপ (ফাঁকা জায়গা বাদ)

text = "  Hello World  "
print(text.strip())   # 'Hello World' (দুই পাশ থেকে)
print(text.lstrip())  # 'Hello World  ' (বাম পাশ থেকে)
print(text.rstrip())  # '  Hello World' (ডান পাশ থেকে)



🔹 F. ফরম্যাটিং (f-string)

name = "Rahim"
age = 25
score = 85.5

# f-string (সবচেয়ে ভালো)
print(f"Name: {name}, Age: {age}, Score: {score}")

# .format() মেথড
print("Name: {}, Age: {}, Score: {}".format(name, age, score))

# % ফরম্যাটিং (পুরনো)
print("Name: %s, Age: %d, Score: %.2f" % (name, age, score))



str-এর গুরুত্বপূর্ণ টিপস

f-string ব্যবহার      	f"Name: {name}"
মাল্টিলাইন স্ট্রিং	        """...""" বা '''...'''
এস্কেপ ক্যারেক্টার	      \n (নিউলাইন), \t (ট্যাব)
Raw স্ট্রিং	              r"C:\Users\Rahim" (ব্যাকস্ল্যাশ এড়াতে)
স্ট্রিং ইন্টারপোলেশন	    f-string সবচেয়ে ভালো 





📝 দ্রুত নোট (সংক্ষেপে):


# str ডেটা টাইপ

✅ ব্যবহার:
- নাম, ইমেইল, বিবরণ
- API রিকোয়েস্ট/রেসপন্স
- ডেটাবেস টেক্সট ফিল্ড
- কনফিগারেশন

✅ গুরুত্বপূর্ণ মেথড:
upper(), lower(), strip(), split(), join()
replace(), find(), count(), len()

✅ মনে রাখবেন:
- ইমিউটেবল (পরিবর্তন করা যায় না)
- ফরম্যাটিংয়ে f-string ব্যবহার করুন
- ইউনিকোড (বাংলা) সাপোর্ট করে
- None চেক করতে ভুলবেন না


১.	str দিয়ে বেসিক অপারেশন করুন (ইন্ডেক্সিং, স্লাইসিং)
২.	upper(), lower(), strip() ব্যবহার 
৩.	split() ও join() দিয়ে ডেটা প্রসেস 
৪.	f-string দিয়ে ডায়নামিক রেসপন্স 
৫.	FastAPI-তে str প্যারামিটার ও রিকোয়েস্ট বডি ব্যবহার 
৬.	বাংলা স্ট্রিং নিয়ে কাজ 


স্ট্রিং ইনডেক্সিং (Indexing) এবং স্লাইসিং (Slicing)
স্ট্রিংয়ের ভেতরের প্রতিটি অক্ষর বা ক্যারেক্টারের একটি নির্দিষ্ট নম্বর বা পজিশন থাকে, একে Index বলে। পাইথনে ইনডেক্স শুরু হয় 0 থেকে।

text = "PYTHON"
# ইনডেক্স:  P=0, Y=1, T=2, H=3, O=4, N=5
# উল্টো দিক: N=-1, O=-2, H=-3 ... (একে নেগেটিভ ইনডেক্স বলে)

print(text[0])   # আউটপুট আসবে: P
print(text[-1])  # আউটপুট আসবে শেষের অক্ষর: N


স্ট্রিং কেটে টুকরো করা (Slicing)
যদি পুরো স্ট্রিং থেকে নির্দিষ্ট একটা অংশ কেটে নিতে চাওয়া হয়, তবে [start:stop] নিয়ম ব্যবহার করা যাবে (মনে রাখতে হবে, stop ইনডেক্সের আগের ঘর পর্যন্ত কাটা হবে):

text = "Hello World"
# ০ থেকে শুরু করে ৫ নম্বর ইনডেক্সের ঠিক আগের (৪ নম্বর) পর্যন্ত কাটবে
print(text[0:5])  # আউটপুট আসবে: Hello






স্ট্রিং পরিবর্তন করা যায় না (Immutable)

পাইথনে স্ট্রিং হলো Immutable। এর মানে হলো, একবার একটি স্ট্রিং তৈরি করলে তার ভেতরের কোনো নির্দিষ্ট অক্ষর আপনি সরাসরি বদলে দিতে পারবেন না।

word = "Cat"
# আপনি যদি চান 'C' বদলে 'B' করে "Bat" বানাবেন:
# word[0] = "B"  --> এটি করলে পাইথনে Error আসবে!



স্ট্রিংয়ের কিছু প্রয়োজনীয় মেথড (String Methods)

msg = "  hello python  "

print(msg.upper())     # সব বড় হাতের হবে -> "  HELLO PYTHON  "
print(msg.title())     # প্রতি শব্দের প্রথম অক্ষর বড় হাতের হবে -> "  Hello Python  "
print(msg.strip())     # শুরুর এবং শেষের সব ফালতু স্পেস কেটে দেবে -> "hello python"
print(msg.replace("hello", "hi")) # শব্দ বদলে দেবে -> "  hi python  "

# স্ট্রিংয়ে মোট কয়টি ক্যারেক্টার আছে তা জানতে len() ব্যবহার করা হয়
print(len("Dhaka"))    # আউটপুট আসবে: 5


স্লাইসিং (Slicing)

text = "Programming"

print(text[0:6])    # Progra   (0 থেকে 5 পর্যন্ত, 6 বাদ)
print(text[:4])     # Prog     (শুরু থেকে 4 পর্যন্ত)
print(text[4:])     # ramming  (4 থেকে শেষ পর্যন্ত)
print(text[::-1])   # gnimmargorP  (পুরো স্ট্রিং উল্টে যাবে)
print(text[::2])    # Pormig   (প্রতি 2 ধাপে একটা করে)




গুরুত্বপূর্ণ স্ট্রিং মেথডসমূহ

text = "  Python Programming  "

print(text.upper())        # Python কে বড় হাতের করে: "  PYTHON PROGRAMMING  "
print(text.lower())        # ছোট হাতের করে
print(text.strip())        # দুই পাশের স্পেস বাদ দেয়: "Python Programming"
print(text.replace("Python", "Java"))  # "  Java Programming  "
print(text.split())        # স্পেস দিয়ে ভেঙে লিস্ট বানায়: ['Python', 'Programming']
print(len(text))           # স্ট্রিং-এর মোট ক্যারেক্টার সংখ্যা

s = "hello"
print(s.startswith("he"))  # True
print(s.endswith("lo"))    # True
print(s.find("ll"))        # 2 (ইনডেক্স পজিশন রিটার্ন করে)
print(s.count("l"))        # 2 (কতবার আছে গোনে)
print(s.capitalize())      # Hello
print(s.title())           # Hello (প্রতিটা শব্দের প্রথম অক্ষর বড়)




স্ট্রিং চেক করার মেথড (is-মেথডগুলো)

print("123".isdigit())     # True — সব সংখ্যা কিনা
print("abc".isalpha())     # True — সব অক্ষর কিনা
print("abc123".isalnum())  # True — অক্ষর+সংখ্যা কিনা
print("   ".isspace())     # True — শুধু স্পেস কিনা
print("Hello".islower())   # False
print("HELLO".isupper())   # True




স্ট্রিং ফরম্যাটিং (String Formatting)

পদ্ধতি ১: f-string (সবচেয়ে জনপ্রিয় ও আধুনিক)

name = "Arman"
age = 25
print(f"My name is {name} and I am {age} years old.")


পদ্ধতি ২: .format() মেথড

print("My name is {} and I am {} years old.".format(name, age))


Escape Characters

স্ট্রিং-এর ভেতরে বিশেষ ক্যারেক্টার ব্যবহার করতে \ (backslash) ব্যবহার হয়:

print("He said, \"I love Python\"")   # কোট এর ভেতরে কোট
print("Line1\nLine2")                  # \n = নতুন লাইন
print("Tab\tSpace")                    # \t = ট্যাব স্পেস
print("This is a backslash: \\")       # \\ = একটা backslash



স্ট্রিং জয়েন ও স্প্লিট

# Split: স্ট্রিং কে লিস্টে ভাঙা
sentence = "I love Python programming"
words = sentence.split()
print(words)   # ['I', 'love', 'Python', 'programming']

# Join: লিস্ট থেকে আবার স্ট্রিং বানানো
joined = "-".join(words)
print(joined)  # I-love-Python-programming




স্ট্রিং-এ লুপ চালানো (Iteration)

for char in "Hi!":
    print(char)
# আউটপুট:
# H
# i
# !



in অপারেটর দিয়ে চেক করা

text = "Python is powerful"
print("Python" in text)      # True
print("Java" in text)        # False
print("Java" not in text)    # True
