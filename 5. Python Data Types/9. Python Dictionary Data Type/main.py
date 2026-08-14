Dictionary হলো পাইথনের একটা ডেটা টাইপ যেটা ডেটা রাখে Key-Value জোড়া (pair) আকারে। List/Tuple/Set এ শুধু value থাকতো, 
index দিয়ে খুঁজতে হতো। কিন্তু Dictionary তে প্রতিটা value এর একটা নাম (key) থাকে, যেটা দিয়ে সরাসরি সেই value খুঁজে বের করা যায়।

সহজ কথায়: এটা অনেকটা বাস্তব জীবনের অভিধান (dictionary) এর মতো — যেমন একটা শব্দ (key) দিয়ে তার অর্থ (value) খোঁজা হয়।
Dictionary (dict) হলো Python-এর একটি Built-in Data Type যা Key-Value Pair আকারে ডেটা সংরক্ষণ করে।

. Dictionary তৈরি করার নিয়ম

Dictionary লেখা হয় curly bracket { } দিয়ে, প্রতিটা key: value জোড়া কোলন (:) দিয়ে আলাদা করা হয়, আর একাধিক জোড়া কমা (,) দিয়ে আলাদা করা হয়।

# একটি ছাত্রের তথ্য নিয়ে ডিকশনারি
student = {
    "name": "Abdullah",
    "age": 22,
    "cgpa": 3.75,
    "is_active": True
}

print(student)

এখানে "name", "age", "cgpa", "is_active" হলো Keys (চাবি)।

আর "Abdullah", 22, 3.75, True হলো তাদের নিজস্ব Values (মান)।


student = {
    "name": "Arman",
    "age": 22,
    "department": "CSE"
}

"name"       → Key
"Arman"      → Value

"age"        → Key
22           → Value

"department" → Key
"CSE"        → Value



empty_dict = {}                                    # খালি dictionary
person = {"name": "Rahim", "age": 25}               # key-value জোড়া
student = {"id": 1, "name": "Karim", "pass": True}  # বিভিন্ন টাইপের value







ডিকশনারি থেকে ডেটা অ্যাক্সেস করার নিয়ম:
লিস্ট বা টিউপলের মতো এখানে ইনডেক্স (student[0]) দিয়ে ডেটা পাওয়া যায় না। ডিকশনারির ডেটা পেতে হলে তার Key ধরে ডাকতে হয়:


# একটি ছাত্রের তথ্য নিয়ে ডিকশনারি
student = {
    "name": "Rahim",
    "age": 22,
    "cgpa": 3.75,
    "is_active": True
}

print(student)

print(student["name"])  # আউটপুট: Rahim
print(student["cgpa"])  # আউটপুট: 3.75

⚠️ বিশেষ সতর্কতা (KeyError):
যদি এমন কোনো Key দিয়ে ডিকশনারি থেকে মান খুঁজতে চান যা ডিকশনারির ভেতরে নেই, তবে পাইথন ক্র্যাশ করবে এবং KeyError দিবে। 
এই সমস্যা থেকে বাঁচার জন্য get() মেথড ব্যবহার করা যায়:

# 'phone' নামে কোনো কি নেই, তাই এটি এরর না দিয়ে None রিটার্ন করবে
print(student.get("phone"))  # আউটপুট: None


Key দিয়ে Value বের করা

Dictionary তে index number না, key দিয়ে value access করতে হয়।

person = {"name": "Rahim", "age": 25, "city": "Dhaka"}

print(person["name"])   # Rahim
print(person["age"])    # 25
print(person["city"])   # Dhaka

⚠️ না থাকা key দিয়ে access করলে Error

print(person["salary"]) KeyError: 'salary'

নিরাপদ পদ্ধতি — get() মেথড ব্যবহার করা

print(person.get("salary"))          # None  (error দেয় না)
print(person.get("salary", "N/A"))   # N/A   (default value দেওয়া যায়)

get() মেথড দিয়ে access করলে key না থাকলেও প্রোগ্রাম crash করে না, বরং None অথবা নিজের দেওয়া default মান রিটার্ন করে। 
এটা backend code এ best practice।





Dictionary এর মান পরিবর্তন করা (Mutable Property)

person = {"name": "Rahim", "age": 25}

person["age"] = 26          # পুরনো value পরিবর্তন
print(person)  # {'name': 'Rahim', 'age': 26}




নতুন Key-Value যোগ করা

person = {"name": "Rahim", "age": 25}

person["city"] = "Dhaka"    # নতুন key-value যোগ হচ্ছে
print(person)  # {'name': 'Rahim', 'age': 25, 'city': 'Dhaka'}

⚠️  — Dictionary তে নতুন item যোগ করতে append() লাগে না (List এর মতো), শুধু নতুন key বসিয়ে value assign করলেই যোগ হয়ে যায়।






ডিকশনারি থেকে ডেটা ডিলিট করা (pop(), popitem(), del)

pop(key): নির্দিষ্ট কোনো Key এবং তার মান মুছে ফেলতে।

popitem(): পাইথনের সাম্প্রতিক ভার্সনগুলোতে ডিকশনারির শেষের দিক থেকে যেকোনো একটি আইটেম (Key-Value জোড়া) ডিলিট করে দেয়।

del keyword: নির্দিষ্ট কি ধরে ডিলিট করতে।


pop() — নির্দিষ্ট key সরিয়ে তার value রিটার্ন করা

person = {"name": "Rahim", "age": 25, "city": "Dhaka"}

removed_value = person.pop("age")
print(removed_value)  # 25
print(person)         # {'name': 'Rahim', 'city': 'Dhaka'}

কাজ কী: নির্দিষ্ট কোনো Key এবং তার সাথে থাকা মানটি ডিকশনারি থেকে মুছে ফেলতে এটি ব্যবহার করা হয়। এছাড়া মুছে ফেলা মানটি 
চাইলে একটি ভ্যারিয়েবলে ধরেও রাখা যায়।

profile = {
    "name": "Abdullah",
    "age": 30,
    "city": "Dhaka"
}

# নির্দিষ্ট 'age' কি ডিলিট করা হচ্ছে
removed_val = profile.pop("age")

print("মুছে ফেলা মান:", removed_val)  # আউটপুট: 30
print("ডিকশনারি:", profile)          # আউটপুট: {'name': 'Abdullah', 'city': 'Dhaka'}




popitem() — সর্বশেষ যোগ হওয়া key-value জোড়া সরানো

কাজ কী: পাইথনের সাম্প্রতিক ভার্সনগুলোতে (Python 3.7+) ডিকশনারির একদম শেষের দিকে থাকা আইটেমটি (একটি Key-Value জোড়া) ডিলিট করে দেয় 
এবং সেটি একটি টাপল আকারে রিটার্ন করে। এখানে আলাদা করে কোনো কি-র নাম বলে দিতে হয় না।


person = {"name": "Rahim", "age": 25, "city": "Dhaka"}

last_item = person.popitem()
print(last_item)  # ('city', 'Dhaka')
print(person)      # {'name': 'Rahim', 'age': 25}



# একটি গাড়ির ডিকশনারি
car = {
    "brand": "Toyota",
    "model": "Premio",
    "year": 2018
}

# popitem() কল করলে একদম শেষের জোড়া ('year': 2018) ডিলিট হয়ে যাবে
deleted_item = car.popitem()

print("যে জোড়াটি মুছে গেছে:", deleted_item)  # আউটপুট: ('year', 2018)
print("ডিকশনারি এখন যেমন আছে:", car) 
# আউটপুট: {'brand': 'Toyota', 'model': 'Premio'}



del — key দিয়ে item মুছে ফেলা
কাজ কী: এটি কোনো ফাংশন বা মেথড নয়, পাইথনের একটি বিল্ট-ইন কিওয়ার্ড। সুনির্দিষ্ট কোনো Key ধরে ডিকশনারি থেকে ডেটা মুছে ফেলতে এটি ব্যবহৃত হয়।
(pop() এর মতো এটি মুছে ফেলা মান রিটার্ন করে না, সরাসরি ডিকশনারি থেকে উড়িয়ে দেয়)।


person = {"name": "Rahim", "age": 25}
del person["age"]
print(person)  # {'name': 'Rahim'}


# একটি পণ্যের ডিকশনারি
product = {
    "id": 101,
    "title": "Laptop",
    "price": 45000,
    "stock": 10
}

# del কিওয়ার্ড ব্যবহার করে 'price' কি-টি মুছে ফেলা হচ্ছে
del product["price"]

print("ডিকশনারি এখন যেমন আছে:", product) 
# আউটপুট: {'id': 101, 'title': 'Laptop', 'stock': 10}



clear() — পুরো dictionary খালি করা

person = {"name": "Rahim", "age": 25}
person.clear()
print(person)  # {}

নির্দিষ্ট কোনো Key এর নাম ধরে ডিলিট করতে  pop(key) বা del ব্যবহার করা লাগবে ।
কোনো নাম না দিয়ে ডিকশনারির একদম শেষের জোড়াটি উড়িয়ে দিতে popitem() ব্যবহার করা লাগবে।







Dictionary এর তিনটা গুরুত্বপূর্ণ View — keys(), values(), items() ডিকশনারি থেকে কি, ভ্যালু বা দুটোই একসাথে লুপ চালিয়ে বের করার জন্য চমৎকার কিছু মেথড


keys() — সব key এর তালিকা keys() মেথড


ডিকশনারির ভেতরে যতগুলো চাবি বা Key আছে, শুধু সেগুলোকে আলাদা করে বের করে আনতে এটি ব্যবহার করা হয়।


person = {"name": "Rahim", "age": 25, "city": "Dhaka"}
print(person.keys())    # dict_keys(['name', 'age', 'city'])



student = {"name": "Rahim", "age": 22, "cgpa": 3.75}

# শুধু কি-গুলো দেখতে:
for key in student.keys():
    print(key)

# শুধু ভ্যালুগুলো দেখতে:
for val in student.values():
    print(val)

# কি এবং ভ্যালু একসাথে (সবচেয়ে বেশি ব্যবহৃত):
for key, value in student.items():
    print(key, "-->", value)




# Abdullah-র তথ্য সম্বলিত ডিকশনারি
abdullah_info = {
    "name": "Abdullah",
    "age": 30,
    "profession": "Engineer"
}

# শুধু কি (Keys) গুলো বের করা হচ্ছে
all_keys = abdullah_info.keys()

print("ডিকশনারির সব কি (Keys):", all_keys)
# আউটপুট: dict_keys(['name', 'age', 'profession'])


কাজের সময় অনেক সময় শুধু কি-গুলোর ওপর লুপ চালিয়ে কাজ করতে হয়।
যেমন, আব্দুল্লাহর প্রোফাইলে কী কী ফিল্ড বা ইনফরমেশন সেভ করা আছে তা চেক করা:

abdullah_profile = {
    "name": "Abdullah",
    "age": 30,
    "city": "Sylhet",
    "status": "Active"
}

print("আব্দুল্লাহর প্রোফাইলের ফিল্ডগুলোর নাম:")
for key in abdullah_profile.keys():
    print("-", key)


আব্দুল্লাহর প্রোফাইলের ফিল্ডগুলোর নাম:
- name
- age
- city
- status





values() — সব value এর তালিকা 
ডিকশনারির কি-গুলোর বিপরীতে যে মান বা Values গুলো জমা আছে, শুধু সেগুলোকে আলাদা করে বের করতে এটি ব্যবহার করা হয়।


person = {"name": "Rahim", "age": 25, "city": "Dhaka"}
print(person.values())  # dict_values(['Rahim', 25, 'Dhaka'])


# Abdullah-র তথ্য সম্বলিত ডিকশনারি
abdullah_info = {
    "name": "Abdullah",
    "age": 30,
    "profession": "Engineer"
}

# শুধু মান (Values) গুলো বের করা হচ্ছে
all_values = abdullah_info.values()

print("ডিকশনারির সব মান (Values):", all_values)
# আউটপুট: dict_values(['Abdullah', 30, 'Engineer'])



আব্দুল্লাহর প্রোফাইলে কী কী ভ্যালু বা তথ্য ইনপুট দেওয়া আছে (কি বা নাম বাদ দিয়ে):


abdullah_details = {
    "name": "Abdullah",
    "age": 30,
    "skill": "Python",
    "country": "Bangladesh"
}

print("আব্দুল্লাহর প্রোফাইলের ভেতরের মানগুলো:")
for val in abdullah_details.values():
    print(">", val)


আব্দুল্লাহর প্রোফাইলের ভেতরের মানগুলো:
> Abdullah
> 30
> Python
> Bangladesh




items() মেথডের উদাহরণ

ডিকশনারির প্রতিটি Key এবং Value জোড়ায় জোড়ায় (Tuple আকারে) একসাথে বের করে আনতে এটি ব্যবহার করা হয়। 
লুপ চালানোর সময় এটি সবচেয়ে বেশি কাজে লাগে।

person = {"name": "Rahim", "age": 25, "city": "Dhaka"}

print(person.values())  # dict_values(['Rahim', 25, 'Dhaka'])



# Abdullah-র তথ্য সম্বলিত ডিকশনারি
abdullah_info = {
    "name": "Abdullah",
    "age": 30,
    "profession": "Engineer"
}

# কি এবং মান একসাথে (Items) বের করা হচ্ছে
all_items = abdullah_info.items()

print("ডিকশনারির সব জোড়া (Items):", all_items)
# আউটপুট: dict_items([('name', 'Abdullah'), ('age', 30), ('profession', 'Engineer')])


সবচেয়ে চমৎকার ব্যবহার হলো items() দিয়ে লুপ চালিয়ে একবারে কি এবং ভ্যালু সুন্দর ফরম্যাটে প্রিন্ট করা:

abdullah_bio = {
    "name": "Abdullah",
    "age": 30,
    "profession": "Developer",
    "score": 95
}

print("--- আব্দুল্লাহর বায়োডাটা ---")
for key, value in abdullah_bio.items():
    print(f"{key} : {value}")

--- আব্দুল্লাহর বায়োডাটা ---
name : Abdullah
age : 30
profession : Developer
score : 95






অ্যাডভান্সড লেভেল - নেস্টেড ডিকশনারি ও ডিকশনারি কমপ্রিহেনশন (Advanced Level)

১. নেস্টেড ডিকশনারি (Nested Dictionary):
একটি ডিকশনারির ভেতরের ভ্যালু হিসেবে যদি আরেকটি ডিকশনারি বসিয়ে দেওয়া হয়, তাকে নেস্টেড ডিকশনারি বলে। 
রিয়েল-ওয়ার্ল্ড প্রজেক্টে (যেমন: ডাটাবেজ বা জেসন ডেটা হ্যান্ডেলিংয়ে) এটি প্রচুর ব্যবহার করা হয়।

# একটি ক্লাসের একাধিক ছাত্রের তথ্য রাখার নেস্টেড ডিকশনারি
classroom = {
    "student_1": {"name": "Rahim", "age": 22},
    "student_2": {"name": "Karim", "age": 23}
}

# করিমের বয়স দেখতে চাইলে:
print(classroom["student_2"]["age"])  # আউটপুট: 23



২. ডিকশনারি কমপ্রিহেনশন (Dictionary Comprehension):
এক লাইনে লজিক লিখে খুব দ্রুত নতুন ডিকশনারি তৈরি করার আধুনিক পাইথন পদ্ধতি। যেমন, ১ থেকে ৫ পর্যন্ত সংখ্যাগুলোর স্কয়ার বা বর্গ বের করে একটি ডিকশনারি বানাতে হবে:


# এক লাইনে ডিকশনারি কমপ্রিহেনশন
squares = {x: x**2 for x in range(1, 6)}

print(squares)
# আউটপুট: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


 আন্ডার দ্য হুড মেকানিজম ও স্পিড (Under the Hood)কম্পিউটার সায়েন্সের দৃষ্টিকোণ থেকে ডিকশনারি হলো পাইথনের সবচেয়ে পাওয়ারফুল ডেটা স্ট্রাকচার।
 হাশ টেবিল (Hash Table): সেটের মতো ডিকশনারিও ইন্টারনালি হাশ টেবিল অ্যালগরিদম ব্যবহার করে। 
 এর ফলে যেকোনো Key দিয়ে তার Value খুঁজতে বা চেক করতে সুপার ফাস্ট সময় লাগে—যার টাইম কমপ্লেক্সিটি হলো O(1) (Constant Time)। 
 লাখ লাখ ডেটার ভেতর থেকেও ডিকশনারির কি মুহূর্তের মধ্যে খুঁজে পাওয়া যায়।
 Immutable Keys: ডিকশনারির Key হিসেবে সবসময় এমন ডেটা দিতে হয় যা পরিবর্তন করা যায় না (যেমন: String, Number, Tuple)।
 লিস্ট (List) মিউটেবল হওয়ায় ডিকশনারির Key হিসেবে ব্যবহার করা যায় না, দিলেই পাইথন TypeError দিবে।





 in দিয়ে Key আছে কিনা চেক করা

 person = {"name": "Rahim", "age": 25}

print("name" in person)      # True
print("salary" in person)    # False




Dictionary এর দৈর্ঘ্য বের করা


person = {"name": "Rahim", "age": 25, "city": "Dhaka"}
print(len(person))  # 3  (মোট কতগুলো key-value জোড়া আছে)



update() — একাধিক Key-Value একসাথে যোগ/পরিবর্তন করা

person = {"name": "Rahim", "age": 25}

person.update({"age": 26, "city": "Dhaka"})
print(person)  # {'name': 'Rahim', 'age': 26, 'city': 'Dhaka'}
age আগে থেকেই ছিল, তাই সেটা পরিবর্তন হয়েছে (26 হয়েছে), আর city নতুন ছিল, তাই যোগ হয়েছে।




Nested Dictionary (Dictionary এর ভিতরে Dictionary) — Advanced

students = {
    "student1": {"name": "Rahim", "age": 22},
    "student2": {"name": "Karim", "age": 23}
}

print(students["student1"])           # {'name': 'Rahim', 'age': 22}
print(students["student1"]["name"])   # Rahim

এটা backend/API কাজে খুবই common — একটা user এর ভিতরে আরও sub-detail (যেমন address, permissions) রাখতে হলে nested dictionary ব্যবহার হয়।




Dictionary এর ভিতরে List, List এর ভিতরে Dictionary — Advanced

company = {
    "name": "TechCorp",
    "employees": ["Rahim", "Karim", "Salma"]
}

print(company["employees"])      # ['Rahim', 'Karim', 'Salma']
print(company["employees"][0])   # Rahim


students = [
    {"name": "Rahim", "age": 22},
    {"name": "Karim", "age": 23}
]

for student in students:
    print(student["name"])

Rahim
Karim



Dictionary Comprehension — Advanced (এক লাইনে Dictionary তৈরি)

numbers = [1, 2, 3, 4, 5]

squares = {n: n**2 for n in numbers}
print(squares)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}



শর্ত (condition) সহ:

numbers = [1, 2, 3, 4, 5, 6]

even_squares = {n: n**2 for n in numbers if n % 2 == 0}
print(even_squares)  # {2: 4, 4: 16, 6: 36}





Dictionary Copy করা — গুরুত্বপূর্ণ সতর্কতা (List এর মতোই সমস্যা)

dict1 = {"a": 1, "b": 2}
dict2 = dict1        # ⚠️ এটা copy না, একই dictionary কে point করছে!

dict2["c"] = 3
print(dict1)  # {'a': 1, 'b': 2, 'c': 3}  -> dict1 ও পরিবর্তন হয়ে গেছে!

সঠিক copy করার পদ্ধতি:

dict1 = {"a": 1, "b": 2}
dict2 = dict1.copy()

dict2["c"] = 3
print(dict1)  # {'a': 1, 'b': 2}     -> অপরিবর্তিত
print(dict2)  # {'a': 1, 'b': 2, 'c': 3}




Key হিসেবে কী কী ব্যবহার করা যায় (Rule)

Dictionary এর key অবশ্যই immutable ডেটা টাইপ হতে হবে — যেমন string, number, tuple। 
কিন্তু list বা dictionary key হিসেবে ব্যবহার করা যায় না(কারণ এগুলো mutable)।


valid = {1: "one", "two": 2, (1, 2): "tuple key"}   # ঠিক আছে

invalid = {[1, 2]: "list key"}   # TypeError: unhashable type: 'list'

value হিসেবে যেকোনো ডেটা টাইপ ব্যবহার করা যায় (list, dictionary, এমনকি function-ও)।




fromkeys() — একই value দিয়ে একাধিক key তৈরি করা

keys = ["a", "b", "c"]
default_dict = dict.fromkeys(keys, 0)
print(default_dict)  # {'a': 0, 'b': 0, 'c': 0}




setdefault() — Key থাকলে value নেয়, না থাকলে নতুন যোগ করে

person = {"name": "Rahim"}

age = person.setdefault("age", 18)
print(age)      # 18  (নতুন key যোগ হয়েছে, ডিফল্ট মান দিয়ে)
print(person)   # {'name': 'Rahim', 'age': 18}

name = person.setdefault("name", "Unknown")
print(name)     # Rahim  (আগে থেকেই ছিল, তাই পুরনো মানই থাকে)



Dictionary Sorting — Advanced

Dictionary নিজে থেকে সাজানো যায় না (কারণ Python 3.7+ এ order insertion অনুযায়ী থাকে, কিন্তু sort মেথড নেই), 
তবে sorted() ফাংশন ব্যবহার করে sorted করা যায়:


marks = {"Rahim": 85, "Karim": 92, "Salma": 78}

# Key অনুযায়ী সাজানো
sorted_by_key = dict(sorted(marks.items()))
print(sorted_by_key)  # {'Karim': 92, 'Rahim': 85, 'Salma': 78}

# Value অনুযায়ী সাজানো
sorted_by_value = dict(sorted(marks.items(), key=lambda x: x[1]))
print(sorted_by_value)  # {'Salma': 78, 'Rahim': 85, 'Karim': 92}




কতবার কোনো শব্দ এসেছে গোনা (Word Count)

text = "apple banana apple mango banana apple"
words = text.split()

word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1

print(word_count)  # {'apple': 3, 'banana': 2, 'mango': 1}




Simple Database এর মতো ব্যবহার (in-memory storage)

users_db = {
    1: {"name": "Rahim", "email": "rahim@email.com"},
    2: {"name": "Karim", "email": "karim@email.com"}
}

user_id = 1
print(users_db[user_id]["name"])  # Rahim




সাধারণ ভুল (Common Mistakes)


# ভুল ১: না থাকা key সরাসরি access করা
person = {"name": "Rahim"}
print(person["age"])   # KeyError

# ভুল ২: mutable জিনিস (list) কে key হিসেবে ব্যবহার
d = {[1, 2]: "value"}  # TypeError: unhashable type: 'list'

# ভুল ৩: dict copy না করে সরাসরি assign করে ভাবা এটা আলাদা
d1 = {"a": 1}
d2 = d1        # copy না!

# ভুল ৪: খালি dict ভেবে {} লেখা, কিন্তু ভুলে set এর সাথে গুলিয়ে ফেলা
empty = {}     # এটা dict, set না

