অপারেটর প্রিসিডেন্স হলো কোন অপারেটর আগে এক্সিকিউট হবে তার ক্রম। যখন একটি এক্সপ্রেশনে একাধিক অপারেটর থাকে, তখন পাইথন একটি নির্দিষ্ট ক্রম অনুযায়ী সেগুলো মূল্যায়ন (evaluate) করে।

# উদাহরণ
result = 10 + 5 * 2
print(result)  # 20 (5*2 আগে, তারপর 10+10)

# যদি বাম থেকে ডানে হতো: (10+5)*2 = 30
# কিন্তু পাইথন গুণকে অগ্রাধিকার দেয়

👑 পাইথনের অপারেটর অগ্রাধিকার তালিকা (সবার ওপর থেকে সবার নিচে)


প্রিসিডেন্স	        অপারেটর	                  বর্ণনা	                      উদাহরণ

১ (সর্বোচ্চ)       	()	প্যারেনথেসিস             (গ্রুপিং)          	          (2 + 3) * 4

২               	**	এক্সপোনেনশিয়েশন         (ঘাত)	                       2 ** 3

৩                	+x, -x, ~x	ইউনারী পজিটিভ, নেগেটিভ, বিটওয়াইজ NOT	      -5, ~3

৪                	*, /, //, %	গুণ, ভাগ, ফ্লোর ভাগ, মডুলাস	                 10 / 2

৫	                +, -	যোগ, বিয়োগ	                                       10 - 5

৬	              <<, >>	বিটওয়াইজ শিফট	                                 5 << 2

৭	                &	বিটওয়াইজ AND	                                         5 & 3

৮	                ^	বিটওয়াইজ XOR	                                         5 ^ 3

৯	                |	বিটওয়াইজ OR	                                           5 | 3

১০	              ==, !=, >, <, >=, <=, is, is not, in, not in	তুলনা, আইডেন্টিটি, মেম্বারশিপ	x > 5

১১	              not	লজিক্যাল NOT	not x

১২	              and	লজিক্যাল AND	x and y

১৩ (সর্বনিম্ন)	      or	লজিক্যাল OR	x or y



১: প্যারেনথেসিস () - সর্বোচ্চ প্রিসিডেন্স
প্যারেনথেসিস ব্যবহার করে প্রিসিডেন্স ওভাররাইড করা যায়।

# প্যারেনথেসিস ছাড়া
result = 10 + 5 * 2
print(result)  # 20 (গুণ আগে)

# প্যারেনথেসিস দিয়ে
result = (10 + 5) * 2
print(result)  # 30 (যোগ আগে)

# আরও উদাহরণ
print(2 * 3 + 4)      # 10 (6+4)
print(2 * (3 + 4))    # 14 (2*7)
print((2 * 3) + 4)    # 10 (6+4)

# নেস্টেড প্যারেনথেসিস
result = ((2 + 3) * (4 + 5)) / 2
print(result)  # 22.5 (5*9/2)

# ব্যাকএন্ডে ব্যবহার
age = 25
income = 50000
is_eligible = (age >= 18) and (income > 30000)
print(is_eligible)  # True




২: এক্সপোনেনশিয়েশন ** (ঘাত)

# এক্সপোনেনশিয়েশন - ডান থেকে বামে অ্যাসোসিয়েটিভ
result = 2 ** 3
print(result)  # 8 (2^3)

# ডান থেকে বামে (Right-associative)
result = 2 ** 3 ** 2
# আসলে: 2 ** (3 ** 2) = 2 ** 9 = 512
print(result)  # 512

# ভুল ধারণা: (2 ** 3) ** 2 = 8 ** 2 = 64 (হয়নি)

# ঋণাত্মক সংখ্যার ঘাত
result = -2 ** 2
# আসলে: -(2 ** 2) = -4
print(result)  # -4

# প্যারেনথেসিস দিয়ে
result = (-2) ** 2
print(result)  # 4



৩: ইউনারী অপারেটর +, -, ~

# ইউনারী পজিটিভ/নেগেটিভ
x = 5
print(+x)   # 5
print(-x)   # -5
print(-(-x))  # 5

# বিটওয়াইজ NOT (~)
x = 5  # 0101
print(~x)  # -6 (বিট উল্টানো)

# ইউনারী এবং গুণ একসাথে
result = -5 * 2
print(result)  # -10

# জটিল উদাহরণ
x = 3
y = 4
result = -x ** 2 + y
# -(3**2) + 4 = -9 + 4 = -5
print(result)  # -5



৪: গুণ, ভাগ, ফ্লোর ভাগ, মডুলাস *, /, //, %
এগুলো বাম থেকে ডানে অ্যাসোসিয়েটিভ (Left-associative)।

# গুণ ও ভাগ - সমান প্রিসিডেন্স, বাম থেকে ডানে
result = 10 / 2 * 3
# (10/2)*3 = 5*3 = 15
print(result)  # 15.0

# ভুল: 10/(2*3) = 10/6 = 1.666 (হয়নি)

# ফ্লোর ভাগ (//)
print(10 // 3)   # 3
print(-10 // 3)  # -4 (নিচের দিকে রাউন্ড)

# মডুলাস (%)
print(10 % 3)   # 1
print(-10 % 3)  # 2 (পাইথনে ভাগশেষ সবসময় ডান পাশের চিহ্ন অনুযায়ী)

# সব একসাথে
result = 10 + 5 * 2 - 4 / 2
# 10 + (5*2) - (4/2) = 10 + 10 - 2 = 18
print(result)  # 18.0

# জটিল উদাহরণ
result = 100 // 10 // 2
# (100//10)//2 = 10//2 = 5
print(result)  # 5



৫: যোগ ও বিয়োগ +, -

# যোগ-বিয়োগ - বাম থেকে ডানে
result = 10 - 5 + 3
# (10-5)+3 = 5+3 = 8
print(result)  # 8

# স্ট্রিং কনকাটেনেশন
result = "Hello" + " " + "World"
print(result)  # Hello World

# লিস্ট কনকাটেনেশন
list1 = [1, 2] + [3, 4]
print(list1)  # [1, 2, 3, 4]

# সব একসাথে
result = 10 + 5 * 2 - 3
# 10 + (5*2) - 3 = 10 + 10 - 3 = 17
print(result)  # 17


৬: বিটওয়াইজ শিফট <<, >>

# লেফট শিফট (২ দ্বারা গুণ)
x = 5  # 0101
result = x << 2  # 0101 << 2 = 10100 = 20
print(result)  # 20

# রাইট শিফট (২ দ্বারা ভাগ)
x = 20  # 10100
result = x >> 2  # 10100 >> 2 = 0101 = 5
print(result)  # 5

# শিফট এবং গুণ
result = 5 << 2 + 1
# 5 << (2+1) = 5 << 3 = 40 (যোগ আগে)
print(result)  # 40

result = (5 << 2) + 1
print(result)  # 21



৭: বিটওয়াইজ AND &

# বিটওয়াইজ AND
x = 5  # 0101
y = 3  # 0011
result = x & y  # 0001 = 1
print(result)  # 1

# শিফটের চেয়ে কম প্রিসিডেন্স
result = 5 & 3 << 2
# 5 & (3<<2) = 5 & 12 = 0101 & 1100 = 0100 = 4
print(result)  # 4

# কম্প্যারিজনের চেয়ে বেশি প্রিসিডেন্স
result = 5 & 3 == 1
# (5 & 3) == 1 = 1 == 1 = True
print(result)  # True



বিটওয়াইজ XOR ^

# বিটওয়াইজ XOR
x = 5  # 0101
y = 3  # 0011
result = x ^ y  # 0110 = 6
print(result)  # 6

# AND এর চেয়ে কম প্রিসিডেন্স
result = 5 ^ 3 & 2
# 5 ^ (3&2) = 5 ^ 2 = 0101 ^ 0010 = 0111 = 7
print(result)  # 7

# জটিল উদাহরণ
result = 5 ^ 3 | 2
# (5^3) | 2 = 6 | 2 = 0110 | 0010 = 0110 = 6
print(result)  # 6


 ৯: বিটওয়াইজ OR |

# বিটওয়াইজ OR
x = 5  # 0101
y = 3  # 0011
result = x | y  # 0111 = 7
print(result)  # 7

# XOR এর চেয়ে কম প্রিসিডেন্স
result = 5 | 3 ^ 2
# 5 | (3^2) = 5 | 1 = 0101 | 0001 = 0101 = 5
print(result)  # 5

# কম্প্যারিজনের চেয়ে বেশি
result = 5 | 3 > 2
# (5|3) > 2 = 7 > 2 = True
print(result)  # True



১০: তুলনা, আইডেন্টিটি, মেম্বারশিপ

# তুলনা অপারেটর
x = 10
y = 5
result = x > y
print(result)  # True

# চেইন কম্প্যারিজন
result = 5 < x < 15
print(result)  # True

# আইডেন্টিটি অপারেটর
a = [1, 2, 3]
b = a
result = a is b
print(result)  # True

# মেম্বারশিপ অপারেটর
fruits = ['apple', 'banana']
result = 'apple' in fruits
print(result)  # True

# লজিক্যালের চেয়ে বেশি প্রিসিডেন্স
result = 5 > 3 and 4 < 6
# (5>3) and (4<6) = True and True = True
print(result)  # True


১১: লজিক্যাল NOT not

# not - তুলনার চেয়ে কম প্রিসিডেন্স
x = True
result = not x
print(result)  # False

# not এবং কম্প্যারিজন
x = 5
y = 10
result = not x > y
# not (x>y) = not False = True
print(result)  # True

# not এবং is
value = None
result = not value is None
# not (value is None) = not True = False
print(result)  # False



 ১২: লজিক্যাল AND and

# and - শর্ট-সার্কিট ইভ্যালুয়েশন
x = 5
y = 10
result = x > 0 and y > 5
# (x>0) and (y>5) = True and True = True
print(result)  # True

# and এর সাথে not
result = not x > 0 and y > 5
# (not (x>0)) and (y>5) = False and True = False
print(result)  # False

# and ব্যবহারে শর্ট-সার্কিট
def expensive_check():
    print("Checking...")
    return True

result = False and expensive_check()  # expensive_check() কল হয় না!
print(result)  # False



১৩: লজিক্যাল OR or - সর্বনিম্ন প্রিসিডেন্স

# or - সবচেয়ে কম প্রিসিডেন্স
x = 5
y = 10
result = x > 0 or y > 5
# (x>0) or (y>5) = True or True = True
print(result)  # True

# or এবং and একসাথে
result = True or False and False
# True or (False and False) = True or False = True
print(result)  # True

# শর্ট-সার্কিট OR
def fast_check():
    print("Fast check")
    return True

result = fast_check() or expensive_check()  # expensive_check() কল হয় না!
print(result)  # True



১৪: জটিল উদাহরণ (সব একসাথে)

# জটিল এক্সপ্রেশন
result = 10 + 5 * 2 ** 3 - 4 / 2 + 3 * (4 + 2)
print(result)  # 56.0

# ধাপে ধাপে বিশ্লেষণ:
# 1. (4+2) = 6
# 2. 2**3 = 8
# 3. 5*8 = 40
# 4. 4/2 = 2
# 5. 3*6 = 18
# 6. 10 + 40 - 2 + 18 = 66
# আউটপুট: 66.0

# আরও জটিল
result = (10 + 5) * 2 ** 3 - (4 / 2 + 3) * (4 + 2)
print(result)  # 90.0

# বিশ্লেষণ:
# 1. (10+5) = 15
# 2. 2**3 = 8
# 3. 15*8 = 120
# 4. (4/2+3) = 2+3 = 5
# 5. (4+2) = 6
# 6. 5*6 = 30
# 7. 120 - 30 = 90


১৫: অ্যাসোসিয়েটিভিটি (Left vs Right)

# Left-associative (বাম থেকে ডানে)
print(10 - 5 - 2)  # (10-5)-2 = 3
print(10 / 5 / 2)  # (10/5)/2 = 1.0

# Right-associative (ডান থেকে বামে)
print(2 ** 3 ** 2)  # 2**(3**2) = 2**9 = 512

# অ্যাসাইনমেন্ট (Right-associative)
x = y = z = 10
# আসলে: x = (y = (z = 10))
print(x, y, z)  # 10 10 10




 সাধারণ ভুল ও সাবধানতা


 ১: লজিক্যাল অপারেটরের প্রিসিডেন্স

# ❌ ভুল ধারণা
x = True
y = False
z = True

result = x or y and z  # and আগে কাজ করে
# আসলে: x or (y and z) = True or False = True
print(result)  # True

# ✅ পরিষ্কার করতে প্যারেনথেসিস
result = (x or y) and z  # এখন স্পষ্ট
print(result)  # True



২: কনফিউজিং প্রিসিডেন্স

# ❌ কনফিউজিং
result = 10 + 5 * 2 ** 3 / 4
print(result)  # 20.0

# ✅ প্যারেনথেসিস দিয়ে স্পষ্ট
result = 10 + ((5 * (2 ** 3)) / 4)
print(result)  # 20.0


৩: অ্যাসাইনমেন্ট এবং কম্প্যারিজন

# ❌ ভুল
# if x = 5:  # SyntaxError!

# ✅ সঠিক
x = 5
if x == 5:
    print("x is 5")


📝 দ্রুত রেফারেন্স (চিট শিট)

# অপারেটর প্রিসিডেন্স (উচ্চ থেকে নিম্ন)

# 1. প্যারেনথেসিস
(2 + 3) * 4  # 20

# 2. ঘাত (Right-associative)
2 ** 3 ** 2  # 512

# 3. ইউনারী
-5  # -5

# 4. গুণ, ভাগ, ফ্লোর, মডুলাস
10 * 5 / 2  # 25.0

# 5. যোগ, বিয়োগ
10 + 5 - 2  # 13

# 6. বিটওয়াইজ শিফট
5 << 2  # 20

# 7. বিটওয়াইজ AND
5 & 3  # 1

# 8. বিটওয়াইজ XOR
5 ^ 3  # 6

# 9. বিটওয়াইজ OR
5 | 3  # 7

# 10. তুলনা, আইডেন্টিটি, মেম্বারশিপ
x > 5 and y < 10  # True/False

# 11. লজিক্যাল NOT
not True  # False

# 12. লজিক্যাল AND
True and False  # False

# 13. লজিক্যাল OR (সর্বনিম্ন)
True or False  # True



🎯 প্র্যাকটিস চ্যালেঞ্জ

# ১. এই কোডের আউটপুট কী হবে?
result = 10 + 5 * 2 - 4 / 2
print(result)  # ?

# ২. এই কোডের আউটপুট কী হবে?
result = 2 ** 3 ** 2
print(result)  # ?

# ৩. এই কোডের আউটপুট কী হবে?
x = True
y = False
z = True
result = x or y and z
print(result)  # ?

# ৪. প্যারেনথেসিস ব্যবহার করে ফলাফল 15 করুন
# 5 + 3 * 2 = 11
# কিভাবে 15 করবেন?

# ৫. ব্যাকএন্ড চ্যালেঞ্জ: 
# ইউজার যদি অ্যাডমিন হয় (is_admin) অথবা (মেম্বার এবং ১৮ বছরের বেশি)
# তাহলে অ্যাক্সেস দিতে হবে
is_admin = False
is_member = True
age = 20

has_access = is_admin or (is_member and age >= 18)
print(has_access)  # ?


# ১. 18.0
# 2. 512
# 3. True
# 4. (5 + 3) * 2 = 16 (নয়) 
#    5 + 3 * 2 = 11 (এটাই)
#    15 করতে: (5 + 3) * 2 - 1 = 15
#    অথবা 5 * 3 = 15
# 5. True


সর্বোচ্চ	() → ** → ইউনারী → * / // % → + -
মধ্যম	<< >> → & → ^ → | → কম্প্যারিজন
সর্বনিম্ন	not → and → or





পাইথনের প্রায় সব অপারেটর বাম থেকে ডানে (Left to Right) কাজ করে।

print(10 * 5 % 3) # Output: 2
# প্রথমে বামের গুণ: 10 * 5 = 50
# তারপর ডানের মডুলাস: 50 % 3 = 2




শুধুমাত্র পাওয়ার অপারেটর () ডান থেকে বামে (Right to Left) হিসাব করে।

print(2 ** 3 ** 2) # Output: 512
# পাইথন প্রথমে ডানের অংশ করবে: 3 ** 2 = 9
# তারপর বামের অংশ: 2 ** 9 = 512



💻 একটি অ্যাডভান্সড উদাহরণ (স্টেপ-বাই-স্টেপ সমাধান)

result = 10 + 20 / 2 > 15 and not False
print(result) # Output: True

ধাপ ১ (ভাগ): লাইনে সবার চেয়ে ক্ষমতা বেশি ভাগের (/)। তাই 20 / 2 হয়ে গেল 10.0।

লাইনটি দাঁড়ালো: 10 + 10.0 > 15 and not False

ধাপ ২ (যোগ): এবার যোগের (+) ক্ষমতা বেশি। তাই 10 + 10.0 হয়ে গেল 20.0।

লাইনটি দাঁড়ালো: 20.0 > 15 and not False



