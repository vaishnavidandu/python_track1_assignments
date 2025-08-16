#prime with range
def check_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Input range
first_range= int(input("Enter starting number: "))
end_range= int(input("Enter ending number: "))

print("prime numbers between first and last range are:", first_range,end_range)
for num in range(first_range,end_range + 1):
    if check_prime(num):
        print(num)
