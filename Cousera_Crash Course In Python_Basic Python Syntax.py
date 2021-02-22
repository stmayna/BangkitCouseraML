#!/usr/bin/env python
# coding: utf-8

# In[2]:


def convert_seconds(seconds):
    hours= seconds // 3600
    minutes= (seconds - hours*3600) // 60
    remaining_seconds= seconds - hours*3600 - minutes*60
    return hours, minutes, remaining_seconds

hours, minutes, seconds = convert_seconds(5000)
print(hours,minutes, seconds)


# In[4]:


def lucky_number(name):
    number=len(name)*9
    print("Hello "+name+". Your Lucky Number is "+str(number))
    
lucky_number("Mayna")
lucky_number("Nami")


# In[5]:


# REPLACE THIS STARTER CODE WITH YOUR FUNCTION
june_days = 30
print("June has " + str(june_days) + " days.")
july_days = 31
print("July has " + str(july_days) + " days.")


# In[7]:


def month_days(month,days):
    print(month + " has " + str(days) + " days.")
    
month_days("June","30")
month_days("July","31")


# In[8]:


def circle_area(radius):
    pi=3.14
    area=pi*(radius**2)
    print(area)
    
circle_area(5)


# In[11]:


def rectangle_area(base, height):
    area = base*height
    print("The area is " + str(area))

rectangle_area(10,6)


# In[12]:


# Complete the function to return the result of the conversion
def convert_distance(miles):
    # Convert my_trip_miles to kilometers
    km = miles * 1.6  # approximately 1.6 km in 1 mile
    # Calculate the round-trip in kilometers by doubling the result
    round_trip = km * 2
    print("The distance in kilometers is " + str(km))
    print("The round-trip in kilometers is " + str(round_trip))

convert_distance(55)


# In[13]:


# This function compares two numbers and returns them
# in increasing order.
def order_numbers(number1, number2):
    if number2 > number1:
        return number1, number2
    else:
        return number2, number1

# 1) Fill in the blanks so the print statement displays the result
#    of the function call
number1, number2 = order_numbers(100, 99)
smaller= number1
bigger= number2
print(smaller, bigger)


# In[14]:


#Let's revisit our lucky_number function. We want to change it, so that instead of printing the message, it returns the message. This way, the calling line can print the message, or do something else with it if needed. Fill in the blanks to complete the code to make it work.
def lucky_number(name):
  number = len(name) * 9
  message = "Hello " + name + ". Your lucky number is " + str(number)
  return message

message = lucky_number
print(lucky_number("Kay"))
print(lucky_number("Cameron"))


# In[2]:


def is_positive(number):
  if number > 0:
    return True
  else:
    return False

is_positive(-3)


# In[3]:


def number_group(number):
  if number>0:
    return "Positive"
  elif number==0:
    return "Zero"
  else:
    return "Negative"

print(number_group(10)) #Should be Positive
print(number_group(0)) #Should be Zero
print(number_group(-5)) #Should be Negative


# In[6]:


def check(number):
    if number > 11: 
        print(0)
    elif number != 10:
        print(1)
    elif number >= 20 or number < 12:
        print(2)
    else:
        print(3)
check(10)


# In[7]:


def sum(x, y):
    return(x+y)
print(sum(sum(1,2), sum(3,4)))


# In[9]:


def color_translator(color):
    if color == "red":
        hex_color = "#ff0000"
    elif color == "green":
        hex_color = "#00ff00"
    elif color == "blue":
        hex_color = "#0000ff"
    else:
        hex_color = "unknown"
    return hex_color

print(color_translator("blue")) # Should be #0000ff
print(color_translator("yellow")) # Should be unknown
print(color_translator("red")) # Should be #ff0000
print(color_translator("black")) # Should be unknown
print(color_translator("green")) # Should be #00ff00
print(color_translator("")) # Should be unknown


# In[10]:


def exam_grade(score):
    if (score > 95) :
        grade = "Top Score"
    elif (score >=60 and score <=95) :
        grade = "Pass"
    else:
        grade = "Fail"
    return grade

print(exam_grade(65)) # Should be Pass
print(exam_grade(55)) # Should be Fail
print(exam_grade(60)) # Should be Pass
print(exam_grade(95)) # Should be Pass
print(exam_grade(100)) # Should be Top Score
print(exam_grade(0)) # Should be Fail


# In[11]:


def format_name(first_name, last_name):
    # code goes here
    if first_name!='' and last_name!='':
        return f"Name: {last_name}, {first_name}."
    elif first_name!='' or last_name!='':
        return f"Name: {last_name}{first_name}"
    else:
        return ''

print(format_name("Ernest", "Hemingway"))
# Should return the string "Name: Hemingway, Ernest"

print(format_name("", "Madonna"))
# Should return the string "Name: Madonna"

print(format_name("Voltaire", ""))
# Should return the string "Name: Voltaire"

print(format_name("", ""))
# Should return an empty string


# In[12]:


def longest_word(word1, word2, word3):
	if len(word1) >= len(word2) and len(word1) >= len(word3):
		word = word1
	elif len(word2) >= len(word3):
		word = word2
	else:
		word = word3
	return(word)

print(longest_word("chair", "couch", "table"))
print(longest_word("bed", "bath", "beyond"))
print(longest_word("laptop", "notebook", "desktop"))


# In[13]:


def sum(x, y):
		return(x+y)
print(sum(sum(1,2), sum(3,4)))


# In[14]:


def fractional_part(numerator, denominator):
	if denominator > 0:
		return (numerator%denominator)/denominator
	return 0

print(fractional_part(5, 5)) # Should be 0
print(fractional_part(5, 4)) # Should be 0.25
print(fractional_part(5, 3)) # Should be 0.66...
print(fractional_part(5, 2)) # Should be 0.5
print(fractional_part(5, 0)) # Should be 0
print(fractional_part(0, 5)) # Should be 0


# In[ ]:




