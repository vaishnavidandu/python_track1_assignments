#set
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

