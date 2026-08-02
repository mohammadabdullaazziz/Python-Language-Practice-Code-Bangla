Python-এর if, elif, else হলো শর্তভিত্তিক সিদ্ধান্ত নেওয়ার স্টেটমেন্ট। একটি শর্ত সত্য হলে এক ধরনের কাজ হবে, আর না হলে অন্য শর্ত চেক হবে, শেষে কোনো শর্ত না মিললে else চালু হবে ।

মূল ধারণা



if প্রথম শর্ত চেক করে।

elif মানে “আরও একটা শর্ত” — আগের শর্ত false হলে এটি চেক হয়।

else সব শর্ত false হলে ডিফল্ট কাজ করে ।

if condition1:
    code1
elif condition2:
    code2
else:
    code3





elif কী?

elif এর পূর্ণরূপ Else If।

এটি তখন ব্যবহার করা হয় যখন প্রথম if শর্ত False হয়, কিন্তু আরও একটি বা একাধিক শর্ত পরীক্ষা করতে হয়।

Python উপরে থেকে নিচে একে একে শর্তগুলো পরীক্ষা করে।

যেই শর্ত প্রথম True হবে, সেই ব্লকের কোড চলবে এবং এরপরের elif বা else আর পরীক্ষা করা হবে না।





📌 মূল তিনটি অংশের কাজ:

if (যদি): প্রথম শর্ত চেক করে। এটি বাধ্যতামূলক এবং সবসময় সবার আগে থাকে।

elif (অন্যথায় যদি - Else If): প্রথম শর্ত মিথ্যা হলে পরবর্তী শর্তগুলো একটির পর একটি চেক করে। প্রয়োজন অনুযায়ী যত ইচ্ছা elif ব্যবহার করা যায়।

else (অন্যথায়): উপরের কোনো শর্তই যদি সত্য না হয়, তবে শেষ আশ্রয় হিসেবে এটি কাজ করে। এটি দেওয়া ঐচ্ছিক (Optional)।





student_marks = 75

if student_marks >= 80:
    print("Grade: A+")
elif student_marks >= 70:
    print("Grade: A")
elif student_marks >= 60:
    print("Grade: A-")
elif student_marks >= 50:
    print("Grade: B")
elif student_marks >= 40:
    print("Grade: C")
else:
    print("Grade: F (Failed)")





 num = -5

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")




ট্রাফিক সিগন্যাল কন্ট্রোল (String Method + if-elif-else)

signal_color = "RED"

# .lower() দিয়ে নিরাপদ তুলনা করা হচ্ছে
clean_signal = signal_color.lower()

if clean_signal == "red":
    print("Stop! Do not move.")
elif clean_signal == "yellow":
    print("Get ready to move or slow down.")
elif clean_signal == "green":
    print("Go ahead!")
else:
    print("Invalid signal color detected!")

Stop! Do not move.




ই-কমার্স শিপিং ফি হিসাব (লজিক্যাল অপারেটর + if-elif-else)

order_total = 1200
is_premium_member = False

if order_total >= 1000 or is_premium_member:
    print("Shipping Fee: 0 TK (Free Delivery)")
elif order_total >= 500 and not is_premium_member:
    print("Shipping Fee: 40 TK (Discounted)")
else:
    print("Shipping Fee: 80 TK (Standard Rate)")


Shipping Fee: 0 TK (Free Delivery)


⚙️ পাইথন কীভাবে এটি প্রসেস করে? (Execution Order)

পাইথন উপর থেকে নিচে নামতে থাকে এবং প্রথম True শর্তটি পাওয়া মাত্র তার ভেতরের কোড রান করে।

প্রথম True পেয়ে গেলে তার নিচের আর কোনো elif বা else পাইথন চেক করে না, বাকি পুরো ব্লকটি স্কিপ করে চলে যায়।

যদি সবকটি শর্ত False হয়, কেবল তখনই else-এর কোডটি রান করে।





month_name = input("Enter Month Name First 3 Word : ")

if month_name == "Jan":
    print("January")
elif month_name == "Feb":
    print("February")
elif month_name == "Mar":
    print("March")
elif month_name == "Apr":
    print("April")
elif month_name == "May":
    print("May")
elif month_name == "Jun":
    print("June")
elif month_name == "Jul":
    print("July")
elif month_name == "Aug":
    print("August")
elif month_name == "Sep":
    print("September")
elif month_name == "Oct":
    print("October")
elif month_name == "Nov":
    print("November")
elif month_name == "Dec":
    print("December")
else:
    print("BYE")

🚀 পদ্ধতি ২: প্রফেশনাল ও ডাইনামিক উপায় (Case-Insensitive)

উপরের ১ নম্বর উপায়ে ইউজার যদি ছোট হাতের অক্ষরে "jan" বা বড় হাতের অক্ষরে "JAN" লেখে, তবে তা কাজ করবে না, সরাসরি "BYE" চলে আসবে।

ইউজার যেন ছোট বা বড় হাতের অক্ষর যেভাবে-ই লিখুক না কেন কোডটি ঠিকঠাক কাজ করে, সেজন্য পাইথনের .title() বা .capitalize() মেথড ব্যবহার করে আরও প্রফেশনালভাবে লেখা যায়:


# .capitalize() দিয়ে প্রথম অক্ষর ক্যাপিটাল করে নেওয়া হচ্ছে (যেমন: jan -> Jan)
month_name = input("Enter Month Name First 3 Word : ").capitalize()

if month_name == "Jan":
    print("January")
elif month_name == "Feb":
    print("February")
elif month_name == "Mar":
    print("March")
elif month_name == "Apr":
    print("April")
elif month_name == "May":
    print("May")
elif month_name == "Jun":
    print("June")
elif month_name == "Jul":
    print("July")
elif month_name == "Aug":
    print("August")
elif month_name == "Sep":
    print("September")
elif month_name == "Oct":
    print("October")
elif month_name == "Nov":
    print("November")
elif month_name == "Dec":
    print("December")
else:
    print("BYE")







amount2 = 21

if amount2 == 10:
    print("Hello")
elif amount2 == 21:
    print("21")
else:
    print("No match found")





speed = 87

if speed > 90:
    print("OverSpeeding")
elif speed > 50:
    print("Normal")
else:
    print("Slow")

Normal




marks = float(input("Enter your marks: "))

if marks >= 90 and marks <= 100:
    print("Your grade is: Golden A+")
elif marks >= 80 and marks < 90:
    print("Your grade is: A+")
elif marks >= 70 and marks < 80:
    print("Your grade is: A")
elif marks >= 60 and marks < 70:
    print("Your grade is: A-")
elif marks >= 50 and marks < 60:
    print("Your grade is: B")
elif marks >= 40 and marks < 50:
    print("Your grade is: C")
elif marks >= 33 and marks < 40:
    print("Your grade is: Passed")
elif marks >= 0 and marks < 33:
    print("Your grade is: Fail")
else:
    print("Invalid Input! Please enter a number between 0 to 100.")




mark = float(input("Enter your mark: "))

if mark >= 90 and mark <= 100:
    print("Golden A+")
elif mark >= 80 and mark <= 89.999:
    print("A+")
elif mark >= 70 and mark <= 79.999:
    print("A grade")
elif mark >= 60 and mark <= 69.999:
    print("A-")
elif mark >= 50 and mark <= 59.999:
    print("B grade")
elif mark >= 40 and mark <= 49.999:
    print("C")
elif mark >= 33 and mark <= 39.999:
    print("You passed")
elif mark >= 0 and mark <= 32.999:
    print("You failed")
else:
    print("Invalid Input! Please enter a number between 0 to 100.")








marks = float(input("Enter your marks: "))

if marks > 100 or marks < 0:
    print("Invalid Input!")
elif marks >= 90:
    print("Golden A++")
elif marks >= 80:
    print("A++")
elif marks >= 70:
    print("A Grade")
elif marks >= 60:
    print("A-")
elif marks >= 50:
    print("B Grade")
elif marks >= 40:
    print("B")
elif marks >= 33:
    print("C")
else:
    print("Fail Hahahaha")


          
if marks > 100 or marks < 0:

    print("Invalid Input!") 

"যদি নম্বরের মান ১০০-এর চেয়ে বেশি হয়, অথবা নম্বরের মান ০-এর চেয়ে কম হয়—তাহলে প্রিন্ট করো: Invalid Input!"

🔍 ১. কোডের প্রতিটি অংশের অর্থ:
marks > 100: ইউজার ১০০-এর চেয়ে বেশি কিছু লিখেছে কি না (যেমন: ১০২, ১৫০)।

or: এর মানে হলো "অথবা"। অর্থাৎ or-এর বা পাশের অথবা ডান পাশের যেকোনো একটি শর্ত সত্য হলেই পুরো লাইনটি True হয়ে যাবে।

marks < 0: ইউজার ০-এর চেয়ে কম কিছু (ঋণাত্মক/Negative সংখ্যা) লিখেছে কি না (যেমন: -১, -১০)।

print("Invalid Input!"): যদি উপরে উল্লেখ করা দুটি ভুলের যেকোনো একটিও ইউজার করে ফেলে, তবে পাইথন সাথে সাথে বলবে এটি একটি ভুল ইনপুট।


❓ ২. ১০২ দিলে কেন "Invalid Input!" দেখায়?
          
পরীক্ষার সর্বোচ্চ নম্বর তো ১০০,? তাই কোনো শিক্ষার্থী কি ১০২ পেতে পারে? অবশ্যই না!প্রোগ্রামটি এভাবে ধাপে ধাপে কাজ করে:
ইনপুট : 102পাইথন প্রথম শর্তে গিয়ে চেক করল: 102 > 100  True (হ্যাঁ, ১০২ তো ১০০-এর চেয়ে বড়!)যেহেতু or-এর আগের শর্তটি সত্যি হয়ে গেছে, তাই পাইথন নিশ্চিত হয়ে গেল যে এটি একটি ভুল বা অবৈধ ইনপুট।
ফলে পাইথন নিচের কোনো গ্র্যাডিং (A+, B, C) চেক না করে সরাসরি স্ক্রিনে আউটপুট দেখিয়ে দেয়: Invalid Input!




          
user_input = input("Enter your marks: (0-100) ")

# খালি ইনপুট বা স্পেস ইনপুট ফিল্টার করা
if user_input.strip() == "":
    print("Enter a valid number")
else:
    try:
        marks = float(user_input)

        if marks >= 90 and marks <= 100:
            print("Very High")
        elif marks >= 80 and marks < 90:
            print("High Speed")
        elif marks >= 50 and marks < 80:
            print("Medium")
        elif marks >= 0 and marks < 50:
            print("Good")
        else:
            print("Invalid (0-100)")

    except ValueError:
        print("Enter a valid number")


🔍 ১. try ব্লক কী করে?
          
try শব্দের অর্থ হলো "চেষ্টা করা"।

 যে কোডটি নিয়ে সন্দেহ করা হসছে যে এটি ভুল হতে পারে (যেমন: ইউজার ভুল কিছু ইনপুট দিতে পারে), সেই কোডটিকে try-এর ভেতর রাখা হয়। পাইথন প্রথমে এই কোডটি চালিয়ে দেখার চেষ্টা করে।

🔍 ২. except ValueError কী করে?
          
except শব্দের অর্থ হলো "ব্যতিক্রম বা বিকল্প ব্যবস্থা"।

যদি try-এর ভেতরের কোডে কোনো ভুল বা এরর ঘটে (বিশেষ করে মান সংক্রান্ত ভুল বা ValueError), তবে প্রোগ্রাম বন্ধ না হয়ে সাথে সাথে লাফ দিয়ে except ValueError-এর ভেতর চলে আসে।

ValueError কখন হয়?

যখন পাইথন কোনো লেখাকে সংখ্যায় রূপান্তর করতে ব্যর্থ হয়।

যেমন: যদি float("hello") করতে চান, পাইথন অক্ষরের বদলে সংখ্যা আশা করেছিল কিন্তু অক্ষর পাওয়ায় এটি একটি ValueError দেবে।


user_input = "abc"

try:
    marks = float(user_input) # এটি ব্যর্থ হবে!
    print("Success")          # এটি চলবে না
except ValueError:
    print("ভুল ইনপুট! দয়া করে কোনো নম্বর দিন।") # ✅ প্রোগ্রাম ক্র্যাশ না করে এই লাইনটি চালাবে!

print("Hello World")          # ✅ প্রোগ্রাম স্বাভাবিকভাবে বাকি কাজ চালিয়ে যাবে!



try-except এবং except কোনো আলাদা জিনিস নয়—এরা একই ব্যবস্থার অংশ।

সহজ ভাষায়: try-except হলো পুরো পদ্ধতিটার নাম, আর except হলো সেই পদ্ধতির একটি অবিচ্ছেদ্য অংশ (Keyword)।

এদের সম্পর্ক এবং পার্থক্য বুঝতে নিচের পয়েন্টগুলো দেখুন:

🔑 ১. গঠনগত পার্থক্য:
try-except (সম্পূর্ণ ব্লক): এটি এরর হ্যান্ডেল করার পুরো কাঠামো। যেখানে try এবং except একসাথে কাজ করে। শুধু try একা বা শুধু except একা পাইথনে কখনো লেখা যায় না (সিনট্যাক্স এরর হবে)।

try (প্রথম অংশ): যেখানে মূল কোডটি লেখা হয়, যা আপনি চালিয়ে দেখার চেষ্টা করতে চান।

except (দ্বিতীয় অংশ): যদি try-এর ভেতরের কোডে কোনো সমস্যা বা এরর ঘটে, তখন পাইথন কী করবে বা কী মেসেজ দেখাবে—তা এই except-এর ভেতরে লেখা থাকে।

          
try:
    # ১. পাইথন প্রথমে এই লাইনটি চালানোর চেষ্টা করবে
    marks = float(input("Enter marks: "))
    print("Your mark is:", marks)

except:
    # ২. যদি উপরের চেষ্টা ব্যর্থ হয় (যেমন: ইউজার "abc" দিলে), 
    # তখন পাইথন লাফ দিয়ে এই except অংশে চলে আসবে
    print("Invalid Input! Please enter a number.")



💡 সংক্ষেপ কথা:try  "ঝুঁকিপূর্ণ কোডটি আগে চালিয়ে দেখার চেষ্টা করো।
"except "ভুল হলে এই বিকল্প কাজটা করো (ব্যতিক্রম সামলাও)।
"try-except দুটিকে মিলিয়ে বলা হয় "Error Handling Mechanism" বা এরর সামলানোর পুরো কৌশল।

          


  try:
    marks = float(input("Enter marks: "))
    result = 100 / marks
except Exception as e:  # যেকোনো ভুল হলেই এখানে আসবে
    print("কোথাও কোনো একটা ভুল হয়েছে!", e)



  try:
    ans = 10 / 0
except ZeroDivisionError:
    print("শূন্য দিয়ে কোনো কিছুকে ভাগ করা যায় না!")
