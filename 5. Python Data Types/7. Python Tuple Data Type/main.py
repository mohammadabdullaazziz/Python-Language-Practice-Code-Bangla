Tuple কী?

Tuple হলো List এর মতোই একটা ডেটা টাইপ যেটা দিয়ে একাধিক জিনিস একসাথে, ক্রমানুসারে (ordered) রাখা যায়। 
কিন্তু List আর Tuple এর মধ্যে সবচেয়ে বড় পার্থক্য হলো — Tuple তৈরি হওয়ার পর এর ভিতরের মান পরিবর্তন করা যায় না। 
একে বলে immutable (অপরিবর্তনযোগ্য)। যেহেতু এটি পরিবর্তন করা যায় না, তাই এটি লিস্টের চেয়ে দ্রুত কাজ করে এবং মেমোরি কম নেয়। 



Tuple তৈরি করার নিয়ম
Tuple লেখা হয় round bracket ( ) দিয়ে, প্রতিটা item কমা (,) দিয়ে আলাদা করা হয়।

fruits = ("apple", "banana", "mango")
print(fruits)  # ('apple', 'banana', 'mango')


empty_tuple = ()                          # খালি tuple
numbers = (1, 2, 3, 4, 5)                 # সংখ্যার tuple
names = ("Rahim", "Karim", "Salma")       # string এর tuple
mixed = (1, "hello", 3.14, True)          # বিভিন্ন টাইপ একসাথে






⚠️ একটা খুব গুরুত্বপূর্ণ জিনিস — একটা মাত্র item এর Tuple

single = (5)
print(type(single))  # <class 'int'>  -> এটা tuple না, শুধু একটা number!

single_tuple = (5,)   # শেষে কমা (,) দিতেই হবে
print(type(single_tuple))  # <class 'tuple'>


# ভুল পদ্ধতি (এটি টিউপল নয়, সাধারণ ইন্টিজার)
not_a_tuple = (5)

# সঠিক পদ্ধতি (এটি টিউপল)
is_a_tuple = (5,)

কারণ: পাইথন ( ) কে সাধারণত গাণিতিক bracket হিসেবেও ব্যবহার করে (যেমন (2 + 3)), 
তাই একটা মাত্র item দিয়ে tuple বানাতে চাইলে শেষে কমা না দিলে পাইথন এটাকে tuple হিসেবে ধরে না। 
কমা না দিলে পাইথন সেটাকে সাধারণ ব্র্যাকেট বা স্ট্রিং হিসেবে ধরে নেবে।
এটা একটা খুবই কমন ভুল (common mistake)।





Bracket ছাড়াই Tuple তৈরি (Tuple Packing)

my_tuple = 1, 2, 3
print(my_tuple)        # (1, 2, 3)
print(type(my_tuple))  # <class 'tuple'>

পাইথন কমা দেখলেই বুঝে নেয় এটা tuple, bracket না থাকলেও।

# সাধারণ টিউপল
my_tuple = ("apple", "banana", "cherry")
print(my_tuple)

# ব্র্যাকেট ছাড়াও টিউপল তৈরি করা যায় (Comma দিয়ে আলাদা করলেই পাইথন সেটি টিউপল ধরে নেয়)
another_tuple = 10, 20, 30
print(another_tuple)




Index দিয়ে Tuple এর item Access করা
Tuple এও List এর মতোই index (0 থেকে শুরু) দিয়ে item access করা যায়।


fruits = ("apple", "banana", "mango", "orange")
#            0         1         2         3

print(fruits[0])   # apple
print(fruits[2])   # mango


numbers = (10, 20, 30, 40, 50)

# ইনডেক্স দিয়ে উপাদান বের করা
print(numbers[0])   # আউটপুট: 10
print(numbers[-1])  # আউটপুট: 50 (শেষের উপাদান)

# স্লাইসিং (নির্দিষ্ট অংশ কেটে নেওয়া)
print(numbers[1:4]) # আউটপুট: (20, 30, 40)


Negative Index

fruits = ("apple", "banana", "mango", "orange")

print(fruits[-1])   # orange (শেষ item)
print(fruits[-2])   # mango  (শেষ থেকে দ্বিতীয়)




Slicing (Tuple এর একটা অংশ বের করা)

Tuple এও List এর মতোই slicing কাজ করে — একদম একই নিয়ম (start inclusive, stop exclusive)।


numbers = (10, 20, 30, 40, 50, 60)

print(numbers[1:4])    # (20, 30, 40)
print(numbers[:3])     # (10, 20, 30)
print(numbers[3:])     # (40, 50, 60)
print(numbers[::2])    # (10, 30, 50)
print(numbers[::-1])   # (60, 50, 40, 30, 20, 10)



Tuple এর দৈর্ঘ্য বের করা

fruits = ("apple", "banana", "mango")
print(len(fruits))  # 3






🔒 Immutable — Tuple পরিবর্তন করা যায় না (মূল বৈশিষ্ট্য)
যদি টিউপলের কোনো উপাদান বদলাতে চাওয়া হয়, তবে পাইথন এরর (TypeError) দেবে:

t = (1, 2, 3)
# t[0] = 100  # এটি লিখলে Error আসবে, কারণ টিউপল পরিবর্তন করা যায় না!


fruits = ("apple", "banana", "mango")
fruits[1] = "grape"

এখানে error আসবে, কারণ Tuple এর ভিতরের কোনো item সরাসরি পরিবর্তন করা যায় না। 
এটাই Tuple আর List এর সবচেয়ে বড় পার্থক্য।

append(), remove(), insert(), pop(), sort(), reverse(), clear() — এই কোনো মেথডই Tuple এ কাজ করে না, 
কারণ এগুলো সবই List কে পরিবর্তন করার জন্য বানানো, আর Tuple পরিবর্তন করা যায়ই না।


তাহলে উপায় কী?

যদি টিউপল পরিবর্তন করতেই হয়, তবে সেটিকে আগে list() ফাংশন দিয়ে লিস্টে রূপান্তর করে নিতে হবে, 
পরিবর্তন করার পর আবার tuple() ফাংশনে ফিরিয়ে নিতে হবে:

t = (1, 2, 3)
temp_list = list(t)  # লিস্টে রূপান্তর
temp_list[0] = 100   # পরিবর্তন করা হলো
t = tuple(temp_list) # আবার টিউপলে রূপান্তর

print(t)  # আউটপুট: (100, 2, 3)

নামের লিস্ট বা টিউপল থেকে কোনো নাম বদলানো

friends = ("Rahim", "Karim", "Jabbar")

# ১. টিউপলকে লিস্টে রূপান্তর
temp = list(friends)

# ২. ইনডেক্স ১ (দ্বিতীয় নাম) পরিবর্তন করা
temp[1] = "Barkat"

# ৩. লিস্টকে আবার টিউপলে ফিরিয়ে আনা
friends = tuple(temp)

print(friends)  # আউটপুট: ('Rahim', 'Barkat', 'Jabbar')

টিউপলের শেষ বা মাঝখান থেকে কোনো উপাদান মুছে ফেলা (remove বা pop ব্যবহার করে)
ধরা যাক, নিজের কাছে কিছু পণ্যের দামের একটি টিউপল আছে, যেখান থেকে একটি ভুল দাম বাদ দিতে চাইলে।

prices = (100, 250, 500, 300)

# ১. টিউপলকে লিস্টে রূপান্তর
temp = list(prices)

# ২. লিস্টের মেথড ব্যবহার করে ৫৫০ বা নির্দিষ্ট মান বাদ দেওয়া (এখানে ইনডেক্স ২ মানে 500 বাদ দিচ্ছি)
temp.pop(2) 

# ৩. আবার টিউপলে রূপান্তর
prices = tuple(temp)

print(prices)  # আউটপুট: (100, 250, 300)



টিউপলে নতুন কোনো উপাদান যোগ করা (append)

টিউপলে সরাসরি .append() কাজ করে না। তাই এই উপায়ে নতুন উপাদান যুক্ত করা যায়:

colors = ("red", "green")

# ১. লিস্টে রূপান্তর
temp = list(colors)

# ২. নতুন রঙ যোগ করা
temp.append("blue")

# ৩. আবার টিউপলে রূপান্তর
colors = tuple(temp)

print(colors)  # আউটপুট: ('red', 'green', 'blue')


টিউপলের কোনো উপাদান ডুপ্লিকেট বা বাদ দেওয়া (remove ব্যবহার করে)
cart = ("Laptop", "Mouse", "Keyboard", "Mouse")

# ১. লিস্টে রূপান্তর
temp = list(cart)

# ২. 'Mouse' নামের উপাদানটি লিস্ট থেকে মুছে ফেলা
temp.remove("Mouse")

# ৩. আবার টিউপলে রূপান্তর
cart = tuple(temp)

print(cart)  # আউটপুট: ('Laptop', 'Keyboard', 'Mouse') 
# (প্রথমে যে মাউসটি পেয়েছিল, সেটি রিমুভ হয়ে গেছে)


টিউপলের মাঝখানে নতুন কোনো উপাদান ঢুকিয়ে দেওয়া (insert ব্যবহার করে)
যদি লিস্টের শেষে নয়, বরং একদম মাঝখানে কোনো নির্দিষ্ট ইনডেক্সে নতুন ডেটা যুক্ত করতে 

levels = ("Easy", "Hard")

# ১. লিস্টে রূপান্তর
temp = list(levels)

# ২. ইনডেক্স ১ এ (মাঝখানে) "Medium" বসানো
temp.insert(1, "Medium")

# ৩. আবার টিউপলে রূপান্তর
levels = tuple(temp)

print(levels)  # আউটপুট: ('Easy', 'Medium', 'Hard')

টিউপলের সব মান একসাথে পরিবর্তন বা আপডেট করা (লুপ চালিয়ে)

scores = (50, 70, 90)

# ১. লিস্টে রূপান্তর
temp = list(scores)

# ২. লুপ চালিয়ে প্রতিটির সাথে ১০ যোগ করা
for i in range(len(temp)):
    temp[i] += 10

# ৩. আবার টিউপলে রূপান্তর
scores = tuple(temp)

print(scores)  # আউটপুট: (60, 80, 100)



# সপ্তাহের দিনগুলো ফিক্সড থাকে, তাই টিউপল ব্যবহার করা হয়

days_of_week = ("Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday")

print("ছুটির দিন:", days_of_week[1])  # আউটপুট: Sunday

# days_of_week[1] = "Holiday"  # এটা করলে Error আসবে, কারণ টিউপল বদলানো যায় না!


টিউপলকে লিস্ট বানিয়ে এডিট করে আবার টিউপল বানানো 

# বর্তমান টিউপল
prices = (100, 200, 300)

# ১. লিস্টে রূপান্তর
temp = list(prices)

# ২. মান পরিবর্তন বা নতুন মান যোগ করা
temp[0] = 150       # প্রথম মান পরিবর্তন
temp.append(400)    # নতুন মান যোগ

# ৩. আবার টিউপলে রূপান্তর
prices = tuple(temp)

print(prices)  # আউটপুট: (150, 200, 300, 400)


টিউপল আনপাকিং (Tuple Unpacking) - সবচেয়ে বেশি ব্যবহৃত

একটি টিউপলের ভেতরে থাকা মানগুলোকে আলাদা আলাদা ভ্যারিয়েবলে খুব সহজে অ্যাসাইন করে ফেলা। এটি ফাংশন থেকে একাধিক মান রিটার্ন নেওয়ার সময় সবচেয়ে বেশি ব্যবহার করা হয়।

# একটি ইউজারের ইনফরমেশন টিউপল আকারে আছে
user_info = ("Rahim", 25, "Dhaka")

# এক লাইনে আলাদা আলাদা ভ্যারিয়েবলে রেখে দেওয়া
name, age, city = user_info

print(name)  # আউটপুট: Rahim
print(age)   # আউটপুট: 25
print(city)  # আউটপুট: Dhaka





টিউপলের মেথডসমূহ (Methods)
লিস্টের মতো টিউপলে অনেকগুলো মেথড থাকে না, কারণ এটি ইমিউটেবল। টিউপলে মাত্র দুটি বিল্ট-ইন মেথড আছে:

১. count(): নির্দিষ্ট কোনো উপাদান টিউপলে কতবার আছে তা গুণে দেয়।

t = (1, 2, 3, 2, 4, 2)
print(t.count(2))  # আউটপুট: 3 (কারণ ২ আছে তিনবার)

২. index(): নির্দিষ্ট উপাদানটি কত নম্বর ইনডেক্সে আছে তা খুঁজে বের করে।

t = ("apple", "banana", "mango")
print(t.index("banana"))  # আউটপুট: 1



numbers = (10, 20, 30, 20, 40, 20)

print(numbers.count(20))    # 3   -> কতবার 20 আছে গোনে
print(numbers.index(30))    # 2   -> 30 এর index খুঁজে দেয়







টিউপলের সাথে বিল্ট-ইন ফাংশন

লিস্টের মতো টিউপলেও বিভিন্ন বিল্ট-ইন ফাংশন ব্যবহার করা যায়:

len(t) -> টিউপলের দৈর্ঘ্য বের করতে।

max(t) -> সবচেয়ে বড় মান বের করতে।

min(t) -> সবচেয়ে ছোট মান বের করতে।

sum(t) -> সব সংখ্যার যোগফল বের করতে।

in / not in -> কোনো উপাদান টিউপলে আছে কি না চেক করতে ("apple" in my_tuple)।

১. len(t) - টিউপলের দৈর্ঘ্য বা উপাদান সংখ্যা বের করতে 

এটি দিয়ে টিউপলে মোট কয়টি উপাদান আছে তা গণনা করা যায়।

numbers = (10, 20, 30, 40, 50)

print(len(numbers))  # আউটপুট: 5 (কারণ এখানে মোট ৫টি সংখ্যা আছে)


২. max(t) - সবচেয়ে বড় মান বের করতে
টিউপলের ভেতরের সংখ্যাগুলোর মধ্যে সবচেয়ে বড় সংখ্যাটি খুঁজে বের করতে এটি ব্যবহার করা হয়।

scores = (45, 89, 12, 99, 67)

print(max(scores))  # আউটপুট: 99 (সবচেয়ে বড় সংখ্যা)


৩. min(t) - সবচেয়ে ছোট মান বের করতে
টিউপলের ভেতরের সংখ্যাগুলোর মধ্যে সবচেয়ে ছোট সংখ্যাটি বের করার জন্য এটি ব্যবহৃত হয়।

temperatures = (32, 28, 19, 41, 22)

print(min(temperatures))  # আউটপুট: 19 (সবচেয়ে ছোট সংখ্যা)


৪. sum(t) - সব সংখ্যার যোগফল বের করতে
টিউপলের সব সংখ্যাগুলোকে একত্রে যোগ করতে এই ফাংশনটি ব্যবহার করা হয়।

prices = (150, 200, 50, 100)

print(sum(prices))  # আউটপুট: 500 (১৫০+২০০+৫০+১০০)


৫. in - কোনো উপাদান টিউপলে আছে কি না চেক করতে
নির্দিষ্ট কোনো মান টিউপলের ভেতরে উপস্থিত আছে কি না তা যাচাই করে (True অথবা False রিটার্ন করে)।

fruits = ("apple", "banana", "mango")

print("banana" in fruits)  # আউটপুট: True (কারণ ব্যানানা লিস্টে আছে)
print("orange" in fruits)  # আউটপুট: False (কারণ অরেঞ্জ নেই)



৬. not in - কোনো উপাদান টিউপলে নেই কি না চেক করতে

নির্দিষ্ট মানটি টিউপলে অনুপস্থিত কি না তা যাচাই করে। মানটি না থাকলে True এবং থাকলে False দেয়।

colors = ("red", "green", "blue")

print("yellow" not in colors)  # আউটপুট: True (কারণ হলুদ সত্যিই নেই)
print("red" not in colors)     # আউটপুট: False (কারণ লাল তো আছে!)





Tuple কেন ব্যবহার করা হয় — List থাকতে Tuple কেন লাগবে?

ক) ডেটা সুরক্ষিত (Protected) রাখতে

যখন চাওয়া হয় যে ডেটা ভুলবশতও যাতে কেউ পরিবর্তন করতে না পারে (যেমন কোনো fixed configuration বা constant value),তখন Tuple ব্যবহার করা হয়।

DAYS_OF_WEEK = ("Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday")

print(DAYS_OF_WEEK)
print(DAYS_OF_WEEK[0])      # প্রথম দিন
print(DAYS_OF_WEEK[-1])     # শেষ দিন
print(len(DAYS_OF_WEEK))    # মোট কতটা দিন

('Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday')
Saturday
Friday
7
এখানে সপ্তাহের দিন কখনো পরিবর্তন হবে না, তাই এটা Tuple দিয়ে রাখাই যুক্তিসঙ্গত।


for loop দিয়ে সব দিন print করা

DAYS_OF_WEEK = ("Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday")

for day in DAYS_OF_WEEK:
    print(day)

Saturday
Sunday
Monday
Tuesday
Wednesday
Thursday
Friday



Index সহ প্রতিটা দিন দেখানো (enumerate)

DAYS_OF_WEEK = ("Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday")

for index, day in enumerate(DAYS_OF_WEEK):
    print(f"দিন {index + 1}: {day}")

দিন 1: Saturday
দিন 2: Sunday
দিন 3: Monday
দিন 4: Tuesday
দিন 5: Wednesday
দিন 6: Thursday
দিন 7: Friday

পরিবর্তন করার চেষ্টা করলে error দেখা (Tuple এর immutable property প্রমাণ)
DAYS_OF_WEEK[0] = "Funday"   TypeError: 'tuple' object does not support item assignment



enumerate() কী?
enumerate() হলো একটা built-in ফাংশন যেটা কোনো list/tuple এর প্রতিটা item এর সাথে একটা index (গণনা নম্বর) জুড়ে দেয়। 
সাধারণত for loop এ যখন শুধু item না, item এর সাথে তার অবস্থান (position/index) ও দরকার হয়,তখন enumerate() ব্যবহার করা হয়।

আগে সাধারণ ধারণা দেখি (enumerate ছাড়া কী সমস্যা হতো)

DAYS_OF_WEEK = ("Saturday", "Sunday", "Monday")

for day in DAYS_OF_WEEK:
    print(day)

এখানে শুধু day (মান) পাওয়া যাচ্ছে, কিন্তু এটা কততম দিন (index) সেটা জানার উপায় নেই।
এই সমস্যা সমাধান করে enumerate()।

পুরো কোডটা লাইন বাই লাইন

DAYS_OF_WEEK = ("Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday")

for index, day in enumerate(DAYS_OF_WEEK):
    print(f"দিন {index + 1}: {day}")

📝 লাইন বাই লাইন এবং প্রতিটি শব্দের ব্যাখ্যা:

১. DAYS_OF_WEEK = (...)

এখানে একটি টিউপল (tuple) তৈরি করা হয়েছে যার নাম রাখা হয়েছে DAYS_OF_WEEK।

এর ভেতরে সপ্তাহের ৭টি দিনের নাম ক্রমানুসারে স্ট্রিং (string) আকারে রাখা আছে।

পাইথনে এই ৭টি উপাদানের নিজস্ব ইনডেক্স বা পজিশন নম্বর আছে, যা শুরু হয় 0 থেকে এবং শেষ হয় 6 এ গিয়ে
(যেমন: "Saturday" এর ইনডেক্স 0, "Sunday" এর ইনডেক্স 1... এভাবে "Friday" এর ইনডেক্স 6)।


২. for index, day in enumerate(DAYS_OF_WEEK):

এখানে ৩টি গুরুত্বপূর্ণ বিষয় একসাথে কাজ করছে:

enumerate(DAYS_OF_WEEK): এটি এই কোডের সবচেয়ে গুরুত্বপূর্ণ অংশ। enumerate ফাংশনটি 

টিউপলের প্রতিটি উপাদানের সাথে পর্দার আড়ালে একটি করে ক্রমিক নম্বর বা ইনডেক্স জোড়া লাগিয়ে দেয়। অর্থাৎ, এটি শুধু দিনের নামগুলোই আনে না, সাথে তাদের পজিশন নম্বরটাও সাথে করে নিয়ে আসে।

index ভ্যারিয়েবল: enumerate থেকে প্রতিবার লুপ ঘোরার সময় যে ইনডেক্স নম্বরটি (0, 1, 2...) আসে, 
সেটি জমা হয় এই index নামের ভ্যারিয়েবলে।

day ভ্যারিয়েবল: enumerate থেকে প্রতিবার লুপ ঘোরার সময় টিউপল থেকে যে দিনের নামটি ("Saturday", "Sunday"...) আসে, 
সেটি জমা হয় এই day নামের ভ্যারিয়েবলে।

for ... in ...: এটি একটি লুপ, যা টিউপলের প্রথম দিন থেকে শুরু করে একে একে ৭ বার ঘুরবে।


৩. print(f"দিন {index + 1}: {day}")

f"..." (f-string): পাইথনের একটি আধুনিক পদ্ধতি, যার মাধ্যমে লেখার ভেতরে সেকেন্ড ব্র্যাকেট {} দিয়ে খুব সহজে
কোনো ভ্যারিয়েবলের মান বসিয়ে দেওয়া যায়।

index + 1 কেন দেওয়া হলো?

আমরা জানি পাইথনে ইনডেক্স শুরু হয় 0 থেকে। তাই প্রথম লুপে index-এর মান থাকবে 0।

কিন্তু আমরা তো আর "দিন ০" দেখতে চাই না, চাই "দিন ১"। তাই কম্পিউটারের 0-এর সাথে 1 যোগ করে 0 + 1 = 1 বানানো হয়েছে (২য় লুপে হবে 1 + 1 = 2, এভাবে শেষ পর্যন্ত চলবে)।

day: এটি বর্তমান লুপে থাকা দিনের আসল নামটি ("Saturday", "Sunday" ইত্যাদি) প্রিন্ট করবে।


🔄 ড্রাই রান (Dry Run) বা সিরিয়াল এক্সিকিউশন (৭ বারের লুপ ঘোরা):

১ম বার লুপ ঘোরার সময়:

index = 0, day = "Saturday"

প্রিন্টের হিসাব: index + 1 অর্থাৎ 0 + 1 = 1, আর day = "Saturday"

স্ক্রিনে প্রিন্ট হবে: দিন 1: Saturday

২য় বার লুপ ঘোরার সময়:

index = 1, day = "Sunday"

প্রিন্টের হিসাব: 1 + 1 = 2, আর day = "Sunday"

স্ক্রিনে প্রিন্ট হবে: দিন 2: Sunday

৩য় বার লুপ ঘোরার সময়:

index = 2, day = "Monday"

প্রিন্টের হিসাব: 2 + 1 = 3, আর day = "Monday"

স্ক্রিনে প্রিন্ট হবে: দিন 3: Monday

৪র্থ বার লুপ ঘোরার সময়:

index = 3, day = "Tuesday"

প্রিন্টের হিসাব: 3 + 1 = 4, আর day = "Tuesday"

স্ক্রিনে প্রিন্ট হবে: দিন 4: Tuesday

৫ম বার লুপ ঘোরার সময়:

index = 4, day = "Wednesday"

প্রিন্টের হিসাব: 4 + 1 = 5, আর day = "Wednesday"

স্ক্রিনে প্রিন্ট হবে: দিন 5: Wednesday

৬ষ্ঠ বার লুপ ঘোরার সময়:

index = 5, day = "Thursday"

প্রিন্টের হিসাব: 5 + 1 = 6, আর day = "Thursday"

স্ক্রিনে প্রিন্ট হবে: দিন 6: Thursday

৭ম বার লুপ ঘোরার সময় (শেষবার):

index = 6, day = "Friday"

প্রিন্টের হিসাব: 6 + 1 = 7, আর day = "Friday"

স্ক্রিনে প্রিন্ট হবে: দিন 7: Friday

দিন 1: Saturday
দিন 2: Sunday
দিন 3: Monday
দিন 4: Tuesday
দিন 5: Wednesday
দিন 6: Thursday
দিন 7: Friday


খ) List এর চেয়ে দ্রুত (Performance)

Tuple, List এর চেয়ে memory কম নেয় এবং দ্রুত কাজ করে, কারণ পাইথন জানে এটা পরিবর্তন হবে না, 
তাই এটার জন্য কম অপ্টিমাইজেশন লাগে।

import sys

my_list = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3, 4, 5)

print(sys.getsizeof(my_list))   # বেশি জায়গা নেয়
print(sys.getsizeof(my_tuple))  # কম জায়গা নেয়




Tuple Unpacking (খুবই গুরুত্বপূর্ণ ও বহুল ব্যবহৃত)

Tuple এর একটা দারুণ ফিচার হলো একে সরাসরি আলাদা আলাদা variable এ ভাগ করা যায়:

person = ("Rahim", 25, "Dhaka")

name, age, city = person

print(name)  # Rahim
print(age)   # 25
print(city)  # Dhaka





দুইটা Value একসাথে Swap করা (Tuple Unpacking এর কমন ব্যবহার)

a = 5
b = 10

a, b = b, a   # ভিতরে ভিতরে এটা tuple unpacking দিয়েই কাজ করে

print(a)  # 10
print(b)  # 5

এখানে কোনো তৃতীয় variable ছাড়াই দুইটা মান swap করা যাচ্ছে — এটা Tuple এর কারণেই সম্ভব হচ্ছে।




Star (*) দিয়ে বাকি সব একসাথে নেওয়া

numbers = (1, 2, 3, 4, 5)

first, *middle, last = numbers

print(first)   # 1
print(middle)  # [2, 3, 4]  -> এটা list হয়ে যায়
print(last)    # 5





Nested Tuple (Tuple এর ভিতরে Tuple) — Advanced

nested = ((1, 2, 3), (4, 5, 6), (7, 8, 9))

print(nested[0])       # (1, 2, 3)
print(nested[0][1])    # 2
print(nested[2][2])    # 9



Tuple + List একসাথে (Mixed Nesting) — Advanced

student = ("Rahim", [85, 90, 78])   # নাম immutable, কিন্তু marks list mutable

student[1].append(95)
print(student)  # ('Rahim', [85, 90, 78, 95])

⚠️ গুরুত্বপূর্ণ concept: Tuple নিজে immutable, কিন্তু যদি তার ভিতরে একটা list থাকে, তাহলে সেই list-টা পরিবর্তন করা যায় (কারণ list নিজেই mutable)। 
Tuple শুধু নিশ্চিত করে যে তার নিজের item গুলোর reference/অবস্থান পরিবর্তন হবে না — কিন্তু ভিতরের mutable object (list) নিজে পরিবর্তনযোগ্যই থাকে।



Tuple Concatenation ও Repetition

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

combined = tuple1 + tuple2
print(combined)  # (1, 2, 3, 4, 5, 6)

repeated = tuple1 * 3
print(repeated)  # (1, 2, 3, 1, 2, 3, 1, 2, 3)




Named Tuple — Advanced (একটু বেশি structured Tuple)

collections module থেকে namedtuple ব্যবহার করে Tuple এর item গুলোকে নাম দিয়ে access করা যায়, শুধু index দিয়ে না:



from collections import namedtuple

Person = namedtuple("Person", ["name", "age", "city"])

p1 = Person("Rahim", 25, "Dhaka")

print(p1.name)   # Rahim  (index দিয়ে না, নাম দিয়ে access!)
print(p1.age)    # 25
print(p1[0])     # Rahim  (index দিয়েও কাজ করে)

এটা তখন কাজে লাগে যখন Tuple এর প্রতিটা item এর একটা অর্থবহ (meaningful) নাম দিতে চাওয়া হয়, শুধু 0, 1, 2 index দিয়ে মনে রাখার বদলে।
FastAPI/backend কোডে readability বাড়াতে এটা কাজে লাগে।
