#que1 -- what is string

#sequence of characters is called string and it is ddenoted by '' or ""
#it is a datatype to represent text and also like num,symbols,spaces
#ex:'good'

#que2 --- indexing

#giving a number to character in a string
#pos index start from 0 to n-1
#neg index start from -1 to -n
#ex: a="dog" then d=0,o=1,g=3
#negative indexing like g=-1,o=-2,d=-3

#que3 ---
text="hello"
print(text[0])  #h
print(text[4])   #o
print(text[-1])  #o

#que4 ---
name="Ajay"
print(name[0]+name[3])  #Ay
#print(name[10])  # error string index out of range bcz index is only upto 3

#que5 ---
s="Python"
print(s[0:2])   #Py
print(s[5:1])   #empty bcz indexing goes from left to right

#que6 --
s="Python"
print(s[2:-1:2])   #to

#que7 ---
a="elephant"
print(a[5:8])   #ant

#que8  ---
a="Science"
print(a[2:5])  #ien

#que9  difference bw both
s="Python"
print(s[2:5])    #tho
print(s[2:5:1])   #there is no difference op is same for both
#but s[5:10:2] in other case it work like 2 will be added to 5 the op will get of
#index num 5,7,9
