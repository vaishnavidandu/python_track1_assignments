#1.using fun add 2 num
def sum_of_two_num(a,b):
    print(a+b)
sum_of_two_num(2,3)   #5

#2.square of num
def square_of_num(a):
    print(a**2)
square_of_num(10)   #100

#3.even or odd
def even_odd(num):
    if num%2==0:
        print("even")
    else:
        print("odd")
even_odd(2)   #even
even_odd(3)   #odd

#4.factorial of num
def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
        print(fact)
factorial(4)   #1 2 6 24
factorial(2)   #1 2

#5.max num
def greater(a,b,c):
    if a>b and a>c:
         print(a," is max")
    elif b>a and b>c:
        print(b," is max")
    else:
        print(c," is max")
greater(1,2,3)    #3 is max

#6.count vowels
def count_vowels(s):
    vowels="aeiouAEIOU"
    count=0
    for i in s:
        if i in vowels:
           count+=1
    print("no of vowels: ",count)
count_vowels("vaishu")   #3

#7. Function that takes a list and prints the sum of all elements
def sum_list(lst):
    total = 0
    for num in lst:
        total += num
    print("Sum of list:", total)
sum_list((1,2,3,4,5,9,6,8))   #38

#8.rev of string
def reverse_string(s):
    print("Reversed string:", s[::-1])
reverse_string("vaishu")  #uhsiav

#9.palindrome
def palindrome(s):
    if s == s[::-1]:
        print(s, "is a Palindrome")
    else:
        print(s, "is Not a Palindrome")
        
palindrome("mom") #palindrome
palindrome("dad") #palindrome
palindrome("bro") #not palindrome

#10.even num in list
def even_numbers(lst):
    print("Even numbers in the list:")
    for num in lst:
        if num % 2 == 0:
            print(num)
even_numbers((1,2,3,4,5,6))  #2 4 6

#11.area of circle
def area_circle(r):
    pi = 3.14
    print("Area of circle:", pi * r ** 2)
    
area_circle(3)  #28.26

#12.string len
def string_length(s):
    count = 0   
    for char in s:  
        count += 1   
    print("Length of string:", count)
string_length("vaishu")  #6

#13.avg
def average(*args):
    if len(args) == 0:  
        print("No numbers given")
    else:
        total = 0
        count = 0
        for num in args:   
            total += num
            count += 1
        avg = total / count
        print("Average:", avg)
average(10,20,30)    #20
        
    