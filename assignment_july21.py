#que1--- add num to list
list1=[1,2,3,4]
num1=int(input("enter a num to add: "))
final_list=list1+[num1]
print(final_list)

#que2--find even num in list
list1=[1,2,3,4]
for i in list1:
    if i%2==0:
       print(i,"even")
       
#que3--count even and odd num from 1 to 10
even_count=0
odd_count=0
for i in range(1,11):
    if i%2==0:
        even_count+=1
    else:
        odd_count+=1
print("even_count",even_count)
print("odd_count",odd_count)


#que4---sum of digits
n=int(input("enter digit"))
sum_digit=0
for i in str(n):
    sum_digit+=int(i)
    print("sum_digit: ",sum_digit)
    
#que5----product od digit
n=int(input("enter digit"))
product_digit=1
for digit in str(n):
    product_digit *= int(digit)
    print("product_digit: ",product_digit)