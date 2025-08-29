#Even digits in a number
num = 123456789
for d in str(num):
    if int(d) % 2 == 0:
        print(d)   #2 4 6 8

#Prime digits in a number
num = 245678
for d in str(num):
    if int(d) in [2, 3, 5, 7]:
        print(d)   #2 5 7
        
#using if
num=245679
while num>0:
    digit=num%10
    if digit==2 or digit==3 or digit==5 or digit==7 or digit==9:
        print(digit)
    num//=10   #9 7 5 2
    
#Product of all elements in a matrix
matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]

product = 1
for row in matrix:
    for val in row:
        product *= val

print(product)    #362880
