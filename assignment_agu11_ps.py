#palindrome Bus Ticket
ticket_number=input("enter ticket num: ")
def palindrome_bus_ticket(ticket_number):
    if len(ticket_number)<1 or len(ticket_number)>10:
        return("length must contain between 1 to 10")
    elif ticket_number==ticket_number[::-1]:
        return("lucky ticket")
    else:
        return("not lucky ticket")
        
res=palindrome_bus_ticket(ticket_number)
print(res)
# palindrome_bus_ticket("121")  #lucky
# palindrome_bus_ticket("123")  #not lucky
# palindrome_bus_ticket("12345513145161")  #length must contain between 1 to 10

#sum of magic num
def sumof_magic_num():
    num1=int(input("enter num"))
    if num1<1 or num1>10**4:
        print("enter num btw 1 to 10000")
        return
    m_sum=0
    for i in range(1,num1+1):
       m_sum+=i**2
    print(m_sum)
sumof_magic_num()

#treasure hunt
def treasure_hunt():
    secret_num=20
    
    while True:
        guess_num=int(input("enter num btw 1 to 100: "))
        
        if guess_num<1 or guess_num>100:
            print("secret num must be in btw 1 and 100")
            continue
        
        if guess_num==secret_num:
            print("Treasure found")
            break
        
        else:
            print("Try Again")
        
treasure_hunt()

#perfect square 
def perfect_square_fest():
    num1=1
    while num1*num1<500:
        print(num1*num1)
        num1+=1
perfect_square_fest()

#cube challenge
def cube_challenge():
    num1=int(input("enter num: "))
    if num1<1 or num1>1000:
        print("enter num btw 1 to 10000")
        return
    for i in range(1,num1+1):
        print(i**3)
cube_challenge()
    
    
    
