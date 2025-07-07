#que1--- add integre and float
a,b=2,2.5
print(type(a+b))   #4.5 type float


#que2---create string first char,last char, sub string index 2 to 5
a="vaishu"
print(a[0])  #v
print(a[5])   #u
print(a[2:5])   #ish

#que3--concatenate 2 strings
a="vaishnavi"
b="dandu"
print(a+b)    #vaishnavidandu


#que4---define list diff bw list and tuple
#list--collection of orderd hetrogenous elements,it is mutable,denotde as []
#they are comma seperated values
#tuple--denoted by (),inmutable,ordered
#we cant change any a value but we can modify total list 


#que5---list in reverse order
list1=[1,2,3,4,[5,6],'v']
print(list1[: : -1])     # ['v',[5,6],4,3,2,1]

#que6---tuple of 4 elem  print first and last elm
tup1=(1,2,3,4)
print(tup1[0])   #1
print(tup1[3])   #4

#que7---change val in tuple
tup1=(1,2,3,4)
#tup1[2]=5
print(tup1)    #  item assignment error  , we cant change a value in tuple it is inmutable


#que8--- create dict with 3 students marks
dict1={
    1:98,
    2:88,
    3:90
}
print(dict1)     # {1:98 ,2:88 ,3:90}


#que9--- access marks of 1 stud with name
dict1={
    1:98,
    'vaishu':88,
    3:90
}
print(dict1)     # {1:98 ,'vaishu':88 ,3:90}


#que10----update marks of  existing students
dict1={
    1:98,
    'vaishu':88,
    3:90
}
dict1['vaishu']=97
dict1[3]=89
print(dict1)     # {1:98 ,'vaishu':97 ,3:89}


#que11--- can i access key using value
dict1={
    1:98,
    'vaishu':88,
    3:90
}
print(dict1)    
#print(dict1[90])    # we get key error
#we cannot access key using value, we can access value using key


#que12---can i have duplicate keys and values in dict
#we cant have duplicate key in dict,key should be unique
#values can be duplicate,we can change value by using same key then the value of it will be reassigned 
#first connection be cut and second value we get



#que13--- multiples of 17 start from -34 and end below 400
print(list(range(-34,400,17)))    #-34,-17,0,17,34,51,68----391



