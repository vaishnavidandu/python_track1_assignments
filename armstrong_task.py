#amstrong num
num1=int(input("enter num1: "))
original_num=num1
sum=0
while num1>0:
    rem=num1%10
    sum += rem ** 3   #only for 3 digit
    num1=num1//10
print(sum)  
if sum==original_num:
    print("armstrong num")
else:
    print("not armstrong")
    
#for n digits
num1 = int(input("Enter a number: "))
original_num = num1
num_digits = len(str(original_num))

sum_val = 0
while num1 > 0:
    rem = num1 % 10
    sum_val += rem ** num_digits  
    num1 =num1// 10

if sum_val == original_num:
    print("Armstrong number")
else:
    print("Not Armstrong")
    
    
# all amstrong num in given range

num1 = int(input("Enter a number: "))
original_num = num1
num_digits = len(str(original_num))

sum_val = 0
for digit in str(num1): 
    sum_val += int(digit) ** num_digits

if sum_val == original_num:
    print("Armstrong number")
else:
    print("Not Armstrong")
    
#armstrong in for loop
num1 = int(input("Enter a number: "))
original_num = num1
num_digits = len(str(original_num))

sum_val = 0
for digit in str(num1):  
    sum_val += int(digit) ** num_digits

if sum_val == original_num:
    print("Armstrong number")
else:
    print("Not Armstrong")
    
#armstron in while loop
num1 = int(input("Enter a number: "))
original_num = num1
num_digits = len(str(original_num))

sum_val = 0
while num1 > 0:
    digit = num1 % 10
    sum_val += digit ** num_digits
    num1 //= 10

if sum_val == original_num:
    print("Armstrong number")
else:
    print("Not Armstrong")

#armstrong using function
def is_armstrong(num):
    num_digits = len(str(num))
    total = sum(int(d) ** num_digits for d in str(num))
    return total == num

num1 = int(input("Enter a number: "))
if is_armstrong(num1):
    print("Armstrong number")
else:
    print("Not Armstrong")




