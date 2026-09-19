Set কী?

পাইথনে Set হলো এমন একটি ডেটা স্ট্রাকচার, যা মূলত গণিতের 'সেট' (Set) এর ধারণার ওপর ভিত্তি করে তৈরি।

Set হলো পাইথনের একটা ডেটা টাইপ যেটা দিয়ে একাধিক জিনিস রাখা যায়, কিন্তু এর দুইটা বিশেষ বৈশিষ্ট্য আছে:

এর প্রধান দুটি জাদুকরী বৈশিষ্ট্য হলো:
১. সেটের ভেতর কোনো ডুপ্লিকেট বা একই মান দুইবার থাকতে পারে না। আপনি যদি ভুল করেও একই ডেটা বারবার রাখেন, পাইথন নিজে থেকেই ডিরেক্ট ডুপ্লিকেটগুলো মুছে ফেলবে।
২. সেটের কোনো নির্দিষ্ট ইনডেক্স বা সিরিয়াল নেই (Unordered)। তাই আপনি fruits[0] এভাবে ইনডেক্স দিয়ে কোনো আইটেম এক্সেস করতে পারবেন না।
কোনো নির্দিষ্ট ক্রম (order) থাকে না

Set তৈরি করা
Curly Bracket { } দিয়ে


fruits = {"apple", "banana", "mango"}
print(fruits)  # {'banana', 'apple', 'mango'}  -> ক্রম এলোমেলো হতে পারে

numbers = {1, 2, 3, 4, 5}
names = {"Rahim", "Karim", "Salma"}



Set তৈরি করার নিয়ম

Set লেখা হয় curly bracket { } দিয়ে (Dictionary এর মতোই দেখতে, কিন্তু ভিতরে শুধু value থাকে, key-value জোড়া না)।


⚠️ খালি Set — এখানে ভুল সবচেয়ে বেশি হয়

যদি ফাঁকা সেকেন্ড ব্র্যাকেট দিয়ে সেট বানাতে চাওয়া হয়:

empty_set = {}

তাহলে পাইথন এটিকে সেট হিসেবে ধরবে না, বরং একটি ডিকশনারি (Dictionary) হিসেবে ধরবে!

ফাঁকা সেট তৈরি করার সঠিক নিয়ম হলো set() ফাংশন ব্যবহার করা:

empty = {}
print(type(empty))   # <class 'dict'>  -> এটা Set না, Dictionary!

empty = set()
print(type(empty))   # <class 'set'>   -> সঠিক





data = {} এটি Set নয়। এটি Dictionary।

data = set()

print(type(data)) <class 'set'>

"কোনো কি-ভ্যালু পেয়ার থাকে না"

সহজ ভাষায় বলতে গেলে: ডিকশনারিতে ডেটা জমা হয় জোড়ায় জোড়ায় (Key-Value Pair), কিন্তু সেটে শুধু একা একা (Single Values) মান থাকে।

ডিকশনারির গঠন (Key-Value Pair সহ):
              
ডিকশনারিতে প্রতিটি মানের সাথে একটি করে চাবি বা কি (Key) জুড়ে দেওয়া থাকে। যেমন:

# এটি একটি ডিকশনারি (Dictionary)
student = {
    "name": "Abdullah",  # এখানে "name" হলো Key, আর "Abdullah" হলো Value
    "age": 30        # এখানে "age" হলো Key, আর 30 হলো Value
}

প্রতিটি মানের আগে একটি কোলন (:) দিয়ে তার একটি নাম বা কি (Key) দেওয়া আছে। একেই বলে Key-Value Pair (চাবি ও মানের জোড়া)।



সেটের গঠন (কোনো Key-Value Pair নেই):
           
এখন সেটের দিকে তাকান। সেটে কোনো জোড়া বা কোলন (:) থাকে না। সেখানে শুধু সরাসরি মানগুলো কমা দিয়ে বসিয়ে দেওয়া হয়:

# এটি একটি সেট (Set)
numbers = {10, 20, 30, 40}

এখানে শুধু সরাসরি সংখ্যাগুলো (10, 20, 30, 40) আছে। এদের আগে কোনো Key বা কোলন (:) নেই।



ঠিক একইভাবে স্ট্রিংয়ের সেট হতে পারে:

fruits = {"apple", "banana", "mango"}

এখানেও শুধু ফলের নামগুলো আছে, আলাদা কোনো কি-ভ্যালু জোড়া নেই।


⚠️ বিশেষ সতর্কতা (খুব গুরুত্বপূর্ণ ট্রিক):

যদি একদম ফাঁকা সেট বানাতে চাওয়া হয় , তবে ভুল করেও শুধু {} লিখা যাবে না! কারণ পাইথনে {} লিখলে সেটি সেট হিসেবে নয়,

বরং ডিকশনারি হিসেবে গণ্য হয়। ফাঁকা সেট বানাতে হয় এভাবে:

empty_set = set()  # এটি সঠিক ফাঁকা সেট
wrong_set = {}     # এটি আসলে একটি ফাঁকা ডিকশনারি (Dictionary)!


empty_set = {}

print(type(empty_set))  # <class 'dict'>  -> এটা set না, dictionary!

empty_set = set()

print(type(empty_set))  # <class 'set'>   -> সঠিক পদ্ধতি

শুধু {} লিখলে পাইথন এটাকে Dictionary ধরে নেয়, খালি Set বানাতে হলে অবশ্যই set() ফাংশন ব্যবহার করতে হবে।




List/Tuple থেকে Set তৈরি করা

my_list = [1, 2, 2, 3, 3]
my_set = set(my_list)
print(my_set)   # {1, 2, 3}




সেট আসলে কী এবং কেন এটি দরকার?

Set হলো পাইথনের এমন একটি বিল্ট-ইন ডেটা স্ট্রাকচার, যার দুটি প্রধান ও অপরিহার্য বৈশিষ্ট্য রয়েছে:

Unordered (ক্রমহীন): সেটের ভেতরের ডেটাগুলো কোনো নির্দিষ্ট ক্রমানুসারে মেমোরিতে সাজানো থাকে না। যেভাবে ডেটা রাখা হবে,
প্রিন্ট করার সময় সেটি উল্টাপাল্টা অর্ডারে আসতে পারে।

No Duplicates (ডুপ্লিকেট নিষিদ্ধ): সেটের ভেতরে কখনোই হুবহু এক ডেটা একাধিকবার থাকতে পারবে না।  যদি ভুলে একই মান ১০ বারও দেওয়া হয়, 
পাইথন নিজের বুদ্ধিমত্তায় বাকি ৯টি মুছে ফেলবে এবং শুধু ১টি রাখবে।

Set এর সবচেয়ে বড় বৈশিষ্ট্য — Duplicate নিজে থেকেই বাদ যায়

numbers = {1, 2, 2, 3, 4, 4, 5, 1}
print(numbers)  # আউটপুট: {1, 2, 3, 4, 5} (ডুপ্লিকেটগুলো নিজে থেকেই গায়েব!)

একই সংখ্যা একাধিকবার লিখলেও Set এ সেটা একবারই থাকে। এটা Set এর সবচেয়ে গুরুত্বপূর্ণ ও বেশি ব্যবহৃত বৈশিষ্ট্য।







সেট যেহেতু ইনডেক্স মেনে চলে না (যেমন: my_set[0] লিখলে এরর আসবে), তাই এর ডেটা পরিবর্তন,
যোগ বা বাদ দেওয়ার জন্য পাইথন কিছু স্পেশাল মেথড বা ফাংশন দেয়।
Index দিয়ে Access করা যায় না (কারণ Order নেই)

fruits = {"apple", "banana", "mango"}

print(fruits[0]) TypeError: 'set' object is not subscriptable

List/Tuple এর মতো Set এ index number দিয়ে item বের করা যায় না, কারণ Set এর ভিতরের item গুলোর কোনো নির্দিষ্ট ক্রম নেই — 

এলোমেলোভাবে (unordered) সংরক্ষিত থাকে। Order না থাকায় কোনো "প্রথম" বা "দ্বিতীয়" item বলে কিছু নেই।





১. সেটে নতুন উপাদান যোগ করা (add() এবং update())

লিস্টের মতো সেটেও নতুন উপাদান যোগ করা যায়, তবে এখানে .append() না বলে .add() ব্যবহার করা হয়:

add(): একটিমাত্র উপাদান সেটে যোগ করতে।

update(): একসাথে একাধিক উপাদান (যেমন: অন্য কোনো লিস্ট বা সেট) যুক্ত করতে।


fruits = {"apple", "banana"}

# ১টি উপাদান যোগ করা
fruits.add("orange")
print(fruits)  # আউটপুট: {'apple', 'orange', 'banana'} (অর্ডার এলোমেলো হতে পারে)


fruits = {"apple", "banana"}
fruits.add("mango")
print(fruits)  # {'apple', 'banana', 'mango'}

যদি আগে থেকেই থাকা মান আবার add() করা হয়, কিছুই পরিবর্তন হবে না (কারণ duplicate রাখা যায় না):
fruits.add("apple")  # কিছু হবে না, ইতিমধ্যে আছে 


colors = {"red", "green"}
colors.add("blue")

print(colors)  {'red', 'blue', 'green'}  # সিরিয়াল যেকোনোটা আগে-পিছে হতে পারে
  
---

# একাধিক উপাদান (লিস্ট বা অন্য সেট) একসাথে যোগ করা update() — একাধিক item একসাথে যোগ করা
fruits.update(["mango", "grape"])
print(fruits)


fruits = {"apple", "banana"}
fruits.update(["mango", "orange", "grape"])
print(fruits)  # {'apple', 'banana', 'mango', 'orange', 'grape'}

# প্রথমে একটি প্রাথমিক সেট তৈরি করা হলো
fruits = {"apple", "banana"}

# নতুন কিছু ফল লিস্ট আকারে একটি আলাদা ভেরিয়েবলে রাখা হলো
new_fruits = ["mango", "grape", "orange"]

# .update() মেথড দিয়ে একাধিক উপাদান একসাথে মূল সেটে যোগ করা হলো
fruits.update(new_fruits)

# আপডেট হওয়া সেটটি প্রিন্ট করা হচ্ছে
print(fruits)  {'apple', 'banana', 'mango', 'grape', 'orange'}






২. সেট থেকে উপাদান বাদ দেওয়া (remove(), discard(), pop())

remove(item): নির্দিষ্ট উপাদানটি মুছে ফেলতে। তবে উপাদানটি যদি সেটে না থাকে, তবে পাইথন KeyError বা Error দেবে।

discard(item): এটিও নির্দিষ্ট উপাদান মুছে ফেলে। তবে উপাদান সেটে না থাকলেও কোনো এরর দেয় না, চুপচাপ কোড চালিয়ে নেয়।

pop(): সেটের ভেতর থেকে র‍্যান্ডম বা যেকোনো একটি উপাদান ডিলিট করে দেয় এবং সেটি রিটার্ন করে। যেহেতু সেটের কোনো ইনডেক্স নেই,
তাই কোনটি ডিলিট হবে তা নির্দিষ্ট করে বলা যায় না।


remove() — নির্দিষ্ট মান সরানো (না থাকলে error)
remove() মেথড
কাজ কী: সেটের ভেতর থেকে নির্দিষ্ট কোনো উপাদানকে মুছে ফেলতে এটি ব্যবহার করা হয়।
বিশেষ সতর্কতা: যে উপাদানটি  মুছে ফেলতে চাওয়া হসছে সেটি যদি সেটের ভেতরে না থাকে, তবে পাইথন ক্র্যাশ করবে এবং একটি KeyError (এরর) দিবে।


fruits = {"apple", "banana", "mango"}
fruits.remove("banana")
print(fruits)  # {'apple', 'mango'}

fruits.remove("orange")  # KeyError: 'orange' -> এটা নেই তাই error


# ফলের একটি সেট
fruits = {"apple", "banana", "mango", "orange"}

# সেট থেকে "banana" মুছে ফেলা হচ্ছে
fruits.remove("banana")

print("পরে:", fruits)
# আউটপুট: {'apple', 'mango', 'orange'} (ব্যানানা সফলভাবে মুছে গেছে)

# ⚠️ সমস্যা কোথায় হয়:
# fruits.remove("grape")  # 'grape' তো সেটের ভেতরে নেই! 
# আউটপুট: KeyError: 'grape' (প্রোগ্রাম এখানে এসে আটকে বা ক্র্যাশ করবে)




discard() — নির্দিষ্ট মান সরানো (না থাকলে error দেবে না)

discard() মেথড

কাজ কী: এটিও remove() এর মতো নির্দিষ্ট কোনো উপাদানকে সেট থেকে মুছে ফেলতে ব্যবহার করা হয়।
পার্থক্য: যে উপাদানটি মুছে ফেলতে চাওয়া হসছে সেটি যদি সেটের ভেতরে না-ও থাকে, তবুও পাইথন কোনো এরর বা ঝামেলা করবে না। কোড একদম শান্তিতে পরের লাইনে চলে যাবে।

fruits = {"apple", "banana", "mango"}
fruits.discard("orange")  # কোনো error আসবে না, চুপচাপ কিছুই হবে না
print(fruits)  # {'apple', 'banana', 'mango'}

⚠️ remove() vs discard() এর পার্থক্য মনে রাখা জরুরি: item না থাকলে remove() error দেয়, কিন্তু discard() নীরবে কিছুই করে না। 
যখন নিশ্চিত না থাকো item আছে কিনা, তখন discard() ব্যবহার করা নিরাপদ।

# রঙের একটি সেট
colors = {"red", "green", "blue"}

# "green" মুছে ফেলা হলো
colors.discard("green")
print("green মুছে ফেলার পর:", colors)
# আউটপুট: {'red', 'blue'}


# এবার এমন একটি রং মুছতে চাচ্ছি যা সেটের ভেতর নেই ("yellow"):
colors.discard("yellow") 
print("yellow ডাসকার্ড করার পর:", colors)
# আউটপুট: {'red', 'blue'} (কোনো এরর দেয়নি, চুপচাপ কাজ শেষ করেছে!)





pop() — এলোমেলোভাবে একটা item সরিয়ে রিটার্ন করা

pop() মেথড

তাই পাইথনের .pop() মেথড সেট থেকে  একটি র‍্যান্ডম (অনির্দিষ্ট) উপাদানকে ডিলিট করে দেয় এবং ডিলিট হওয়া উপাদানটি রিটার্ন করে।

বিশেষ সতর্কতা: সেটের যেহেতু কোনো নির্দিষ্ট ইনডেক্স বা সিরিয়াল নেই (0, 1 নম্বর বলে কিছু নেই), 
তাই pop() কল করলে ঠিক কোন উপাদানটি মুছে যাবে তা আগে থেকে নিশ্চিত করে বলতে পারা যায় না। 
পাইথন নিজের ইচ্ছামমতো যেকোনো একটি আইটেম উড়িয়ে দেবে। তাছাড়া, সেট ফাঁকা (Empty) থাকলে এটিও এরর দিবে।

fruits = {"apple", "banana", "mango"}
removed = fruits.pop()
print(removed)  # যেকোনো একটা (কোনটা আসবে নিশ্চিত না, কারণ order নেই)
print(fruits)   # বাকি দুইটা

⚠️ List এ pop() নির্দিষ্ট index থেকে সরাতো, কিন্তু Set এ index নেই বলে pop() এলোমেলোভাবে যেকোনো একটা item সরিয়ে দেয়।

# সংখ্যার একটি সেট
numbers = {10, 20, 30, 40, 50}

# pop() কল করলে যেকোনো একটি উপাদান ডিলিট হয়ে সেটি রিমুভড ভ্যারিয়েবলে জমা হবে
removed_item = numbers.pop()

print("যে উপাদানটি মুছে গেছে:", removed_item)
print("মুছে ফেলার পর সেটটি যেমন আছে:", numbers)

# আউটপুট কেমন আসতে পারে (অর্ডার র‍্যান্ডম হওয়ায় পাল্টাতে পারে):
# যে উপাদানটি মুছে গেছে: 40 (বা অন্য যেকোনো একটি সংখ্যা)
# মুছে ফেলার পর সেটটি যেমন আছে: {10, 20, 30, 50}




# একটি সেট তৈরি করা হলো
colors = {"red", "green", "blue", "yellow"}

# .pop() ব্যবহার করে একটি র‍্যান্ডম উপাদান রিমুভ করা হলো
removed_item = colors.pop()

print(f"মুছে ফেলা উপাদানটি হলো: {removed_item}")
print(f"আপডেট হওয়া সেট: {colors}")


আউটপুট দেখতে কেমন হতে পারে?
(যেহেতু সেটের কোনো অর্ডার নেই, তাই প্রতিবার কোড চালালে ভিন্ন ভিন্ন উপাদান ডিলিট হতে পারে)

মুছে ফেলা উপাদানটি হলো: blue
আপডেট হওয়া সেট: {'red', 'green', 'yellow'}


🎯 সংক্ষেপে একনজরে পার্থক্য:

উপাদান ফিক্সড এবং সেটে থাকতেই হবে, না থাকলে কোড ভেঙে ফেলার দরকার হলে remove() ব্যবহার করতে হবে।

উপাদান ডিলিট করতে চাওয়া হলে, কিন্তু সেট না থাকলেও কোড যেন ক্র্যাশ না করে এমন নিরাপত্তা চাইলে  discard() ব্যবহার করতে হবে।

নির্দিষ্ট কোনো নাম না ধরে, শুধু র‍্যান্ডম যেকোনো একটি উপাদান সেট থেকে পপ বা হাওয়া করে দিতে চাইলে  pop() ব্যবহার  করতে হবে।





clear() হলো পাইথনের একটি বিল্ট-ইন মেথড (Method)। এর আক্ষরিক অর্থ হলো "পরিষ্কার করা" বা "সব মুছে ফেলা"।

সেটের .clear() মেথডটি খুবই সহজ এবং কাজের। এর কাজ হলো একটি সেটের ভেতরের সব উপাদান
চিরতরে মুছে ফেলা এবং সেটটিকে একটি খালি (empty) সেটে রূপান্তর করা।

# শুরুতে সেটে ৩টি ফল আছে
fruits = {"apple", "banana", "mango"}
print("আগে:", fruits)  # আউটপুট: {'apple', 'banana', 'mango'} (অর্ডার এলোমেলো হতে পারে)

# clear() মেথড কল করা হলো
fruits.clear()

# এখন প্রিন্ট করলে কী দেখা যাবে?
print("পরে:", fruits)  # আউটপুট: set()



# কিছু উপাদানসহ একটি সেট তৈরি করা হলো
permissions = {"read", "write", "execute"}

print(f"আগের সেট: {permissions}")

# .clear() মেথড ব্যবহার করে সব উপাদান মুছে ফেলা হলো
permissions.clear()

print(f"বর্তমান সেট: {permissions}")


গুরুত্বপূর্ণ পয়েন্টসমূহ:
১. পুরো সেট খালি করে দেয়: এটি একটি একটি করে উপাদান (remove() বা discard() এর মতো) ডিলিট করে না; বরং একবারে সেটের ভেତরের সমস্ত উপাদান মুছে ফেলে।
২. ভ্যারিয়েবল থাকে, শুধু ডেটা মুছে যায়: fruits নামের ব্যাগ বা ভ্যারিয়েবলটি মেমোরিতে ঠিকই বেঁচে থাকে, কিন্তু তার ভেତরের মালপত্র বা উপাদানগুলো শূন্য হয়ে যায়।
৩. আউটপুট কেমন দেখায়? কোড রান করার পর আউটপুটে set() দেখাবে, যার মানে হলো সেটটি এখন একদম ফাঁকা (Empty Set)।


.remove() বা .discard() দিয়ে একটি একটি করে উপাদান মুছতে হয়, কিন্তু .clear() দিয়ে এক ক্লিকেই পুরো সেটের সব ডেটা সাফ করে দেওয়া যায়।

ডেটা মুছে গেলেও সেট ভেরিয়েবলটি ডিলিট হয় না, বরং সেটি একটি খালি সেট (set()) হিসেবে মেমোরিতে বেঁচে থাকে।





.copy() মেথড
এই মেথডটির কাজ হলো হুবহু একই রকম আরেকটি নতুন সেট তৈরি করা (যাতে মূল সেটটি অপরিবর্তিত রেখে নতুন কপিতে পরিবর্তন করা যায়)।


# মূল সেট
original_set = {"apple", "banana", "cherry"}

# .copy() ব্যবহার করে নতুন সেট তৈরি করা হলো
copied_set = original_set.copy()

# নতুন সেটে একটি আইটেম যোগ করা হলো
copied_set.add("orange")

print(f"মূল সেট: {original_set}")
print(f"কপি করা সেট: {copied_set}")


মূল সেট: {'apple', 'banana', 'cherry'}
কপি করা সেট: {'apple', 'banana', 'cherry', 'orange'}

কপি সেটে পরিবর্তন করলেও মূল সেটটি একদম নিরাপদ ও অপরিবর্তিত থাকে।




.intersection_update() মেথড
সাধারণ .intersection() শুধু কমন উপাদানগুলো রিটার্ন করে নতুন আউটপুট দেয়,
কিন্তু .intersection_update() সরাসরি মূল সেটকেই আপডেট করে ফেলে এবং শুধু কমন উপাদানগুলো মূল সেটের ভেতরে রেখে বাকিগুলো মুছে দেয়।



# দুটি সেট
my_permissions = {"read", "write", "execute"}
allowed_permissions = {"read", "execute", "delete"}

# my_permissions-কে আপডেট করা হবে যেন শুধু কমন উপাদানগুলো থাকে
my_permissions.intersection_update(allowed_permissions)

print(f"আপডেট হওয়া পারমিশন সেট: {my_permissions}")


আপডেট হওয়া পারমিশন সেট: {'read', 'execute'}

খানে my_permissions এবং allowed_permissions এর মধ্যে কমন আইটেম ছিল শুধু "read" এবং "execute",
আর .intersection_update() কল করার কারণে মূল my_permissions সেটটি ছোট হয়ে শুধু এই দুটি উপাদানই নিজের ভেতর রেখে দিয়েছে।





.difference_update() মেথড
সাধারণ - বা .difference() অপারেটর শুধু ডিফারেন্স দেখায়, কিন্তু .intersection_update() এর মতো 
.difference_update() সরাসরি মূল সেট থেকেই অন্য সেটের উপাদানগুলো মুছে ফেলে আপডেট করে দেয়।




all_users = {"Rahim", "Karim", "Sakib", "Arman"}
banned_users = {"Karim", "Sakib"}

# all_users থেকে ব্যান হওয়া ইউজারদের বাদ দিয়ে মূল সেটটি আপডেট করা হলো
all_users.difference_update(banned_users)

print(all_users)
# আউটপুট: {'Rahim', 'Arman'} (Karim ও Sakib বাদ পড়ে গেছে)




.symmetric_difference() এবং .symmetric_difference_update()
এই মেথডটি দুটি সেটের মধ্যে যে উপাদানগুলো কমন নয় (উভয় সেটে আছে এমনগুলো বাদ দিয়ে বাকি সব ইউনিক উপাদান) সেগুলো খুঁজে বের করে।



set_a = {1, 2, 3}
set_b = {3, 4, 5}

# উভয় সেটে কমন (3) বাদ দিয়ে বাকিগুলো নিয়ে নতুন সেট বানাবে
result = set_a.symmetric_difference(set_b)
print(result)
# আউটপুট: {1, 2, 4, 5}

(আর যদি .symmetric_difference_update() ব্যবহার করা হয়, তবে এটি নতুন সেট না বানিয়ে সরাসরি মূল সেটকে আপডেট করে ফেলবে।)




.issubset() এবং .issuperset()
.issubset(): একটি সেট অন্য একটি সেটের ভেতরে পুরোপুরি আছে কিনা তা চেক করে (True বা False রিটার্ন করে)।

.issuperset(): একটি সেট অন্য সেটটির মূল বা সুপারসেট কিনা তা চেক করে।


group_a = {"apple", "banana"}
group_b = {"apple", "banana", "cherry", "mango"}

# group_a এর সব উপাদান কি group_b এ আছে?
print(group_a.issubset(group_b))  # আউটপুট: True

# group_b কি group_a কে পুরোপুরি ধারণ করে?
print(group_b.issuperset(group_a))  # আউটপুট: True





.isdisjoint() মেথড
দুটি সেটের মধ্যে একটিও উপাদান কমন আছে কি না তা চেক করতে এটি ব্যবহার করা হয়। 
যদি কোনো কমন উপাদান না থাকে, তবে এটি True রিটার্ন করে (অর্থাৎ তাদের মধ্যে কোনো মিল নেই)।

set1 = {1, 2, 3}
set2 = {4, 5, 6}

print(set1.isdisjoint(set2))
# আউটপুট: True (কারণ এই দুটি সেটের মধ্যে কোনো মিল বা কমন সংখ্যা নেই)






অ্যাডভান্সড লেভেল - গণিতের সেট থিওরি অপারেশন (Advanced Set Operations)
সেটের আসল ক্ষমতা লুকিয়ে আছে এর গণিতভিত্তিক অপারেশনগুলোর মধ্যে। ডেটা সায়েন্স বা কমপ্লেক্স লজিক হ্যান্ডেল করার সময় এগুলো পানির মতো কাজে লাগে।

.union() মেথডটি ঠিক পাইথনের ইউনিয়ন অপারেটর (|) এর মতোই কাজ করে।
দুটি বা ততোধিক সেটের সব ইউনিক উপাদানগুলোকে একসাথে মিলিয়ে একটি নতুন সেট তৈরি করাই এর কাজ (যেখানে কোনো ডুপ্লিকেট ভ্যালু থাকে না)।

python_devs = {"Rahim", "Karim", "Jabbar", "Salam"}

java_devs = {"Karim", "Salam", "Rafiq", "Baset"}

১. ইউনিয়ন বা সংযোগ সেট (union বা |)
উভয় সেটের সব মানুষগুলোকে একসাথে করতে (ডুপ্লিকেট বাদ দিয়ে)।

all_devs = python_devs.union(java_devs)
# অথবা পাইপ সাইন দিয়েও করা যায়: all_devs = python_devs | java_devs

print("সব ডেভেলপার:", all_devs)
# আউটপুট: {'Rahim', 'Karim', 'Jabbar', 'Salam', 'Rafiq', 'Baset'}


ফলের বা ফুলের নাম দিয়ে union এর উদাহরণ:

# প্রথম সেট: কিছু ফুলের নাম
summer_flowers = {"Rose", "Jasmine", "Marigold", "Sunflower"}

# দ্বিতীয় সেট: আরও কিছু ফুলের নাম (এখানে কিছু ফুল আগের সেটের সাথে মিল থাকতে পারে)
winter_flowers = {"Marigold", "Sunflower", "Tulip", "Orchid"}

# ১. union() মেথড ব্যবহার করে উভয় সেটের সমস্ত ফুল একসাথে করা (ডুপ্লিকেট বাদ দিয়ে)
all_flowers = summer_flowers.union(winter_flowers)

# অথবা পাইপ সাইন (|) ব্যবহার করেও এটি করা যায়:
# all_flowers = summer_flowers | winter_flowers

print("সব ফুল একসাথে:", all_flowers)

🔍 কোডটির ড্রাই রান ও বিশ্লেষণ:

১. summer_flowers সেটে আছে: {"Rose", "Jasmine", "Marigold", "Sunflower"}

২. winter_flowers সেটে আছে: {"Marigold", "Sunflower", "Tulip", "Orchid"}

৩. যখন আপনি union() বা | অপারেটর ব্যবহার করবেন, তখন পাইথন কী করবে?

প্রথমে প্রথম সেটের সব ফুলগুলো নেবে: Rose, Jasmine, Marigold, Sunflower

এরপর দ্বিতীয় সেটের ফুলগুলো যোগ করতে যাবে। কিন্তু দেখবে Marigold এবং Sunflower তো আগেই একবার নেওয়া হয়ে গেছে!

তাই পাইথন ওই ডুপ্লিকেট বা কমন ফুলগুলো বাদ দিয়ে শুধু নতুন ফুলগুলো (Tulip, Orchid) যুক্ত করে দেবে।

সব ফুল একসাথে: {'Rose', 'Jasmine', 'Marigold', 'Sunflower', 'Tulip', 'Orchid'}


.union() এর কোড উদাহরণ
 দুটি আলাদা সেটে দুই ক্যাটাগরির ইউজারনেম আছে। এখন চাচ্ছেন সব ইউজারকে মিলিয়ে একটি ইউনিক মাস্টার লিস্ট তৈরি করতে:

# প্রথম সেট: অ্যাডমিন ইউজারগণ
admins = {"admin_01", "super_user", "moderator"}

# দ্বিতীয় সেট: সাধারণ ইউজারগণ
regular_users = {"moderator", "john_doe", "alice_99"}

# .union() মেথড ব্যবহার করে দুটি সেট এক করা হলো
all_users = admins.union(regular_users)

print(f"সব ইউজারের তালিকা: {all_users}")

সব ইউজারের তালিকা: {'super_user', 'alice_99', 'admin_01', 'moderator', 'john_doe'}


পাইপ (|) অপারেটর দিয়ে সেট ইউনিয়ন (Union)

# প্রথম সেট: ওয়েব ডেভেলপার টিম
web_devs = {"Rahim", "Karim", "Arman"}

# দ্বিতীয় সেট: সাইবার সিকিউরিটি টিম
security_team = {"Arman", "Sakib", "Tanvir"}

# সরাসরি | অপারেটর ব্যবহার করে দুটি সেট এক করা হলো
all_members = web_devs | security_team

print(f"সকল টিম মেম্বারের তালিকা: {all_members}")

সকল টিম মেম্বারের তালিকা: {'Rahim', 'Sakib', 'Karim', 'Arman', 'Tanvir'}

এখানে "Arman" নামটি উভয় সেটের মধ্যেই ছিল, কিন্তু | অপারেটর (বা .union()) ডুপ্লিকেট বাদ দিয়ে এটিকে একবারই যুক্ত করেছে।

কোডিংয়ের সময় শর্টকাট বা পরিষ্কার সিনট্যাক্সের জন্য অনেকেই .union() লেখার পরিবর্তে এই | অপারেটরটি ব্যবহার করতে পছন্দ করে






২. ইন্টারসেকশন বা ছেদ সেট (intersection বা &)
.intersection() এবং & অপারেটর উভয়ের কাজ হলো দুটি বা ততোধিক সেটের মধ্যে কোন কোন উপাদান কমন বা মিল আছে তা খুঁজে বের করা। 
অর্থাৎ, উভয় সেটের ভেতরে যে উপাদানগুলো উপস্থিত রয়েছে, শুধু সেগুলো নিয়েই এটি একটি নতুন সেট তৈরি করে।

common_devs = python_devs.intersection(java_devs)
# অথবা এমপার্সান্ড দিয়ে: common_devs = python_devs & java_devs

print("উভয় দলে যারা আছে:", common_devs)
# আউটপুট: {'Karim', 'Salam'}



ব্যাকএন্ড স্কিল এবং সাইবার সিকিউরিটি স্কিলগুলোর মধ্যে কোন কোন স্কিল কমন আছে তা খুঁজে বের করতে:

# ব্যাকএন্ড এবং সিকিউরিটির স্কিলগুলোর সেট
backend_skills = {"Python", "Node.js", "SQL", "Docker"}
security_skills = {"Python", "Linux", "Docker", "Wireshark"}

# .intersection() মেথড ব্যবহার করে কমন স্কিল বের করা হলো
common_skills = backend_skills.intersection(security_skills)

print(f"কমন স্কিলসমূহ: {common_skills}")

কমন স্কিলসমূহ: {'Python', 'Docker'}



ফুলের নাম দিয়ে intersection এর উদাহরণ:

প্রথম বাগানে (garden_a) কিছু ফুল ফোটে।

দ্বিতীয় বাগানে (garden_b) কিছু ফুল ফোটে।
এখন আমরা দেখতে চাই যে, কোন কোন ফুল দুটি বাগানেই কমন (উভয় বাগানেই আছে)।


# প্রথম বাগান বা সেট
garden_a = {"Rose", "Jasmine", "Marigold", "Sunflower"}

# দ্বিতীয় বাগান বা সেট
garden_b = {"Marigold", "Sunflower", "Tulip", "Orchid"}

# ১. intersection() মেথড ব্যবহার করে উভয় বাগানের কমন ফুলগুলো বের করা
common_flowers = garden_a.intersection(garden_b)

# অথবা এমপার্সান্ড (&) সাইন ব্যবহার করেও এটি করা যায়:
# common_flowers = garden_a & garden_b

print("উভয় বাগানেই আছে যে ফুলগুলো:", common_flowers)


🔍 কোডটির ড্রাই রান ও বিশ্লেষণ:
১. garden_a সেটে আছে: {"Rose", "Jasmine", "Marigold", "Sunflower"}

২. garden_b সেটে আছে: {"Marigold", "Sunflower", "Tulip", "Orchid"}

৩. যখন আপনি intersection() বা & ব্যবহার করবেন, তখন পাইথন দুটো সেট মিলিয়ে দেখবে কোন ফুলগুলো উভয় দলেই উপস্থিত রয়েছে:

Rose: শুধু garden_a-তে আছে, তাই বাদ।

Jasmine: শুধু garden_a-তে আছে, তাই বাদ।

Marigold: garden_a এবং garden_b উভয় জায়গাতেই আছে! তাই এটি সিলেক্ট হলো।

Sunflower: garden_a এবং garden_b উভয় জায়গাতেই আছে! তাই এটিও সিলেক্ট হলো।

Tulip ও Orchid: শুধু garden_b-তে আছে, তাই বাদ।

উভয় বাগানেই আছে যে ফুলগুলো: {'Marigold', 'Sunflower'}


& অপারেটর দিয়ে উদাহরণ
একই কাজ খুব সহজে এবং শর্টকাটে সরাসরি & অপারেটর ব্যবহার করেও করা যাবে। কাজের দিক থেকে এটি এবং .intersection() সম্পূর্ণ এক:


# ব্যাকএন্ড এবং সিকিউরিটির স্কিলগুলোর সেট
backend_skills = {"Python", "Node.js", "SQL", "Docker"}
security_skills = {"Python", "Linux", "Docker", "Wireshark"}

# সরাসরি & অপারেটর ব্যবহার করে কমন স্কিল বের করা হলো
common_skills_op = backend_skills & security_skills

print(f"কমন স্কিলসমূহ (& অপারেটর দিয়ে): {common_skills_op}")

কমন স্কিলসমূহ (& অপারেটর দিয়ে): {'Python', 'Docker'}






পার্থক্য বা ডিফারেন্স সেট (difference বা -)
.difference() মেথড এবং মাইনাস (-) অপারেটর উভয়ের কাজ একই। এদের মূল কাজ হলো—প্রথম সেটে আছে কিন্তু দ্বিতীয় সেটে নেই,
এমন উপাদানগুলো খুঁজে বের করে একটি নতুন সেট তৈরি করা (অর্থাৎ প্রথম সেট থেকে দ্বিতীয় সেটের উপাদানগুলো বাদ বা ডিফারেন্স করে দেওয়া)।

.difference() মেথড দিয়ে উদাহরণ
ধরুন,  মোট প্রজেক্টের লিস্ট থেকে যেসব প্রজেক্ট ইতিমধ্যে শেষ হয়ে গেছে, সেগুলো বাদ দিয়ে বাকি কাজগুলোর তালিকা বের করতে

# মোট প্রজেক্টের সেট
all_projects = {"Python API", "Cyber Security Tool", "Database Design", "Web Scraper"}

# সম্পন্ন হওয়া প্রজেক্টের সেট
completed_projects = {"Database Design", "Web Scraper"}

# .difference() মেথড ব্যবহার করে বাকি প্রজেক্টগুলো বের করা হলো
remaining_projects = all_projects.difference(completed_projects)

print(f"বাকি প্রজেক্টসমূহ: {remaining_projects}")  বাকি প্রজেক্টসমূহ: {'Python API', 'Cyber Security Tool'}



- অপারেটর দিয়ে উদাহরণ
একই কাজ  সরাসরি  - অপারেটর ব্যবহার করেও খুব সহজে করা যাবে। কাজের দিক থেকে এটি এবং .difference() সম্পূর্ণ এক:

# মোট প্রজেক্টের সেট
all_projects = {"Python API", "Cyber Security Tool", "Database Design", "Web Scraper"}

# সম্পন্ন হওয়া প্রজেক্টের সেট
completed_projects = {"Database Design", "Web Scraper"}

# সরাসরি - অপারেটর ব্যবহার করে বাকি প্রজেক্টগুলো বের করা হলো
remaining_projects_op = all_projects - completed_projects

print(f"বাকি প্রজেক্টসমূহ (- অপারেটর দিয়ে): {remaining_projects_op}")



ফুলের নাম দিয়ে difference এর উদাহরণ:

প্রথম ঝুড়িতে (basket_1) কিছু ফুল আছে।

দ্বিতীয় ঝুড়িতে (basket_2) কিছু ফুল আছে।

এখন জানতে চাওয়া হসছে—প্রথম ঝুড়িতে এমন কোন ফুলগুলো আছে, যেগুলো দ্বিতীয় ঝুড়িতে একদমই নেই?

# প্রথম ঝুড়ির ফুলগুলো
basket_1 = {"Rose", "Jasmine", "Marigold", "Sunflower"}

# দ্বিতীয় ঝুড়ির ফুলগুলো
basket_2 = {"Marigold", "Sunflower", "Tulip", "Orchid"}

# ১. difference() মেথড ব্যবহার করে প্রথম ঝুড়ির একক ফুলগুলো বের করা
only_in_basket1 = basket_1.difference(basket_2)

# অথবা মাইনাস (-) সাইন ব্যবহার করেও এটি করা যায়:
# only_in_basket1 = basket_1 - basket_2

print("শুধু প্রথম ঝুড়িতে যে ফুলগুলো আছে:", only_in_basket1)


🔍 কোডটির ড্রাই রান ও বিশ্লেষণ:

১. basket_1 সেটে আছে: {"Rose", "Jasmine", "Marigold", "Sunflower"}

২. basket_2 সেটে আছে: {"Marigold", "Sunflower", "Tulip", "Orchid"}

৩. যখন আপনি basket_1.difference(basket_2) বা basket_1 - basket_2 করবেন, তখন পাইথন প্রথম ঝুড়ির প্রতিটি ফুল ধরে চেক করবে দ্বিতীয় ঝুড়িতে সেগুলো আছে কি না:

Rose: এটি কি দ্বিতীয় ঝুড়িতে আছে? না! তাই এটি রেখে দেওয়া হলো।

Jasmine: এটি কি দ্বিতীয় ঝুড়িতে আছে? না! তাই এটিও রেখে দেওয়া হলো।

Marigold: এটি কি দ্বিতীয় ঝুড়িতে আছে? হ্যাঁ আছে! তাই এটি বাদ দেওয়া হলো।

Sunflower: এটি কি দ্বিতীয় ঝুড়িতে আছে? হ্যাঁ আছে! তাই এটিও বাদ দেওয়া হলো।

শুধু প্রথম ঝুড়িতে যে ফুলগুলো আছে: {'Rose', 'Jasmine'}


- অপারেটর ব্যবহার করার জন্য উভয় পাশে অবশ্যই সেট থাকতে হয়।

পক্ষান্তরে, .difference() মেথডের ভেতরে আপনি সেট ছাড়াও অন্যান্য ডেটা (যেমন লিস্ট বা টপল) পাস করতে পারেন।





৪. সিমেট্রিক ডিফারেন্স (symmetric_difference বা ^)
যারা যেকোনো একটি দলে আছে, কিন্তু উভয় দলে নেই (কমন বাদ দিয়ে বাকি সবাই)।
সিমেট্রিক ডিফারেন্স (Symmetric Difference) সেটের একটি চমৎকার অপারেশন। সহজ বাংলায় এর অর্থ হলো—উভয় সেটের মধ্যে যেগুলো কমন (Common) বা মিল রয়েছে, 
সেগুলোকে বাদ দিয়ে বাকি সব ব্যতিক্রমী উপাদানগুলোকে একত্র করা।

unique_devs = python_devs.symmetric_difference(java_devs)
# অথবা ক্যারেট সাইন দিয়ে: unique_devs = python_devs ^ java_devs

print("একক ডেভেলপাররা:", unique_devs)
# আউটপুট: {'Rahim', 'Jabbar', 'Rafiq', 'Baset'}


ফুলের নাম দিয়ে symmetric_difference এর উদাহরণ:

ঝুড়িতে (my_basket) কিছু ফুল আছে।

বন্ধুর ঝুড়িতে (friend_basket) কিছু ফুল আছে।
এখন  জানতে চাওয়া হবে—উভয় ঝুড়ির কমন ফুলগুলো বাদ দিলে, শুধু কার ঝুড়িতে কোন কোন এক্সক্লুসিভ ফুলগুলো আলাদাভাবে আছে?

# আপনার ঝুড়ির ফুলগুলো
my_basket = {"Rose", "Jasmine", "Marigold", "Sunflower"}

# বন্ধুর ঝুড়ির ফুলগুলো
friend_basket = {"Marigold", "Sunflower", "Tulip", "Orchid"}

# ১. symmetric_difference() মেথড ব্যবহার করা
unique_flowers = my_basket.symmetric_difference(friend_basket)

# অথবা ক্যারেট (^) সাইন ব্যবহার করেও এটি করা যায়:
# unique_flowers = my_basket ^ friend_basket

print("উভয় ঝুড়ির কমন বাদে বাকি সব ফুল:", unique_flowers)


১. my_basket সেটে আছে: {"Rose", "Jasmine", "Marigold", "Sunflower"}

২. friend_basket সেটে আছে: {"Marigold", "Sunflower", "Tulip", "Orchid"}

৩. যখন আপনি symmetric_difference বা ^ ব্যবহার করবেন, তখন পাইথন ধাপে ধাপে যা করবে:

Marigold এবং Sunflower: এই দুটি ফুল উভয় ঝুড়িতেই কমন আছে। তাই পাইথন এই দুটিকে সম্পূর্ণ বাদ দিয়ে দেবে।

বাকি থাকে আপনার ঝুড়ির Rose, Jasmine এবং বন্ধুর ঝুড়ির Tulip, Orchid—এগুলো কোনো দলেই কমন নয়। পাইথন এই চারটিকে একসাথে করে একটি নতুন সেট বানিয়ে দেবে।


উভয় ঝুড়ির কমন বাদে বাকি সব ফুল: {'Rose', 'Jasmine', 'Tulip', 'Orchid'}



প্রফেশনাল লেভেল টিপস ও আন্ডার দ্য হুড মেকানিজম (Under the Hood & Performance)
কম্পিউটার সায়েন্সের ভাষায়, লিস্ট বা টিউপলে কোনো উপাদান খুঁজতে হলে পুরোটা সার্চ করতে হয় (Time Complexity: O(n))। 
কিন্তু সেট (Set) হাশ টেবিল (Hash Table) অ্যালগরিদম ব্যবহার করে তৈরি। ফলে সেটের ভেতরে কোনো উপাদান আছে কি না (in অপারেটর দিয়ে)
তা চেক করতে সুপার ফাস্ট সময় লাগে—যার টাইম কমপ্লেক্সিটি হলো O(1) (Constant Time)! 
লাখ লাখ ডেটার ভেতর থেকেও সেট মুহূর্তের মধ্যে বলে দিতে পারে ডেটাটি সেখানে আছে কি না।


চমৎকার রিয়েল-লাইফ ট্রিক: লিস্ট থেকে এক পলকে ডুপ্লিকেট তাড়ানো!
ধরা যাক, নিজের কাছে একটি লিস্ট আছে যেখানে অনেক ডুপ্লিকেট সংখ্যা আছে।এক লাইনে সব ডুপ্লিকেট মুছে ফেলতে চাওয়া হসছে:

dirty_list = [1, 2, 2, 3, 4, 4, 5, 1, 6]

# প্রথমে লিস্টকে সেটে রূপান্তর করলে ডুপ্লিকেট উড়ে যাবে, 
# তারপর আবার তাকে লিস্টে রূপান্তর করা হলো
clean_list = list(set(dirty_list))

print(clean_list)  # আউটপুট: [1, 2, 3, 4, 5, 6] (অর্ডার বদলে যেতে পারে, কিন্তু ডুপ্লিকেট ফাস!)





in দিয়ে Set এ কোনো মান আছে কিনা চেক করা

fruits = {"apple", "banana", "mango"}

print("apple" in fruits)    # True
print("orange" in fruits)   # False
একটা গুরুত্বপূর্ণ তথ্য: Set এ in দিয়ে চেক করা List এর চেয়ে অনেক দ্রুত (faster),
বিশেষ করে ডেটা বেশি থাকলে। এটাই Set এর অন্যতম বড় সুবিধা (performance এর দিক থেকে)।




দৈর্ঘ্য বের করা

fruits = {"apple", "banana", "mango"}
print(len(fruits))   # 3



for loop দিয়ে Set এর প্রতিটা item নিয়ে কাজ করা

fruits = {"apple", "banana", "mango"}

for fruit in fruits:
    print(fruit)

⚠️ প্রতিবার রান করলে আউটপুটের ক্রম ভিন্ন হতে পারে, কারণ Set এ কোনো নির্দিষ্ট order নেই।




Set এর মূল আকর্ষণ — গাণিতিক Set Operations (Mathematics এর Set Theory থেকে এসেছে)

এখানেই Set সবচেয়ে বেশি শক্তিশালী এবং ব্যবহারযোগ্য হয়ে ওঠে — গণিতের Set Theory এর মতো অপারেশন করা যায়।


Union (মিলন) — দুইটা Set এর সব unique মান একসাথে 

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

result = set1.union(set2)
print(result)  # {1, 2, 3, 4, 5, 6}

# অথবা | চিহ্ন দিয়ে
result = set1 | set2
print(result)  # {1, 2, 3, 4, 5, 6}


Intersection (ছেদ) — দুই Set এ যা কমন (উভয়ে আছে) তা বের করা

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

result = set1.intersection(set2)
print(result)  # {3, 4}

# অথবা & চিহ্ন দিয়ে
result = set1 & set2
print(result)  # {3, 4}


Difference (পার্থক্য) — একটা Set এ আছে কিন্তু অন্যটায় নেই

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

result = set1.difference(set2)
print(result)  # {1, 2}  -> set1 এ আছে কিন্তু set2 তে নেই

result2 = set2.difference(set1)
print(result2)  # {5, 6}  -> set2 তে আছে কিন্তু set1 এ নেই

# অথবা - চিহ্ন দিয়ে
result = set1 - set2
print(result)  # {1, 2}


Symmetric Difference — দুই Set এ যা কমন না (দুই দিকেই যা আলাদা)

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

result = set1.symmetric_difference(set2)
print(result)  # {1, 2, 5, 6}  -> কমন (3, 4) বাদ দিয়ে বাকি সব

# অথবা ^ চিহ্ন দিয়ে
result = set1 ^ set2
print(result)  # {1, 2, 5, 6}







Set Relationship চেক করা (Subset, Superset)


issubset() — একটা Set আরেকটা Set এর ভিতরে সম্পূর্ণ আছে কিনা

set1 = {1, 2}
set2 = {1, 2, 3, 4, 5}

print(set1.issubset(set2))   # True  -> set1 এর সবকিছু set2 তে আছে



issuperset() — একটা Set আরেকটাকে সম্পূর্ণ ধারণ করে কিনা

set1 = {1, 2, 3, 4, 5}
set2 = {1, 2}

print(set1.issuperset(set2))   # True  -> set1, set2 কে সম্পূর্ণভাবে ধারণ করছে



isdisjoint() — দুইটা Set এ একদমই কোনো কমন মান নেই কিনা

set1 = {1, 2, 3}
set2 = {4, 5, 6}

print(set1.isdisjoint(set2))   # True  -> কোনো কমন মান নেই

set3 = {3, 4, 5}
print(set1.isdisjoint(set3))   # False -> 3 কমন আছে


Set Comprehension — Advanced (এক লাইনে Set তৈরি)

List Comprehension এর মতোই, Set Comprehension আছে:

numbers = [1, 2, 2, 3, 3, 4, 5, 5]

squares = {n ** 2 for n in numbers}
print(squares)  # {16, 1, 4, 9, 25}  -> duplicate বাদ, order এলোমেলো




Frozenset — Advanced (Immutable Set)

frozenset হলো Set এর একটা immutable (অপরিবর্তনযোগ্য) ভার্সন, ঠিক যেমন List এর immutable ভার্সন হলো Tuple।

normal_set = {1, 2, 3}
frozen = frozenset([1, 2, 3])

frozen.add(4)  AttributeError: 'frozenset' object has no attribute 'add'

frozenset পরিবর্তন করা যায় না, তাই এটা Dictionary এর key হিসেবে বা আরেকটা Set এর ভিতরে item হিসেবে ব্যবহার করা যায় (কারণ Set এর item গুলোও অবশ্যই immutable হতে হবে):



Set আর List/Tuple এর মধ্যে রূপান্তর

# List → Set
my_list = [1, 2, 2, 3]
my_set = set(my_list)
print(my_set)  # {1, 2, 3}

# Set → List
my_set = {1, 2, 3}
my_list = list(my_set)
print(my_list)  # [1, 2, 3]

# String → Set (প্রতিটা আলাদা অক্ষর)
my_set = set("hello")
print(my_set)  # {'h', 'e', 'l', 'o'}  -> duplicate 'l' একবারই থাকবে



বাস্তব জীবনের ব্যবহার (Real-life Use Cases)
Duplicate ইমেইল বাদ দেওয়া

emails = ["a@gmail.com", "b@gmail.com", "a@gmail.com", "c@gmail.com"]
unique_emails = set(emails)
print(unique_emails)  # {'a@gmail.com', 'b@gmail.com', 'c@gmail.com'}


দুই গ্রুপের কমন সদস্য বের করা

math_students = {"Rahim", "Karim", "Salma"}
physics_students = {"Karim", "Fatema", "Salma"}

both_subjects = math_students & physics_students
print(both_subjects)  # {'Karim', 'Salma'}


FastAPI/backend এ Permission/Role চেক করা

user_permissions = {"read", "write"}
required_permissions = {"read", "write", "delete"}

if required_permissions.issubset(user_permissions):
    print("অনুমতি আছে")
else:
    missing = required_permissions - user_permissions
    print(f"এই অনুমতিগুলো নেই: {missing}")  # {'delete'}


  দ্রুত membership check (backend এ performance এর জন্য গুরুত্বপূর্ণ)

  blocked_users = {101, 205, 309, 412}  # অনেক ইউজার আইডি থাকতে পারে

user_id = 205
if user_id in blocked_users:   # List এর চেয়ে অনেক দ্রুত চেক হয়
    print("এই ইউজার ব্লকড")


  
