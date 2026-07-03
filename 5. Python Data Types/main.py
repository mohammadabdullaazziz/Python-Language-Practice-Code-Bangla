পাইথনে ডাটা টাইপ বলতে বোঝায় একটি ভেরিয়েবলে কী ধরনের তথ্য বা উপাত্ত জমা রাখা হচ্ছে তা নির্ধারণ করা পাইথন একটি Dynamically Typed প্রোগ্রামিং ভাষা, 
যার মানে হলো এখানে ভেরিয়েবল তৈরি করার সময় আলাদা করে ডাটা টাইপ বলে দিতে হয় না; ভ্যালু দেখে পাইথন নিজেই তা বুঝে নেয়। কোনো ভেরিয়েবলের ডাটা টাইপ জানতে type() ফাংশন ব্যবহার করা হয়।


📚 Python ডেটা টাইপসমূহ (সম্পূর্ণ তালিকা)


১. Numeric Types (সংখ্যা)--

টাইপ        	বিবরণ

int	         পূর্ণসংখ্যা (Integer)	  

float	       দশমিক সংখ্যা    

complex	     জটিল সংখ্যা                



২. Sequence Types (ক্রম/ধারা)---

টাইপ	          বিবরণ	                          

list	          পরিবর্তনযোগ্য সিকোয়েন্স(Mutable)	   

tuple	          অপরিবর্তনীয় সিকোয়েন্স (Immutable) 

range	          সংখ্যার ধারা (জেনারেটরের মতো)	  



৩. Mapping Type (ম্যাপিং)---

টাইপ	       বিবরণ	                      

dict	       কী-ভ্যালু জোড়ার সংগ্রহ(Mutable)	      



৪. Set Types (সেট)---


টাইপ          বিবরণ	                           

set	          ইউনিক এলিমেন্টের সংগ্রহ (Mutable)	    

frozenset	    ইউনিক এলিমেন্টের ইমিউটেবল সেট	       


৫. Boolean Type (বুলিয়ান)---

টাইপ	   বিবরণ	         

bool	   সত্য/মিথ্যা           



৬. Binary Types (বাইনারি)---

টাইপ	       বিবরণ	                 

bytes	      ইমিউটেবল বাইনারি ডেটা	   

bytearray	  মিউটেবল বাইনারি ডেটা     

memoryview	 বাইনারি ডেটার মেমোরি ভিউ   


৭. None Type (নাল)---

টাইপ     	বিবরণ	        

NoneType	 শূন্য/নাল ভ্যালু	 


৮. Text Type (টেক্সট)--

str	     টেক্সট/স্ট্রিং (Immutable)   	





🎯 FastAPI-র জন্য গুরুত্বপূর্ণ টাইপ (নোট)

✅ Must Learn (৯টি)

int	
float	      
str	        
bool	       
list	      
dict	       
set	       
Optional[type]	অপশনাল ফিল্ড
None	নাল ভ্যালু


⚠️ Good to Know (৫টি)
tuple    
bytes	     
EmailStr	   
HttpUrl	URL 
datetime	    



❌ বাদ (৪টি)
	
complex	  
bytearray	 
memoryview	
frozenset	


💡 সংক্ষিপ্ত টিপস:

প্রথমে ৯টি Must টাইপ  (int, float, str, bool, list, dict, set, Optional, None)

তারপর Pydantic স্পেশাল (EmailStr, HttpUrl, UUID, datetime)

সবশেষে Binary (bytes, bytearray) — সিকিউরিটি/ফাইল কাজে

বাদ complex, memoryview, frozenset



Mutable মানে হলো—যাকে পরিবর্তন করা যায় (Changeable)।

Immutable মানে হলো—যাকে কোনোভাবেই পরিবর্তন করা যায় না (Unchangeable)।

🛑 ১. Immutable (যা পরিবর্তন করা অসম্ভব)

যখন মেমরিতে একটি Immutable ডাটা তৈরি করা হয়, তখন সেটির ভেতরের কোনো অংশ  আর মডিফাই বা চেঞ্জ করা যায় না। যদি  জোর করে পরিবর্তন করতে চাওয়া হয়,
তবে জাভাস্ক্রিপ্ট বা পাইথন মেমরিতে সম্পূর্ণ নতুন আরেকটি ডাটা বা জায়গা তৈরি করবে, কিন্তু আগের ডাটাটি যেমন ছিল তেমনই থাকবে।

জাভাস্ক্রিপ্ট এবং পাইথনে কারা Immutable?
সব ধরণের Primitive Data Types হলো ইমিউটেবল। যেমন: Numbers, Strings, Booleans, null, undefined ইত্যাদি।

Immutable (পরিবর্তন করা যায় না)
int
float
complex
str
tuple
bool
None


🔄 ২. Mutable (যা অনায়াসে পরিবর্তন করা যায়)

মেমরিতে একটি Mutable ডাটা তৈরি করার পর, যখন খুশি তার ভেতরের কোনো অংশ বা উপাদান সরাসরি বদলে দেওয়া যায়। 
এর জন্য মেমরিতে নতুন কোনো জায়গা তৈরি হয় না, আগের জায়গাতেই ডাটা ওভাররাইট (Overwrite) হয়ে যায়।

জাভাস্ক্রিপ্ট এবং পাইথনে কারা Mutable?
সব ধরণের Non-primitive Data Types হলো মিউটেবল। যেমন: Arrays (তালিকা) এবং Objects (পাইথনে যাকে Dictionary বলে)।

Mutable (পরিবর্তন করা যায়)
List
Dictionary
Set


সংখ্যা: int, float, complex
লেখা: str
সত্য/মিথ্যা: bool
একাধিক ডেটা: list, tuple, set
Key-Value: dict
কোনো মান নেই: None



Python-এ সাধারণত এইগুলো বেশি ব্যবহার হয়:

str — text

int — পূর্ণসংখ্যা

float — দশমিক সংখ্যা

bool — True/False

list — পরিবর্তনযোগ্য sequence

tuple — অপরিবর্তনযোগ্য sequence

dict — key-value data

set — unique item-এর collection

NoneType — কোনো value নেই বোঝায়




