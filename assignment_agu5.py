#greater of 3 num
def greater_of_3(num1,num2,num3):
    if num1>num2 and num1>num3:
        print("num1 greater")
    elif num2>num1 and num2>num3:
        print("num2 greater")
    else:
        print("num3 is greater")
greater_of_3(3,9,1)  #num2 greater

#leap year
def leapyear(year):
    print("leap year") if (year%4==0 and year%100!=0)or(year%400==0) else print("not a leap year") 
year=int(input("enter year: "))
leapyear(year)

#vowel consonant
def vow_con(ch):
    ch=ch.lower()
    if len(ch)!=1 or not ch.isalpha():
         print("neither")
    if ch in "aeiou":
         print("vowel")
    else:
        print("consoneant")
a=input("enter char")
res=vow_con(a)
print(res)

#grade checker
def grade_checker(marks):
    if marks>=90:
        print("grade A")
    elif marks>=75 and marks<=89:
        print("grade B")
    elif marks>=60 and marks<=74:
        print("grade C")
    elif marks>=40 and marks<=59:
        print("grade D")
    else:
        print("fail")
grade_checker(56)  #d
grade_checker(30)  #fail
grade_checker(90)  #a

#triangle
def triangle_side(a,b,c):
    print("proper traingle")if a+b>c and b+c>a and c+a>b else print("not a triangle")
a=float(input("enter a side"))
b=float(input("enter a side"))
c=float(input("enter a side"))
res=triangle_side(a,b,c)
print(res)
       
   
       

