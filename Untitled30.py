#!/usr/bin/env python
# coding: utf-8

# 1.Add the current date to the text file today.txt as a string.

# In[1]:


import datetime


today = datetime.date.today().strftime("%Y-%m-%d")


with open("today.txt", "a") as file:
    file.write(today + "\n")


# 2. Read the text file today.txt into the string today_string

# In[2]:


with open('today.txt', 'r') as f:
    today_string = f.read()


# 3. Parse the date from today_string.

# In[3]:


import datetime

today_string = "May 1, 2023"

date_obj = datetime.datetime.strptime(today_string, '%B %d, %Y').date()

print(date_obj)


# 4. List the files in your current directory

# In[4]:


import os
current_dir = os.getcwd()
files = os.listdir(current_dir)
print(files)


# 5. Create a list of all of the files in your parent directory (minimum five files should be available).

# In[5]:


import os

parent_dir = os.path.dirname(os.getcwd()) 
files = os.listdir(parent_dir)  
print(files)


# 6. Use multiprocessing to create three separate processes. Make each one wait a random number of seconds between one and five, print the current time, and then exit.

# In[12]:


import multiprocessing
import time
import random
import datetime

def wait_and_print():
    # Generate a random wait time between 1 and 5 seconds
    wait_time = random.randint(1, 5)
    # Wait for the specified time
    time.sleep(wait_time)
    # Print the current time
    print(f"Process {multiprocessing.current_process().name} waited for {wait_time} seconds and is exiting at {datetime.datetime.now()}")

if __name__ == '__main__':
    # Create three separate processes
    p1 = multiprocessing.Process(target=wait_and_print, name='Process 1')
    p2 = multiprocessing.Process(target=wait_and_print, name='Process 2')
    p3 = multiprocessing.Process(target=wait_and_print, name='Process 3')
    # Start the processes
    p1.start()
    p2.start()
    p3.start()
    # Wait for all processes to finish
    p1.join()
    p2.join()
    p3.join()


# 7. Create a date object of your day of birth.

# In[13]:


from datetime import date

birth_year = 1998
birth_month = 12
birth_day = 18

birth_date = date(birth_year, birth_month, birth_day)
print(birth_date)


# 8. What day of the week was your day of birth?

# In[14]:


import datetime

birthdate = datetime.date(year=1998, month=12, day=18)


birthdate_str = birthdate.strftime("%Y-%m-%d")

day_of_week = birthdate.weekday()

weekday_names = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

print("My birthday ({}) was on a {}".format(birthdate_str, weekday_names[day_of_week]))


# 9. When will you be (or when were you) 10,000 days old?

# In[15]:


from datetime import datetime, timedelta

birthdate = datetime.strptime('1998-12-18', '%Y-%m-%d')

ten_thousand_days = timedelta(days=10000)
ten_thousand_days_old = birthdate + ten_thousand_days

print('You will be 10,000 days old on:', ten_thousand_days_old.strftime('%Y-%m-%d'))


# In[ ]:




