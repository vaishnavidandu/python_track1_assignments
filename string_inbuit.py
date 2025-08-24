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

#
a=num1,num2,num3=(list(map(float,input("enter all csv format num: ").split(','))))
print(a)
#
print('how$are$you'.split('$'))

#join
list1=["1","2","3","hi"]
encoded_str=','.join(list1)
print(encoded_str)   #1,2,3,hi