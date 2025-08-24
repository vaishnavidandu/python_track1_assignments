#string----mutable and inmutable
#when we assign only once if we want to replace  the we cant replace it in middle 
#replace also can make diff

#case-conversions-builtin fun
#lower,upper,islower,isupper,swapcase,len,captlize
#len,count,index----for list and string common

#lower---to convert from upper to lower
a="VAISHU"
print(a.lower())    #vaishu

#upper----to convert from lower to upper
a="vaishu"
print(a.upper())   #VAISHU

#isupper---to check uppercase letter
a="Vaishu"
print(a.isupper())   #False

#isupper---to check lowercase letter
a="vaishu"
print(a.islower())   #True

#swapcase---change upper to lower lower to upper
a="VAishu"
print(a.swapcase())    #vaISHU

#captilise--only 1st letter of 1st word change to capital
#after space it wont change of every word---drawback
#to overcome that we use title
a="vaishnavi dandu"
print(a.capitalize())   #Vaishnavi dandu

#tittle----only 1st letter for every word after spaces capital
a="vaishnavi dandu"
print(a.title())   #Vaishnavi Dandu

#trimming and replacing builtin fun
#strip,rstrip,lstrip,replace

#strip--to remove extra spaces
#assign then print
a="      vaishnavi    "
a=a.strip()
print(a)    #vaishnavi

#rstrip -----to remove space from right
a="      vaishnavi    "
a=a.lstrip()
print(a)   #vaishnavi      

#lstrip--to remove space from left
a="      vaishnavi    "
a=a.rstrip()
print(a)   #      vaishnavi 

#replace---to replace old val with new value
#replace(old,"new")
#if we replace the word with other word which is not there in given string it wont give error
#but it just run the code without any op and error
a="vaishnavi"   
a=a.replace("vaishnavi","dandu")
print(a)   #dandu

a="vaishnavi is"   
a=a.replace("dandu","dandu")
print(a)    #vaishnavi is

#find---where the elm is present in which index
str1="vaishu"
print(str1.find('s'))   #3

#startswith---we get true or false if the word starts with same
str1="vaishu"
print(str1.startswith('v'))   #True
print(str1.startswith('V'))    #False

#endswith---we get true or false if the word starts with same
str1="vaishu"
print(str1.endswith('shu'))   #True
print(str1.endswith('u'))    #True

#split---it split each elem
num1=input("enter nums: ")
print(num1.split(','))   #['2', '3', '4', '5']

#if we use it without map it convert into list
#input("enter all csv format num: ").split(',')  ----list
#(map(float,input("enter all csv format num: ").split(',')))----we get map object wont get output
#(list(map(float,input("enter all csv format num: ").split(','))))-----we get output
a=num1,num2,num3=(list(map(float,input("enter all csv format num: ").split(','))))
print(a)
#
print('how$are$you'.split('$'))

#join
list1=["1","2","3","hi"]
encoded_str=','.join(list1)
print(encoded_str)   #1,2,3,hi


#set---collection of unordered finite unique
#1.add----to add elem into set
a={1,2,3}
a.add(10)
print(a)  #{10, 1, 2, 3}

#2.remove
#in remove if we give elem from outside we get error
#
a={1,2,3}
a.remove(1)
print(a)   #{2, 3}

#3.discard
#if we give elm from outside also it print same input but wont give error
a={1,2,3}
a.discard(10)
print(a)   #{1, 2, 3}

#4.pop----which index to del
a={1,2,3}
print(a.pop())  #1
print(a)    #{2, 3}

#5.clear----remove everything
a={1,2,3}
print(a.clear())  #none
a.clear()
print(a)   #set()

#6.union---combine both sets
a={1,2,3}
b={10,11,12}
print(a.union(b))   #{1, 2, 3, 10, 11, 12}

#7.difference
#if a-b we get a elem which are not in b
#if b-a we get b elm which are not in a
a={1,2,3}
b={1,2,10,11,12}
print(a.difference(b))   #{3}
print(b.difference(a))   #{10, 11, 12}

#intersection----common elem from both
a={1,2,3}
b={1,2,10,11,12}
print(a.intersection(b))    #{1, 2}

#symmetric_difference----which are same that elem we wont get
a={1,2,3}
b={1,2,10,11,12}
print(a.symmetric_difference(b))    #{3, 10, 11, 12}

#isdisjoint---no common elm we get true or false
a={1,2,3}
b={1,2,3,10,11,12}
print(a.isdisjoint(b))   #False
a={1,2,3}
b={4,5,6}
print(a.isdisjoint(b))   #True

#map---map(function,iterable)
def  square(x):
    return x**2
print(list(map(square,[2,3,4])))   #[4, 9, 16]



