📌 স্ট্রিং কনকাটেনেশন কী?
স্ট্রিং কনকাটেনেশন হলো দুই বা ততোধিক স্ট্রিংকে একত্রিত করে একটি নতুন স্ট্রিং তৈরি করা। পাইথনে স্ট্রিং ইমিউটেবল (immutable), তাই প্রতিবার কনকাটেনেশনে নতুন স্ট্রিং অবজেক্ট তৈরি হয়।

 ১: বেসিক কনকাটেনেশন পদ্ধতি

# বেসিক কনকাটেনেশন
first = "Hello"
last = "World"
result = first + " " + last
print(result)  # Hello World

# একাধিক স্ট্রিং
full = "Python" + " " + "is" + " " + "awesome"
print(full)  # Python is awesome

# সংখ্যার সাথে স্ট্রিং কনকাটেনেশন - এরর!
# age = 25
# message = "I am " + age + " years old"  # TypeError!

# সঠিক উপায়
age = 25
message = "I am " + str(age) + " years old"
print(message)  # I am 25 years old




# পাইথন (Python)
result = 5 + "5"  
# ❌ TypeError: unsupported operand type(s) for +: 'int' and 'str'

📌 পাইথনে কেন এরর দেয়?
পাইথনের ডিজাইন ফিলোসফি হলো "Explicit is better than implicit" (স্পষ্টতা ভালো)। পাইথন ইমপ্লিসিট (implicit) টাইপ কনভার্সন করে না। অর্থাৎ, এটি নিজে থেকে ধরে নেয় না যে কী চাওয়া হয়। 
যখন একটি ইন্টিজারের সাথে স্ট্রিং যোগ করার চেষ্টা করা হয়, পাইথন বুঝতে পারে না যে যোগ করা নাকি কনকাটেনেট করা হসছে , তাই এটি এরর দেয়।

পাইথনে সংখ্যা ও স্ট্রিং একত্রে কাজ করতে চাইলে এক্সপ্লিসিট (explicit) কনভার্সন করতে হবে।

১. সংখ্যাকে স্ট্রিংয়ে কনভার্ট করা (স্ট্রিং কনকাটেনেশন)

age = 25
message = "I am " + str(age) + " years old"
print(message)  # I am 25 years old


২. f-string ব্যবহার করা (সেরা পদ্ধতি)

age = 25
message = f"I am {age} years old"
print(message)  # I am 25 years old




পাইথনে স্ট্রিং-এর সাথে সংখ্যা (integer/float) ব্যবহার করলে -, *, /, % এই অপারেটরগুলো কী ফেরত দেয়।

১. * (গুণ) — ✅ কাজ করে, রিটার্ন করে স্ট্রিং
যখন স্ট্রিং * সংখ্যা, পাইথন এটি রিপিটিশন (পুনরাবৃত্তি) হিসেবে ধরে নেয়। এটি একটি নতুন স্ট্রিং তৈরি করে 

# উদাহরণ ১: বেসিক রিপিটিশন
text = "Hi"
result = text * 3
print(result)           # আউটপুট: HiHiHi
print(type(result))     # আউটপুট: <class 'str'>

# উদাহরণ ২: সংখ্যা * স্ট্রিং-ও কাজ করে
result = 3 * "Ha"
print(result)           # আউটপুট: HaHaHa

# উদাহরণ ৩: বড় স্ট্রিং তৈরি (ব্যাকএন্ডে ইউজ)
line = "-" * 50
print(line)             # আউটপুট: --------------------------------------------------
print(type(line))       # আউটপুট: <class 'str'>

# উদাহরণ ৪: স্পেস তৈরি
indent = " " * 4
print(f"{indent}Hello") # আউটপুট:     Hello

# ব্যতিক্রম: স্ট্রিং * স্ট্রিং কাজ করে না
# result = "Hi" * "3"   # ❌ TypeError: can't multiply sequence by non-int of type 'str'


২. - (বিয়োগ) — ❌ কাজ করে না, রিটার্ন দেয় TypeErro
পাইথনে স্ট্রিং থেকে কোনো সংখ্যা বা অন্য স্ট্রিং বাদ দেওয়ার কোনো গাণিতিক অর্থ নেই। তাই এটি এরর দেয়।

# উদাহরণ ১: স্ট্রিং থেকে সংখ্যা বাদ দেওয়া
# result = "Hello" - 2   # ❌ TypeError: unsupported operand type(s) for -: 'str' and 'int'

# উদাহরণ ২: স্ট্রিং থেকে স্ট্রিং বাদ দেওয়া
# result = "Hello" - "H" # ❌ TypeError: unsupported operand type(s) for -: 'str' and 'str'


৩. / (ভাগ) — ❌ কাজ করে না, রিটার্ন দেয় TypeError
স্ট্রিংকে কোনো সংখ্যা দিয়ে ভাগ করার কোনো গাণিতিক অর্থ পাইথনে নেই।


# উদাহরণ ১: স্ট্রিংকে সংখ্যা দিয়ে ভাগ
# result = "Hello" / 2   # ❌ TypeError: unsupported operand type(s) for /: 'str' and 'int'

# উদাহরণ ২: স্ট্রিংকে স্ট্রিং দিয়ে ভাগ
# result = "Hello" / "H" # ❌ TypeError: unsupported operand type(s) for /: 'str' and 'str'


৪. % (মডুলাস/ভাগশেষ) — ❌ সাধারণত কাজ করে না (শুধু ফরম্যাটিং-এ)
সাধারণ গাণিতিক % (ভাগশেষ) স্ট্রিং-এ কাজ করে না এবং TypeError দেয়।

# উদাহরণ ১: স্ট্রিং % সংখ্যা (গাণিতিক মডুলাস)
# result = "Hello" % 2   # ❌ TypeError: not all arguments converted during string formatting

# উদাহরণ ২: স্ট্রিং % স্ট্রিং
# result = "Hello" % "H" # ❌ TypeError: not all arguments converted during string formatting


কিন্তু, %-এর একটি বিশেষ ব্যবহার আছে যখন এটি স্ট্রিং ফরম্যাটিং-এর জন্য ব্যবহার করা হয়। সেক্ষেত্রে এটি স্ট্রিং ফেরত দেয় (পুরনো স্টাইল)

# স্ট্রিং ফরম্যাটিং (পুরনো স্টাইল) - এটি কাজ করে
name = "John"
result = "Hello %s" % name
print(result)           # আউটপুট: Hello John
print(type(result))     # আউটপুট: <class 'str'>

# কিন্তু এখানে বাম পাশে থাকতে হবে স্ট্রিং, ডান পাশে টাপল বা ডিকশনারি
# সংখ্যার সাথে সরাসরি স্ট্রিং % সংখ্যা করলে কাজ করে না!









৩. join() মেথড (সবচেয়ে কার্যকরী)

# লিস্ট থেকে জয়েন
words = ["Python", "is", "awesome"]
result = " ".join(words)
print(result)  # Python is awesome

# কমা দিয়ে
fruits = ["apple", "banana", "orange"]
result = ", ".join(fruits)
print(result)  # apple, banana, orange

# নিউলাইন দিয়ে
lines = ["Line 1", "Line 2", "Line 3"]
result = "\n".join(lines)
print(result)
# Line 1
# Line 2
# Line 3

# খালি স্ট্রিং দিয়ে
chars = ['H', 'e', 'l', 'l', 'o']
result = ''.join(chars)
print(result)  # Hello



৪. f-strings (Python 3.6+) - সবচেয়ে সুপারিশকৃত

# বেসিক f-string
name = "Alice"
age = 30
city = "Dhaka"

message = f"My name is {name}, I am {age} years old from {city}"
print(message)  # My name is Alice, I am 30 years old from Dhaka

# এক্সপ্রেশন ইনসাইড f-string
price = 49.99
tax = 0.15
total = f"Total: ${price + (price * tax):.2f}"
print(total)  # Total: $57.49

# ফাংশন কল
def greet(name):
    return f"Hello {name}"

message = f"{greet('Bob')}, welcome!"
print(message)  # Hello Bob, welcome!

# ডিকশনারি আনপ্যাকিং
user = {"name": "John", "age": 25}
message = f"User: {user['name']}, Age: {user['age']}"
print(message)  # User: John, Age: 25

# মাল্টিলাইন f-string
name = "Alice"
age = 30
bio = f"""
Name: {name}
Age: {age}
Status: {'Adult' if age >= 18 else 'Minor'}
"""
print(bio)


৫. format() মেথড

# পজিশনাল আর্গুমেন্ট
name = "Alice"
age = 30
message = "My name is {}, I am {} years old".format(name, age)
print(message)  # My name is Alice, I am 30 years old

# ইনডেক্স দিয়ে
message = "My name is {0}, I am {1} years old".format(name, age)
print(message)  # My name is Alice, I am 30 years old

# কীওয়ার্ড আর্গুমেন্ট
message = "My name is {name}, I am {age} years old".format(name=name, age=age)
print(message)  # My name is Alice, I am 30 years old

# ডিকশনারি আনপ্যাকিং
data = {"name": "Bob", "age": 25}
message = "My name is {name}, I am {age} years old".format(**data)
print(message)  # My name is Bob, I am 25 years old

# ফরম্যাটিং স্পেসিফিকেশন
price = 49.99
message = "Price: ${:.2f}".format(price)
print(message)  # Price: $49.99

# নম্বর ফরম্যাটিং
number = 1234567.89
print("{:,}".format(number))  # 1,234,567.89
print("{:.2f}".format(number))  # 1234567.89
print("{:.2%}".format(0.25))  # 25.00%





অ্যাডভান্সড কনকাটেনেশন টেকনিক



io.StringIO - মেমোরি এফিসিয়েন্ট

from io import StringIO

# বড় স্ট্রিং কনকাটেনেশনের জন্য
def build_large_string():
    output = StringIO()
    for i in range(1000):
        output.write(f"Line {i}\n")
    return output.getvalue()

result = build_large_string()
print(result[:100])  # প্রথম ১০০ ক্যারেক্টার

# পারফরম্যান্স তুলনা
import time

# খারাপ পদ্ধতি (+ ব্যবহার)
start = time.time()
result = ""
for i in range(10000):
    result += str(i) + " "
end = time.time()
print(f"Plus operator: {end - start:.4f}s")

# ভালো পদ্ধতি (join)
start = time.time()
result = " ".join(str(i) for i in range(10000))
end = time.time()
print(f"Join method: {end - start:.4f}s")

# ভালো পদ্ধতি (StringIO)
start = time.time()
output = StringIO()
for i in range(10000):
    output.write(str(i) + " ")
result = output.getvalue()
end = time.time()
print(f"StringIO: {end - start:.4f}s")




textwrap - টেক্সট ফরম্যাটিং
import textwrap

# লং টেক্সট র‍্যাপ
long_text = """
Python is a programming language that lets you work quickly and 
integrate systems more effectively. It is widely used in data science, 
web development, and automation.
"""

wrapped = textwrap.fill(long_text, width=40)
print(wrapped)

# ইন্ডেন্ট
text = "Hello World"
indented = textwrap.indent(text, "    ")
print(indented)  #     Hello World

# ডিডেন্ট (ইন্ডেন্ট রিমুভ)
text = """
    Hello
        World
    Python
"""
dedented = textwrap.dedent(text)
print(dedented)






টেমপ্লেট স্ট্রিং (Template Strings)

from string import Template

# বেসিক টেমপ্লেট
template = Template("Hello $name, you are $age years old")
result = template.substitute(name="Alice", age=30)
print(result)  # Hello Alice, you are 30 years old

# ডিকশনারি দিয়ে
data = {"name": "Bob", "age": 25}
result = template.substitute(data)
print(result)  # Hello Bob, you are 25 years old

# $$ - ডলার সাইন
template = Template("Cost: $$$price")
result = template.substitute(price=100)
print(result)  # Cost: $100

# safe_substitute - মিসিং ভ্যালু হ্যান্ডেল
template = Template("Hello $name, from $city")
result = template.safe_substitute(name="Alice")
print(result)  # Hello Alice, from $city (মিসিং ভ্যালু)

# কাস্টম ডিলিমিটার
class CustomTemplate(Template):
    delimiter = '@'

template = CustomTemplate("Hello @name, you are @age")
result = template.substitute(name="Alice", age=30)
print(result)  # Hello Alice, you are 30


pprint - প্রিটি প্রিন্ট

import pprint

# জটিল ডেটা প্রিন্ট
data = {
    "users": [
        {"name": "Alice", "age": 30, "email": "alice@example.com"},
        {"name": "Bob", "age": 25, "email": "bob@example.com"}
    ],
    "total": 2,
    "status": "active"
}

# সাধারণ প্রিন্ট
print(data)

# প্রিটি প্রিন্ট
pprint.pprint(data, indent=2, width=40)
