পাইথনে Comparison Operators বা তুলনা করার অপারেটর হলো এমন কিছু বিশেষ চিহ্ন, যা দুটি সংখ্যা, ভ্যারিয়েবল বা মানের মধ্যে তুলনা করতে ব্যবহৃত হয়।
তুলনা অপারেটর দুটি মান/ভেরিয়েবলের মধ্যে তুলনা করে এবং একটি বুলিয়ান ফলাফল প্রদান করে: True যেমন `true` বা False`false`। 


অপারেটর	        নাম	                              কাজ	                                 উদাহরণ (x=5, y=3)
>	               বড় (Greater Than)	                বামের মান ডানের চেয়ে বড় কিনা	         x > y → True
<	               ছোট (Less Than)	                  বামের মান ডানের চেয়ে ছোট কিনা	         x < y → False
>=	             বড় বা সমান (Greater or Equal)	    বামের মান ডানের চেয়ে বড় বা সমান কিনা	 x >= y → True
<=	             ছোট বা সমান (Less or Equal)	      বামের মান ডানের চেয়ে ছোট বা সমান কিনা	 x <= y → False
==	             সমান (Equal)	                      দুটি মান সমান কিনা চেক করে	           x == y → False
!=	             অসমান (Not Equal)	                দুটি মান অসমান কিনা চেক করে	         x != y → True


বড় অপারেটর (>)
বাম পাশের মান ডান পাশের মানের চেয়ে বড় কিনা চেক করে।

age = 25
voting_age = 18

print(age > voting_age)  # True (ভোট দেওয়ার যোগ্য)

# স্ট্রিং-এ লেক্সিকোগ্রাফিক্যাল তুলনা (অক্ষর অনুযায়ী)
print("apple" > "banana")   # False ('a' < 'b')
print("banana" > "apple")   # True ('b' > 'a')
print("Python" > "Java")    # True ('P' > 'J')



ছোট অপারেটর (<)
বাম পাশের মান ডান পাশের মানের চেয়ে ছোট কিনা চেক করে।
temperature = 30
boiling_point = 100

print(temperature < boiling_point)  # True (পানি ফোটেনি)

# স্ট্রিং
print("apple" < "banana")   # True
print("car" < "bus")        # False ('c' > 'b')



বড় বা সমান অপারেটর (>=)
বাম পাশের মান ডান পাশের মানের চেয়ে বড় বা সমান কিনা চেক করে।

marks = 80
pass_marks = 80

print(marks >= pass_marks)  # True (পাস করেছে)

# অন্য উদাহরণ
score = 75
target = 80
print(score >= target)  # False (75 >= 80 নয়)



ছোট বা সমান অপারেটর (<=)
বাম পাশের মান ডান পাশের মানের চেয়ে ছোট বা সমান কিনা চেক করে।

age = 17
driving_age = 18

print(age <= driving_age)  # True (ড্রাইভিং এর বয়স হয়নি)

# অন্যটি
weight = 65
max_weight = 65
print(weight <= max_weight)  # True (ওজন সীমার মধ্যে)



অসমান অপারেটর (!=)
দুটি মান অসমান কিনা চেক করে।
x = 10
y = 5
z = 10

print(x != y)  # True
print(x != z)  # False

# স্ট্রিং
print("apple" != "apple")   # False
print("apple" != "orange")  # True



সমান অপারেটর (==)
দুটি মান সমান কিনা চেক করে।

# সংখ্যা
a = 10
b = 10
c = 5

print(a == b)  # True
print(a == c)  # False

# স্ট্রিং
name1 = "Python"
name2 = "Python"
name3 = "Java"

print(name1 == name2)  # True
print(name1 == name3)  # False

# ভিন্ন টাইপের মান
print(10 == 10.0)  # True (int ও float তুলনা সম্ভব)
print(10 == "10")  # False (ভিন্ন টাইপ)






স্ট্রিং কম্প্যারিজন (Lexicographical Comparison)
পাইথন স্ট্রিং তুলনা করে ASCII ভ্যালু অনুযায়ী (অক্ষর ক্রম অনুযায়ী)।

# 'a' (97) < 'b' (98) < 'c' (99)
print("apple" < "banana")  # True
print("abc" < "abcd")      # True (ছোট স্ট্রিং বড় স্ট্রিং-এর আগে)

# বড় হাতের অক্ষর ছোট হাতের থেকে ছোট (ASCII তে)
print("Apple" < "apple")   # True ('A' 65 < 'a' 97)

# কিন্তু কেস ইনসেনসিটিভ তুলনা চাইলে:
print("Apple".lower() == "apple".lower())  # True




চেইন কম্প্যারিজন (Chained Comparison)
পাইথনে এক লাইনে একাধিক তুলনা করা যায়! এটি পাইথনের খুবই সুন্দর ফিচার।

x = 5

# সাধারণ পদ্ধতি
print(x > 3 and x < 10)  # True

# চেইন কম্প্যারিজন (পাইথন স্টাইল)
print(3 < x < 10)  # True (একেবারে গাণিতিক নোটেশনের মতো!)

# অন্যান্য উদাহরণ
age = 25
print(18 <= age <= 60)  # True (বয়স ১৮-৬০ এর মধ্যে)

score = 85
print(80 <= score <= 100)  # True (স্কোর ৮০-১০০ এর মধ্যে)

# একাধিক চেইন
a = 10
print(5 < a < 15 < 20)  # True (সব শর্ত পূরণ করে)




লিস্ট, টাপল, ডিকশনারি কম্প্যারিজন
পাইথনে শুধু সংখ্যা বা স্ট্রিং নয়, কম্পোজিট ডেটা টাইপ-ও তুলনা করা যায়!

# লিস্ট তুলনা (এলিমেন্ট বাই এলিমেন্ট)
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = [1, 2, 4]

print(list1 == list2)  # True
print(list1 == list3)  # False

# টাপল তুলনা
tuple1 = (10, 20)
tuple2 = (10, 20)
tuple3 = (10, 30)

print(tuple1 == tuple2)  # True
print(tuple1 < tuple3)   # True (20 < 30)

# ডিকশনারি তুলনা (কী-ভ্যালু জোড়া অনুযায়ী)
dict1 = {"a": 1, "b": 2}
dict2 = {"a": 1, "b": 2}
dict3 = {"a": 1, "b": 3}

print(dict1 == dict2)  # True
print(dict1 == dict3)  # False

# সেট তুলনা
set1 = {1, 2, 3}
set2 = {3, 2, 1}  # অর্ডার আলাদা কিন্তু সেট সমান
print(set1 == set2)  # True (সেট আনঅর্ডার্ড)




বুলিয়ান কম্প্যারিজন

# True = 1, False = 0 (সংখ্যার সাথে তুলনা করা যায়)
print(True == 1)   # True
print(False == 0)  # True
print(True > 0)    # True
print(False < 1)   # True

# বুলিয়ান নিজেদের মধ্যে
print(True == True)   # True
print(True != False)  # True



ইউজার ইনপুট ভ্যালিডেশন
age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote!")
else:
    print("Sorry, you are too young to vote.")


 পাসওয়ার্ড চেক

password = input("Enter password: ")
confirm = input("Confirm password: ")

if password == confirm:
    print("Password set successfully!")
else:
    print("Passwords do not match!")


তাপমাত্রা চেক

temp = float(input("Enter temperature: "))

if temp > 100:
    print("Water is boiling!")
elif temp < 0:
    print("Water is freezing!")
else:
    print("Water is liquid.")




রেঞ্জ চেক (চেইন কম্প্যারিজন)

score = 85

if 80 <= score <= 100:
    grade = "A"
elif 70 <= score < 80:
    grade = "B"
elif 60 <= score < 70:
    grade = "C"
else:
    grade = "F"

print(f"Grade: {grade}")  # Grade: A




লিস্টে এলিমেন্ট সার্চ

fruits = ["apple", "banana", "orange", "mango"]

user_fruit = input("Enter a fruit name: ")

if user_fruit in fruits:  # `in` অপারেটর (কম্প্যারিজন নয়, সদস্যতা পরীক্ষা)
    print(f"Yes, {user_fruit} is in the list!")
else:
    print(f"Sorry, {user_fruit} not found!")



== vs is - পার্থক্য

# == চেক করে মান (value) সমান কিনা
# is চেক করে একই অবজেক্ট (memory location) কিনা

a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)  # True (মান সমান)
print(a is b)  # False (ভিন্ন অবজেক্ট)
print(a is c)  # True (একই অবজেক্ট)

# ইমিউটেবল ডেটার ক্ষেত্রে:
x = 10
y = 10
print(x == y)  # True
print(x is y)  # True (পাইথন ছোট ইন্টিজার ক্যাশে রাখে)

# স্ট্রিং
str1 = "hello"
str2 = "hello"
print(str1 == str2)  # True
print(str1 is str2)  # True (ইন্টার্নিং)




ফ্লোটিং পয়েন্ট তুলনা (সতর্কতা)

# ভুল পদ্ধতি (কখনো কাজ নাও করতে পারে)
a = 0.1 + 0.2
b = 0.3
print(a == b)  # False! (ফ্লোটিং পয়েন্ট এরর)

# সঠিক পদ্ধতি
import math
print(math.isclose(a, b))  # True




None চেক করা

x = None

# ভুল পদ্ধতি
if x == None:  # কাজ করলেও ঠিক না
    print("x is None")

# সঠিক পদ্ধতি
if x is None:
    print("x is None")



একাধিক কম্প্যারিজন চেইনিং 
# পাইথন স্টাইল (সুন্দর ও পাঠযোগ্য)
if 18 <= age <= 60:
    print("Working age")

# অন্যান্য ভাষার স্টাইল (পাইথনেও কাজ করে)
if age >= 18 and age <= 60:
    print("Working age")




# ১.
print(5 > 3 > 1)

# ২.
print(10 == 10.0)

# ৩.
print("Python" > "python")

# ৪.
print([1, 2] == [1, 2])

# ৫.
print(3 < 5 != 8)

(উত্তরগুলো: True, True, False, True, True)



আইডেন্টিটি অপারেটর (is, is not)
গুলো মান (value) তুলনা করে না, বরং অবজেক্টের আইডেন্টিটি (মেমোরি লোকেশন) তুলনা করে।

# `is` - একই অবজেক্ট কিনা চেক করে
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a is b)      # False (ভিন্ন অবজেক্ট)
print(a is c)      # True (একই অবজেক্ট)
print(a is not b)  # True (ভিন্ন অবজেক্ট)

# ইমিউটেবল ডেটার ক্ষেত্রে
x = 10
y = 10
print(x is y)  # True (পাইথন ইন্টার্নিং করে)

# None চেক করার সঠিক উপায়
value = None
if value is None:  # ✅ সঠিক
    print("Value is None")
    
if value == None:  # ⚠️ কাজ করলেও ঠিক না
    print("Value is None")




সদস্যতা অপারেটর (in, not in)
এগুলো চেক করে কোনো এলিমেন্ট একটি কন্টেইনার (লিস্ট, টাপল, সেট, ডিকশনারি, স্ট্রিং) এর মধ্যে আছে কিনা।

# লিস্টে সদস্যতা
fruits = ["apple", "banana", "orange"]
print("apple" in fruits)     # True
print("grape" in fruits)     # False
print("grape" not in fruits) # True

# স্ট্রিংয়ে সাবস্ট্রিং
text = "Hello, World!"
print("World" in text)       # True
print("world" in text)       # False (কেস সেনসিটিভ)

# ডিকশনারিতে কী চেক
person = {"name": "Alice", "age": 30}
print("name" in person)      # True (কী চেক করে)
print("Alice" in person)     # False (ভ্যালু চেক করে না)
print("Alice" in person.values())  # True (ভ্যালু চেক করতে চাইলে)

# রেঞ্জে সদস্যতা
print(5 in range(1, 10))     # True
print(15 in range(1, 10))    # False


টাইপ কম্প্যারিজন (type() দিয়ে)
কোনো ভেরিয়েবলের টাইপ তুলনা করা:

x = 10
y = "Hello"
z = [1, 2, 3]

print(type(x) == int)        # True
print(type(y) == str)        # True
print(type(z) == list)       # True

# আধুনিক পদ্ধতি (isinstance)
print(isinstance(x, int))    # True
print(isinstance(y, str))    # True
print(isinstance(z, list))   # True

# একাধিক টাইপ চেক
print(isinstance(x, (int, float)))  # True




অবজেক্ট কম্প্যারিজন মেথড (__eq__, __lt__ ইত্যাদি)



কম্প্যারিজন চেইনিং এর বিশেষ ক্ষমতা
পাইথনে চেইন কম্প্যারিজন শুধু সংখ্যার জন্য নয়, যেকোনো তুলনাযোগ্য ডেটার জন্য কাজ করে:

# স্ট্রিং চেইন
print("apple" < "banana" < "cherry")  # True

# লিস্ট চেইন
print([1, 2] < [1, 3] < [1, 4])      # True

# মিক্সড চেইন (সতর্ক থাকুন)
x = 5
print(1 < x < 10)        # True
print(1 < x < 10 < 20)   # True

# জটিল চেইন
a = 10
b = 20
c = 30
print(a < b < c)         # True
print(a < b > c)         # False (b > c? 20 > 30? False)



বুলিয়ান অপারেটরের সাথে কম্প্যারিজন

age = 25
income = 50000

# AND অপারেটর
if age > 18 and income > 30000:
    print("Eligible for loan")

# OR অপারেটর
if age > 60 or income < 20000:
    print("Special consideration")

# NOT অপারেটর
if not (age < 18):
    print("Adult")



অল (all()) এবং যেকোনো (any()) ফাংশন
একাধিক কম্প্যারিজনের ফলাফল চেক করা:

# সবগুলো শর্ত সত্য কিনা
numbers = [10, 20, 30, 40]
print(all(num > 5 for num in numbers))   # True (সব ৫ এর বেশি)
print(all(num > 25 for num in numbers))  # False (সব ২৫ এর বেশি না)

# কোনো একটি শর্ত সত্য কিনা
print(any(num > 25 for num in numbers))  # True (৩০, ৪০ আছে)
print(any(num > 50 for num in numbers))  # False (কোনোটাই ৫০ এর বেশি না)

# ব্যবহারিক উদাহরণ
ages = [18, 20, 22, 17]
if all(age >= 18 for age in ages):
    print("All are adults")
else:
    print("Some are minors")




# এই কোডগুলোর আউটপুট?
print(1 < 2 < 3 < 4)           # ?
print(1 < 2 > 3 < 4)           # ?
print([1, 2] is [1, 2])        # ?
print(5 in range(1, 10))       # ?
print(all(x > 0 for x in [1, -2, 3]))  # ?
(উত্তর: True, False, False, True, False)






কম্প্যারিজনের জন্য functools.total_ordering





মৌলিক	==, !=, >, <, >=, <=	মান তুলনা
আইডেন্টিটি	is, is not	অবজেক্ট আইডেন্টিটি
সদস্যতা	in, not in	কন্টেইনারে সদস্যতা
বুলিয়ান	and, or, not	লজিক্যাল অপারেটর
টাইপ	isinstance(), type()	টাইপ চেক
কাস্টম	__eq__, __lt__ ইত্যাদি	ক্লাসে কাস্টম তুলনা




✅ আইডেন্টিটি অপারেটর (is, is not)

✅ সদস্যতা অপারেটর (in, not in)

✅ টাইপ কম্প্যারিজন (type(), isinstance())

✅ কাস্টম কম্প্যারিজন (__eq__, __lt__ মেথড)

✅ অল এবং যেকোনো (all(), any())

✅ টার্নারি এক্সপ্রেশন

✅ functools.total_ordering

✅ ফ্লোটিং পয়েন্ট তুলনা (math.isclose())

✅ চেইন কম্প্যারিজনের বিশেষ ব্যবহার
