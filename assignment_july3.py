# que1 -- hrs,min,seconds 
 
total_sec=8000
hrs=total_sec//3600
min=(total_sec%3600)//60
sec=total_sec%60
print(hrs,"hr",min,"min",sec,"s")  # 2hr 13min 20s

# que2 -- totalcost

p1,p2=100,50
q1,q2=2,3
total=(p1*q1)+(p2*q2)
tax=(total*(18/100))
finalamount=total+tax
print(finalamount)     #413

#que3    -- perimeter and area of circle

r=5
pi=3.14
perimeter=2*pi*r
area=pi*r*r
print(area) #78.5
print(perimeter) #31.4

#que4 --- temp- farrenheit

c=28
f=(c*9/5)+32
print(f)  # 82.4

#que5 

#complied lang - code to compiler to executable file
#pros - code privacy,faster  con- not portable,1st step is slow 
#interpreted lan - code to interpreter line by line exec
#pros - portable,easy debug  con- no code privacy,slow,must contain interpeter
#hybrid - mix up of both compiler and interpreter ex:python
#code-complier-bytecode-interpretur  both code privacy and portable 


#que6--

# python code can be executed in various ways
#1. idle --we can write a code but atoumatic execution is dn -- not a good approch to use
#2. notepad--write code in that and save by ctrl+s by .py extension
# then open file manger and see the folder
# and go to path and remove it and type cmd then promt will open
# then write python filename.py the code will be executed
# 3.vs code- in extensions install python then create a folder and then in that file.py
# next write the code in file then click on run button the code is exceuted
# or if no exetension go to teminal and execute with crt path and 
# use commonds like cd for sub folder and cd .. for parent folder  
