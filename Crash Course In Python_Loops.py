#!/usr/bin/env python
# coding: utf-8

# In[1]:


#while
x = 0
while x < 5:
  print("Not there yet, x=" + str(x))
  x = x + 1
print("x=" + str(x))


# In[2]:


#while inside function
def attempts(n):
    x = 1
    while x <= n:
        print("Attempt " + str(x))
        x += 1
    print("Done")
    
attempts(7)


# In[11]:


#function behave incorrectly
#I am not sure about this
def count_down(start_number):
  current=start_number
  while (current > 0):
    print(current)
    current -= 1
  print("Zero!")

count_down(5)


# In[6]:


#fixing infinite loop
def print_range(start, end):
    # Loop through the numbers from start to end
    n = start
    while n <= end:
        print(n)
        n+=1

print_range(1, 5)  # Should print 1 2 3 4 5 (each number on its own line) 


# In[18]:


#prime factor
def print_prime_factors(number):
  # Start with two, which is the first prime
  factor = 2
  # Keep going until the factor is larger than the number
  while factor <= number:
    # Check if factor is a divisor of number
    if number % factor == 0:
      # If it is, print it and divide the original number
      print(factor)
      number = number / factor
    else:
      # If it's not, increment the factor by one
      factor+=1
  return "Done"

print_prime_factors(100)
# Should print 2,2,5,5
# DO NOT DELETE THIS COMMENT


# In[8]:


def is_power_of_two(n):
  # Check if the number can be divided by two without a remainder
  while n % 2 == 0:
    if n == 0:
      break
    n = n / 2
  # If after dividing by two the number is 1, it's a power of two
  if n == 1:
    return True
  return False
  

print(is_power_of_two(0)) # Should be False
print(is_power_of_two(1)) # Should be True
print(is_power_of_two(8)) # Should be True
print(is_power_of_two(9)) # Should be False


# In[9]:


def sum_divisors(n):
  sum = 0
  divisors = 1
  while divisors <n:
    if n == 0:
      return 0
    elif n % divisors == 0:
      sum += divisors
      divisors+=1
    else:
      divisors+=1
  # Return the sum of all divisors of n, not including n
  return sum

print(sum_divisors(0))
# 0
print(sum_divisors(3)) # Should sum of 1
# 1
print(sum_divisors(36)) # Should sum of 1+2+3+4+6+9+12+18
# 55
print(sum_divisors(102)) # Should be sum of 2+3+6+17+34+51
# 114


# In[10]:


def multiplication_table(number):
# Initialize the starting point of the multiplication table
    multiplier = 1
    # Only want to loop through 5
    while multiplier <= 5:
        result = number*multiplier
        # What is the additional condition to exit out of the loop?
        if result > 25 :
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))
        # Increment the variable for the loop
        multiplier += 1

multiplication_table(3) 
# Should print: 3x1=3 3x2=6 3x3=9 3x4=12 3x5=15

multiplication_table(5) 
# Should print: 5x1=5 5x2=10 5x3=15 5x4=20 5x5=25

multiplication_table(8)	
# Should print: 8x1=8 8x2=16 8x3=24


# In[20]:


for x in range(5):
    print(x)


# In[7]:


def square(n):
    return n*n

def sum_squares(x):
    sum = 0
    for n in range(x):
        sum += square(n)
    return sum

print(sum_squares(10)) # Should be 285
#pertama def square (n) itu kan fungsi buat menghasilkan kuadrat dari nilai n sebagai input,
#Jadi kita return n kali n,
#terus di dalem def sum_square(x) prosesnya kurang lebih begini
#1) kita tetapkan nilai sum=0
#2) kita looping dari 0 samoai x-1
#3) setiap iterasi dari looping, kita tambah nilai sum dengan square(n+1)
#4) setelah semua iterasi selesai, kita return nilai sum


# In[22]:


friends =['Mayna','Nami','Hurry','Mama','Abah']
for friend in friends:
    print("Hi "+friend)


# In[25]:


values = [23,52,59,37,48]
sum = 0 #var
length = 0 #var
for value in values:
    sum += value
    length += 1
print("Total Sum: " +str(sum)+ " - Average: " + str(sum/length))


# In[26]:


product = 1
for n in range (1,10):
    product =product * n
print(product)


# In[27]:


#factorial
def factorial(n):
    result = 1
    for i in range(1,n+1):
        result = result*i
    return result

print(factorial(4)) # should return 24
print(factorial(5)) # should return 120


# In[28]:


def to_celcius(x):
    return (x-32)*5/9

for x in range (0,101,10):
    print(x, to_celcius(x))


# In[1]:


#domino,nested

for left in range(7):
    for right in range(left,7):
        print("[" + str(left) + " | " + str(right) + "]", end=" ")
    print()


# In[2]:


# output all possible team pairings
# 1st name = home team
#2nd name = away team
# we don't wanna team play againts itself

teams = ['Dragons','Wolves','Pandas','Unicorns']
for home_team in teams:
    for away_team in teams:
        if home_team!=away_team:
            print ("The match: " + home_team + " VS " + away_team)


# In[4]:


for x in range(25):
    print(x)


# In[5]:


for x in [25]:
    print(x)


# In[16]:


def greet_friends(friends):
    for friend in friends:
        print("Hi " +friend)
        
greet_friends(['Mayna','Nami','Hurry','Abah','Mama'])
greet_friends(["Barry"]) #what's going on here, string are iterable


# In[22]:


#only want 1 element
def validate_users(users):
    for user in users:
        if len(user) >= 3 :
            print(user + " is valid")
        else:
            print(user + " is invalid")

validate_users(["purplecat"])


# In[16]:


for i in range(0,101,7):
        print(i)


# In[17]:


#factorial and print
def factorial(n):
    result = 1
    for x in range(1,n+1):
        result = result * x
    return result

for n in range(0,10):
    print(n, factorial(n+1))


# In[18]:


# first 10 cube number
for x in range(1,11):
  print(x**3)


# In[19]:


#multiples of 7 between 0 to 100
for i in range(0,101,7):
        print(i)


# In[26]:


#this program work in Cousera, but not at jupyter

# def retry(operation, attempts):
#  for n in range(attempts):
#    if operation():
#      print("Attempt " + str(n) + " succeeded")
#      break
#    else:
#      print("Attempt " + str(n) + " failed")

#retry(create_user, 3)
#retry(stop_service, 5)


# In[32]:


def factorial(n):
    print("Factorial called with: " + str(n))
    if n < 2 : #base
        print("Returning 1")
        return 1
    result = n * factorial(n-1) #recursif
    print("Returning " +str(result)+ " for factorial of: " +str(n))
    return result

factorial(4)


# In[3]:


def factorial(n):
    if n < 2 :
        return 1
    result = n * factorial(n-1) #recursif
    return result

factorial(10)


# In[4]:


#recursive template

def recursive_function(parameters):
    if base_case_condition(parameters):
        return base_case_value
    recursive_function(modified_parameters)


# In[5]:


for x in range(10):
    for y in range(x):
        print(y)


# In[6]:


for x in range(1, 10, 3):
    print(x)


# In[9]:


def even_numbers(maximum):
    return_string = " "
    for x in range (2,maximum+1,2):
        return_string += str(x) + " "
    return return_string.strip()

print(even_numbers(6))  # Should be 2 4 6
print(even_numbers(10)) # Should be 2 4 6 8 10
print(even_numbers(1))  # No numbers displayed
print(even_numbers(3))  # Should be 2
print(even_numbers(0))  # No numbers displayed


# In[10]:


def is_power_of(number, base):
  # Base case: when number is smaller than base.
  if number < base:
    # If number is equal to 1, it's a power (base**0).
    return number == 1
  result = number // base

  # Recursive case: keep dividing number by base.
  return is_power_of(result, base)

print(is_power_of(8,2)) # Should be True
print(is_power_of(64,4)) # Should be True
print(is_power_of(70,10)) # Should be False


# In[12]:


#def count_users(group):
#  count = 0
#  for member in get_members(group):
#    count += 1
#    if is_group(member):
#      count += count_users(member)-1
#  return count

#print(count_users("sales")) # Should be 3
#print(count_users("engineering")) # Should be 8
#print(count_users("everyone")) # Should be 18


# In[13]:


def sum_positive_numbers(n):
  if n==0:
    return n
  return n + sum_positive_numbers(n-1)

print(sum_positive_numbers(3)) # Should be 6
print(sum_positive_numbers(5)) # Should be 15


# In[ ]:




