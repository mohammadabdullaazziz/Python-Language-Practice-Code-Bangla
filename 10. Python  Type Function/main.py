পাইথনে সবকিছুই এক একটা অবজেক্ট, তাই type() ফাংশন কোনো সাধারণ টেক্সট দেয় না। সে সরাসরি ওই ডাটাটি কোন ক্লাসের অংশ, সেই ক্লাসের নাম (<class '...'>) বলে দেয়।
পাইথনে type() ফাংশনটির কাজ হলো কোনো ডেটা বা ভ্যারিয়েবলের ডাটার ধরণ (Data Type) বা শ্রেণী বের করা।

💻 সব ডেটা টাইপের কোড ও আউটপুট

# ১. Text Type (স্ট্রিং)
text_data = "Hello Python"
print(type(text_data))       # আউটপুট: <class 'str'>

# ২. Numeric Types (সংখ্যাবাচক)
int_data = 500
float_data = 99.99
complex_data = 3 + 5j
print(type(int_data))        # আউটপুট: <class 'int'>
print(type(float_data))      # আউটপুট: <class 'float'>
print(type(complex_data))    # আউটপুট: <class 'complex'>

# ৩. Boolean Type (বুলিয়ান)
bool_data = True
print(type(bool_data))       # আউটপুট: <class 'bool'>

# ৪. Sequence Types (ক্রমবাচক কালেকশন)
list_data = ["apple", "banana", 10]
tuple_data = ("red", "green", "blue")
range_data = range(5)
print(type(list_data))       # আউটপুট: <class 'list'>
print(type(tuple_data))      # আউটপুট: <class 'tuple'>
print(type(range_data))      # আউটপুট: <class 'range'>

# ৫. Mapping Type (ডিকশনারি)
dict_data = {"name": "Asif", "role": "Hacker"}
print(type(dict_data))       # আউটপুট: <class 'dict'>

# ৬. Set Types (ইউনিক সেট)
set_data = {1, 2, 3, 3, 4}   # ডুপ্লিকেট ৩ বাদ যাবে
print(type(set_data))        # আউটপুট: <class 'set'>

# ৭. None Type (খালি মান)
none_data = None
print(type(none_data))       # আউটপুট: <class 'NoneType'>

