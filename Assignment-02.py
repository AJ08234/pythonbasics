#!/usr/bin/env python
# coding: utf-8
# 1.What are the two values of the Boolean data type? How do you write them?
2. What are the three different types of Boolean operators?
3. Make a list of each Boolean operator's truth tables (i.e. every possible combination of Boolean values for the operator and what it evaluate ).
4. What are the values of the following expressions?
(5 > 4) and (3 == 5)
not (5 > 4)
(5 > 4) or (3 == 5)
not ((5 > 4) or (3 == 5))
(True and True) and (True == False)
(not False) or (not True)
5. What are the six comparison operators?
6. How do you tell the difference between the equal to and assignment operators?Describe a condition and when you would use one.
7. Identify the three blocks in this code:
spam = 0
if spam == 10:
print('eggs')
if spam > 5:
print('bacon')
else:
print('ham')
print('spam')
print('spam')
8. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints Greetings! if anything else is stored in spam.


9.If your programme is stuck in an endless loop, what keys you’ll press?
10. How can you tell the difference between break and continue?
11. In a for loop, what is the difference between range(10), range(0, 10), and range(0, 10, 1)?
12. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent program that prints the numbers 1 to 10 using a while loop.
13. If you had a function named bacon() inside a module named spam, how would you call it after importing spam?
# 1.What are the two values of the Boolean data type? How do you write them?

1.True
2.False

Boolean data types are True and false.and We can write using First Letter with capital of T and F# 2. What are the three different types of Boolean operators?

There are three different types of Boolean operators,
1.and 
2.or
3.not# 3. Make a list of each Boolean operator's truth tables (i.e. every possible combination of Boolean values for the operator and what it evaluate ).

Truth Table for AND
A B output
0 0 0 
0 1 0
1 0 0
1 1 1

Truth Table for OR
A B output
0 0 0
0 1 1
1 0 1
1 1 1

Truth Table for NOT
A output
0 1
1 0
4. What are the values of the following expressions?
(5 > 4) and (3 == 5)
not (5 > 4)
(5 > 4) or (3 == 5)
not ((5 > 4) or (3 == 5))
(True and True) and (True == False)
(not False) or (not True)

Answer:
    
False
False
True
False
False
True5. What are the six comparison operators?

Answer:
    ==, !=, <, >, <=, and >=
    6. How do you tell the difference between the equal to and assignment operators?
   Describe a condition and when you would use one.

Answer:
    == is the equal to operator that compares two values and evaluates to a Boolean,
    while = is the assignment operator that stores a value in a variable.
# In[10]:


#Example
# Equal to operator

if(3==7):
    print("True")
else:
    print("False")
    
 #Assignment Operator

A=1  #Here I have used assignment operator
print("A=",A)

7. #Identify the three blocks in this code:
# In[12]:



spam = 0
if spam == 10:
    print('eggs') #Block1 
if spam > 5:
    print('bacon') #Block2
else:
    print('ham')
    print('spam')
    print('spam') #Block3

8. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints Greetings! if anything else is stored in spam.
# In[8]:


spam=int(input("Enter the number"))
if spam==1:
    print("spam")
elif spam==2:
    print("Howdy")
else:
    print("Greeting!")

9.If your programme is stuck in an endless loop, what keys you’ll press?Answer:
    If My Program is stuck in an endless loop,Ctrl+C keys will be used10. How can you tell the difference between break and continue?Answer:
    The Break pass will stop the execution of the code and just after the loop
    The Continue pass will continue the iteration one by one interation until it compelets.11. In a for loop, what is the difference between range(10), range(0, 10), and range(0, 10, 1)?
# In[15]:


for i in range(10):
    print(i)
print("........................")
for i in range(0,10):
    print(i)
print("........................")
for i in range(0,10,1):
    print(i)

From the above output we can conclude that they all do the same thing. The range(10) call ranges from 0 up to (but not including) 10, range(0, 10) tells the loop to start at 0, and range(0, 10, 1) tells the loop to increase the variable by 1 on each iteration.12. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent program that prints the numbers 1 to 10 using a while loop.
# In[17]:


#Use of For Loop
print("For Loop")
for i in range(1,11):
    print(i)
#Use of While Loop
print("While Loop")
a =1
while a <= 10:
    print(a)
    a+=1

13. If you had a function named bacon() inside a module named spam, how would you call it after importing spam?Answer: spam.bacon() would be call it after importing spam
