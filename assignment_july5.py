#que1 --- what is datatype
# Structure in which data is organised is called datatype

#que2--- types of datatype
#1.Numeric datatype:integer,float,complex
#2.Boolean : True or False     3==3(T),2==3(F)
#3.Sequence: string,list,tuple,range
#4.set:
#5.None

#que3--- diff bw mutable and immutable
#Mutable:where we can make changes ex:list,set
#imutable:we cannot make changes ex:tuple,String


#que4 -- diff bw int,float,complex
#int:integer defines a number ex:a=5  print(type(a))#int
#float:any num after decimal point indicate as float ex:2.3 even in division by defaut we get output as float
#complex:m+nj m:real num and j is imaginary num


#que5 --- 
#string str is a datatpe used to represent text in python 
#not only text string contain num,symbols etc


#que6 ----
print(type(521))   #int
print(type("521"))  #str


#que7 --- diff bw tuple,list,set
# 1 list: ordered collection of hetrogenous elements denoted as[]
#it is mutable,we can index and slice in list and can change data,del,add
# 2 tuple: denotde as ()
#it is inmutable,orderded,index and slice can be done but cant update,del,change elements
# 3 set: denoted as {}
#it is mutable, unordered, we can add,del,



#que8--- diff dictinary and list
#dictinary: {} data is in key value pair form
#key should be unique,values can be cahnged or repeated
#list: []
#ordered,mutable,can change data

#que9 ---
#float is the default datatype of a number with decimal point


#que10---
age=10   #int
marks=93.5   #float
name="vaishnavi"   #str
z=2+3j   #complex


#que11---  type functions
a=2
b='vaishu'
c=9.3
print(type(a))  #int
print(type(b))   #str
print(type(c))  #float


#que12---
a=1
b="v"
#print(b+a)   #error bcz adding is not possible only concadination is possible


#que13 ---
x=[1,2,3]
y=(1,2,3)
z={1,2,3}
print(type(x),type(y),type(z))   # list,tuple,set


#que14---
#we cant change a value in tuple bcz it is immutable 
#we cant delete,update,add anything once tuple is declared


#que15 ---
#yes reasssignment is possible in inmutable datatypes
#bcz in inmutable do add,del will work so if a=1 in intial
#then a=5 then a refer to 5 next tym and cut the connection from 1




