লিস্টে নতুন আইটেম যোগ করা বা বাদ দেওয়ার জন্য পাইথনে বেশ কিছু বিল্ট-ইন মেথড রয়েছে:

১. ডেটা যোগ করা (Adding Elements)

append(): লিস্টের একদম শেষে নতুন আইটেম যোগ করে।

insert(): নির্দিষ্ট কোনো পজিশনে বা ইনডেক্সে আইটেম যোগ করে।

extend(): অন্য কোনো লিস্টের উপাদানগুলোকে বর্তমান লিস্টের সাথে যুক্ত করে।




append() মেথড

কাজ: লিস্টের একদম শেষে নতুন একটি উপাদান যোগ করে।

# ছোট ভ্যারিয়েবল 'l' (list বোঝাতে)
l = [10, 20]

# লিস্টের শেষে 30 যোগ করা
l.append(30)

print(l)  
# আউটপুট: [10, 20, 30]






insert() মেথড

কাজ: নির্দিষ্ট পজিশন বা ইনডেক্সে নতুন উপাদান বসায়। এর জন্য দুটি জিনিস দিতে হয়: (index, value)।

l = [10, 30]

# ১ নম্বর ইনডেক্সে গিয়ে '20' বসিয়ে দাও
l.insert(1, 20)

print(l)  
# আউটপুট: [10, 20, 30]  (যেহেতু ১ নম্বর ইনডেক্সে 20 বসে গেছে)



extend() মেথড
কাজ: একটি লিস্টের সাথে আরেকটি পুরো লিস্ট যুক্ত করে বা ছড়িয়ে দেয়।


l1 = [1, 2]
l2 = [3, 4]

# l1 এর সাথে l2 কে এক্সটেন্ড বা যুক্ত করা
l1.extend(l2)

print(l1)  
# আউটপুট: [1, 2, 3, 4]




২. ডেটা মুছে ফেলা (Removing Elements)

remove(): নির্দিষ্ট কোনো উপাদানের নাম ধরে মুছে ফেলে।

pop(): ইনডেক্স ধরে বা ডিফল্টভাবে শেষের উপাদানটি মুছে ফেলে।

del: নির্দিষ্ট ইনডেক্সের উপাদান ডিলিট করে।

clear(): লিস্টের সব উপাদান মুছে খালি করে দেয়।


colors = ["Red", "Green", "Blue", "Yellow"]

colors.remove("Green") # ফল: ['Red', 'Blue', 'Yellow']
colors.pop(0)          # ০ নম্বর ইনডেক্স ডিলিট করবে: ['Blue', 'Yellow']
del colors[1]          # ১ নম্বর ইনডেক্স ডিলিট করবে
colors.clear()         # সম্পূর্ণ লিস্ট খালি হয়ে যাবে: []


colors = ["Red", "Green", "Blue", "Yellow"]
removed_item = colors.pop(0)

print(colors)         # আউটপুট: ['Green', 'Blue', 'Yellow']
print(removed_item)   # আউটপুট: Red (মুছে যাওয়া জিনিসটি আলাদা হয়ে হাতে চলে এল)




৩. খোঁজাখুঁজি ও সাজানো (Searching & Sorting)

sort(): ছোট থেকে বড় বা অ্যালফাবেট অনুযায়ী সাজায়।

reverse(): লিস্ট উল্টে দেয়।

count(): কোনো উপাদান লিস্টে কয়বার আছে গুনে দেয়।

index(): কোনো উপাদানের পজিশন বা ইনডেক্স কত তা বলে দেয়।


nums = [4, 1, 9, 3, 1]

nums.sort()            # ছোট থেকে বড় সাজাবে: [1, 1, 3, 4, 9]
nums.reverse()         # উল্টে দেবে: [9, 4, 3, 1, 1]
print(nums.count(1))   # ১ কয়বার আছে দেখাবে: 2

l = [10, 20, 30, 20]
print(l.index(20))  # আউটপুট: 1 (প্রথম যে ২০ পাবে তার ইনডেক্স দেবে)







ইন্টারমিডিয়েট লেভেল (Intermediate Concepts)



লুপের মাধ্যমে লিস্ট ট্রাভার্স করা
for লুপ ব্যবহার করে খুব সহজেই লিস্টের প্রতিটি আইটেম আলাদাভাবে প্রিন্ট বা প্রসেস করা যায়:

fruits = ["Apple", "Banana", "Mango"]

for fruit in fruits:
    print(fruit)



in অপারেটর ব্যবহার করে চেক করা
কোনো উপাদান লিস্টে আছে কি না তা in দিয়ে চেক করা:

fruits = ["Apple", "Banana", "Mango"]

if "Banana" in fruits:
    print("হ্যাঁ, ব্যানানা আছে!")





লিস্ট কপি করার সমস্যা ও সমাধান (copy() বা സ্লাইসিং)
খুব সাধারণ একটি ভুল হলো list2 = list1 এভাবে লেখা। এভাবে লিখলে একটি পরিবর্তন করলে অন্যটিও বদলে যায়। সঠিক নিয়মে কপি করতে হয়:


original = [1, 2, 3]
copy_list = original.copy()  # অথবা original[:]

print(copy_list)



অ্যাডভান্সড লেভেল (Advanced List Concepts)
লিস্ট কমপ্রিহেনশন (List Comprehension) - খודই শক্তিশালী ফিচার
এক লাইনে লুপ চালিয়ে নতুন লিস্ট তৈরি করার দারুণ এক পদ্ধতি হলো লিস্ট কমপ্রিহেনশন। এটি কোডকে খুব সুন্দর ও ফাস্ট করে।

সাধারণ নিয়ম বনাম লিস্ট কমপ্রিহেনশন:

# সাধারণ নিয়মে ১ থেকে ৫ এর স্কয়ার বের করা:
squares = []
for x in range(1, 6):
    squares.append(x ** 2)

# লিস্ট কমপ্রিহেনশন দিয়ে (এক লাইনে):
squares = [x ** 2 for x in range(1, 6)]
print(squares)  # আউটপুট: [1, 4, 9, 16, 25]


শর্তযুক্ত (Conditional) লিস্ট কমপ্রিহেনশন:

# শুধু জোড় সংখ্যাগুলোর স্কয়ার বের করা:
even_squares = [x ** 2 for x in range(1, 11) if x % 2 == 0]
print(even_squares)  # আউটপুট: [4, 16, 36, 64, 100]




নেস্টেড লিস্ট (Nested List / 2D List)
লিস্টের ভেতরে যখন আরেকটি লিস্ট রাখা হয়, তাকে নেস্টেড বা টু-ডাইমেনশনাল (2D) লিস্ট বলে (ম্যাট্রিক্সের মতো)।

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# নির্দিষ্ট উপাদান এক্সেস করা (যেমন: ৫ নম্বরটি)
print(matrix[1][1])  # আউটপুট: 5 (১ম রো, ১ কলাম)



প্যাকিং এবং আনপ্যাক করা (Packing & Unpacking)
লিস্টের উপাদানগুলোকে আলাদা আলাদা ভ্যারিয়েবলে খুব সহজে অ্যাসাইন করা যায়:

student = ["Abdullah", 30, "Computer Science"]

# আনপ্যাক করা
name, age, department = student

print(name)        # Abdullah
print(age)         # 30





অতিরিক্ত উপাদান একসাথে ধরার জন্য স্টার (*) অপারেটর ব্যবহার করা যায়:

numbers = [1, 2, 3, 4, 5]
first, *middle, last = numbers

print(first)   # 1
print(middle)  # [2, 3, 4] (বাকি মাঝখানের সব)
print(last)    # 5

পাইথনের লিস্ট হলো একটি বহুমুখী হাতিয়ার। বেসিক ইনডেক্সিং থেকে শুরু করে অ্যাডভান্সড List Comprehension পর্যন্ত আয়ত্ত করতে পারলে পাইথনে ডেটা ম্যানিপুলেশন সহজ হয়ে যাবে!



বিল্ট-ইন ফাংশন (যেগুলো লিস্টের সাথে ব্যবহার করা যায়):

len(): লিস্টে মোট কয়টি উপাদান আছে তা বলে। (len(l))

max(): লিস্টের সবচেয়ে বড় সংখ্যাটি বের করে। (max(l))

min(): লিস্টের সবচেয়ে ছোট সংখ্যাটি বের করে। (min(l))

sum(): লিস্টের সব সংখ্যার যোগফল বের করে। (sum(l))


# আমাদের মূল লিস্ট
l = [10, 25, 5, 40, 15]

# ১. len() - লিস্টের মোট উপাদান সংখ্যা বের করা
total_items = len(l)
print(f"Total items: {total_items}")

# ২. max() - সবচেয়ে বড় সংখ্যাটি বের করা
max_value = max(l)
print(f"Maximum value: {max_value}")

# ৩. min() - সবচেয়ে ছোট সংখ্যাটি বের করা
min_value = min(l)
print(f"Minimum value: {min_value}")

# ৪. sum() - সব সংখ্যার যোগফল বের করা
total_sum = sum(l)
print(f"Total sum: {total_sum}")


Total items: 5
Maximum value: 40
Minimum value: 5
Total sum: 95





in এবং not in অপারেটর (চেক করা)

কোনো উপাদান লিস্টে আছে কি না তা খুব সহজে চেক করতে এগুলো ব্যবহার করা হয়। এর আউটপুট সবসময় True বা False আসে।

l = ["apple", "banana", "mango"]

print("banana" in l)     # আউটপুট: True (যেহেতু আছে)
print("orange" not in l) # আউটপুট: True (যেহেতু অরেঞ্জ লিস্টে নেই)



del কিওয়ার্ড (ডিলিট করা)
ইনডেক্স ধরে কোনো নির্দিষ্ট উপাদান বা পুরো লিস্টই মুছে ফেলার জন্য del ব্যবহার করা হয়।

l = [10, 20, 30, 40]

del l[1]      # ১ নম্বর ইনডেক্সের উপাদান (২০) ডিলিট করে দেবে
print(l)      # আউটপুট: [10, 30, 40]

# del l       # পুরো লিস্টটাই মেমোরি থেকে মুছে ফেলে

nums = [10, 20, 30, 40, 50]

del nums[1:3]  # ১ থেকে ৩ নম্বর ইনডেকser আগের পর্যন্ত (অর্থাৎ ২০ এবং ৩০) ডিলিট হয়ে যাবে
print(nums)    # আউটপুট: [10, 40, 50]




লিস্ট জয়েন করা বা যোগ করা (+ অপারেটর)
গাণিতিক প্লাস (+) চিহ্ন দিয়ে দুটি আলাদা লিস্টকে একসাথে যুক্ত করে একটি নতুন লিস্ট বানানো যায়।

l1 = [1, 2]
l2 = [3, 4]

l3 = l1 + l2
print(l3)  # আউটপুট: [1, 2, 3, 4]



লিস্ট মাল্টিপ্লিকেশন (* অপারেটর)
কোনো লিস্টকে কোনো সংখ্যা দিয়ে গুণ করলে লিস্টের উপাদানগুলো ততোবার পুনরাবৃত্তি (repeat) হয়।

l = [5, 10]
result = l * 3

print(result)  # আউটপুট: [5, 10, 5, 10, 5, 10]



sorted() ফাংশন (আসল লিস্ট ঠিক রেখে সাজানো)
আগে আমরা l.sort() দেখেছি, যা আসল লিস্টকে বদলে দেয়। কিন্তু sorted() ফাংশনটি আসল লিস্ট অপরিবর্তিত রেখে নতুন একটি সাজানো লিস্ট রিটার্ন করে।

l = [5, 2, 9, 1]

new_l = sorted(l)

print("আসল লিস্ট:", l)      # আউটপুট: [5, 2, 9, 1] (পরিবর্তন হয়নি)
print("নতুন সাজানো লিস্ট:", new_l)  # আউটপুট: [1, 2, 5, 9]



লিস্ট আনপ্যাক করা (List Unpacking)
লিস্টের ভেতরের উপাদানগুলোকে আলাদা আলাদা ভ্যারিয়েবলে খুব সহজে অ্যাসাইন করে ফেলা যায়।


info = ["Rahim", 25, "Dhaka"]

name, age, city = info

print(name)  # Rahim
print(age)   # 25
print(city)  # Dhaka

আর যদি মাঝখানের অনেকগুলো উপাদান একসাথে ধরতে চান, তবে স্টার (*) ব্যবহার করা যায়:

numbers = [1, 2, 3, 4, 5]
first, *middle, last = numbers

print(first)   # 1
print(middle)  # [2, 3, 4]
print(last)    # 5




লুপের সাথে enumerate() এর ব্যবহার (ইনডেক্সসহ লুপ চালানো)
সাধারণত for লুপ চালালে শুধু উপাদানগুলো পাওয়া যায়, ইনডেক্স পাওয়া যায় না। কিন্তু enumerate() ব্যবহার করলে একসাথেই ইনডেক্স এবং উপাদান উভয়ই পাওয়া যায়:

fruits = ["apple", "banana", "mango"]

for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")

Index 0: apple
Index 1: banana
Index 2: mango




zip() ফাংশন (একাধিক লিস্ট একসাথে মেলানো)
দুটি আলাদা লিস্টকে পাশাপাশি জোড়া লাগাতে zip() ব্যবহার করা হয়:

names = ["Ali", "Babu", "Hasan"]
scores = [85, 90, 95]

# একসাথে লুপ চালিয়ে প্রিন্ট করা
for n, s in zip(names, scores):
    print(f"{n} got {s} marks.")


names = ["Rahim", "Karim", "Salma"]
ages = [25, 30, 22]

for name, age in zip(names, ages):
    print(f"{name}: {age} বছর")








in দিয়ে লিস্টে থাকা চেক করার সময় if-else এর ব্যবহার

colors = ["red", "green", "blue"]

if "green" in colors:
    print("হ্যাঁ, এই রঙটি লিস্টে আছে!")
else:
    print("না, নেই।")





my_list = []

if not my_list:
    print("List খালি")







any() এবং all() ফাংশন লিস্টের সাথে 

any(): লিস্টের অন্তত একটি উপাদানও যদি True হয়, তবে এটি True রিটার্ন করে।

all(): লিস্টের সবকটি উপাদান যদি True হয়, তবেই এটি True রিটার্ন করে।

bool_list = [True, False, True]

print(any(bool_list))  # আউটপুট: True (কারণ অন্তত একটি True আছে)
print(all(bool_list))  # আউটপুট: False (কারণ সবকটি True নয়)



sort() vs sorted() — পার্থক্য 

numbers = [5, 2, 8, 1]

sorted_numbers = sorted(numbers)   # নতুন sorted list রিটার্ন করে, আসলটা পরিবর্তন করে না
print(sorted_numbers)   # [1, 2, 5, 8]
print(numbers)          # [5, 2, 8, 1]  -> অপরিবর্তিত

numbers.sort()          # আসল list কে সরাসরি পরিবর্তন করে
print(numbers)          # [1, 2, 5, 8]





Unpacking (List থেকে সরাসরি Variable এ ভাগ করা)

fruits = ["apple", "banana", "mango"]

a, b, c = fruits
print(a)  # apple
print(b)  # banana
print(c)  # mango



Star (*) দিয়ে বাকি সব একসাথে নেওয়া:

numbers = [1, 2, 3, 4, 5]

first, *middle, last = numbers
print(first)   # 1
print(middle)  # [2, 3, 4]
print(last)    # 5


zeros = [0] * 5
print(zeros)  # [0, 0, 0, 0, 0]




Average বের করা

marks = [85, 90, 78, 92, 88]

average = sum(marks) / len(marks)
print(f"গড় নম্বর: {average}")  # গড় নম্বর: 86.6




কার্ট সিস্টেম (Shopping Cart) - FastAPI backend এ কমন

cart = []

cart.append("Laptop")
cart.append("Mouse")
cart.append("Keyboard")

print(f"কার্টে {len(cart)}টা আইটেম আছে: {cart}")



ছাত্রদের নাম রাখা ও প্রসেস করা

students = ["Rahim", "Karim", "Salma", "Fatema"]

for student in students:
    print(f"স্বাগতম, {student}!")



String আর List এর মধ্যে রূপান্তর

# String কে list এ রূপান্তর করা
text = "hello"
char_list = list(text)
print(char_list)  # ['h', 'e', 'l', 'l', 'o']

# শব্দ ভাগ করা
sentence = "I love Python"
words = sentence.split()
print(words)  # ['I', 'love', 'Python']

# List কে আবার string এ জোড়া লাগানো
joined = " ".join(words)
print(joined)  # I love Python



List যোগ করা (Concatenation) ও পুনরাবৃত্তি (Repetition)

list1 = [1, 2, 3]
list2 = [4, 5, 6]

combined = list1 + list2
print(combined)  # [1, 2, 3, 4, 5, 6]

repeated = list1 * 3
print(repeated)  # [1, 2, 3, 1, 2, 3, 1, 2, 3]



শর্ত (condition) সহ List Comprehension:

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = [n for n in numbers if n % 2 == 0]
print(even_numbers)  # [2, 4, 6, 8, 10]



List Comprehension দিয়ে (এক লাইনে):

numbers = [1, 2, 3, 4, 5]
squares = [n ** 2 for n in numbers]
print(squares)  # [1, 4, 9, 16, 25]






numbers = [1, 2, 3, 4, 5]
squares = []

for n in numbers:
    squares.append(n ** 2)

print(squares)  # [1, 4, 9, 16, 25]


সঠিক copy করার পদ্ধতি:

list1 = [1, 2, 3]
list2 = list1.copy()    # অথবা list1[:]

list2.append(4)
print(list1)   # [1, 2, 3]     -> অপরিবর্তিত
print(list2)   # [1, 2, 3, 4]



List সাজানো (Sorting)

numbers = [5, 2, 8, 1, 9]

numbers.sort()
print(numbers)  # [1, 2, 5, 8, 9]  -> ছোট থেকে বড়

numbers.sort(reverse=True)
print(numbers)  # [9, 8, 5, 2, 1]  -> বড় থেকে ছোট




List খোঁজা ও গোনার মেথড

numbers = [10, 20, 30, 20, 40]

print(numbers.index(20))    # 1  -> প্রথম যেখানে 20 পাওয়া যায় সেই index
print(numbers.count(20))    # 2  -> কতবার 20 আছে
print(20 in numbers)        # True  -> আছে কিনা চেক
print(100 in numbers)       # False





List এর মান পরিবর্তন করা (Mutable Property)

List এর সবচেয়ে গুরুত্বপূর্ণ একটা বৈশিষ্ট্য হলো এটা mutable (পরিবর্তনযোগ্য) — মানে তৈরি হওয়ার পরও এর ভিতরের মান পরিবর্তন করা যায়।

fruits = ["apple", "banana", "mango"]
fruits[1] = "grape"
print(fruits)  # ['apple', 'grape', 'mango']


পাইথন list এর official method মাত্র ১১টা, আর সবগুলোই আগে কভার হয়ে গেছে। উপরে যেগুলো দিলাম (zip, map, filter, any, all, unpacking) সেগুলো method না,
এগুলো হলো পাইথনের built-in function যেগুলো list এর সাথে খুব বেশি একসাথে ব্যবহার হয় — এগুলো জানা থাকলে backend/FastAPI কাজে অনেক সুবিধা হবে।

List এর মধ্যে সরাসরি একাধিক শর্ত (if-else সহ Comprehension)

numbers = [1, 2, 3, 4, 5, 6]

result = ["জোড়" if n % 2 == 0 else "বিজোড়" for n in numbers]
print(result)  # ['বিজোড়', 'জোড়', 'বিজোড়', 'জোড়', 'বিজোড়', 'জোড়']
