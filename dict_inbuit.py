#dictionary----collection of key value pairs

#get----it ret value of key if exits else it ret default
#[]---it throw error so use get
d={'name':'Vaishu','age':23}
print(d.get('name'))   #Vaishu
print(d.get('class'))    #None
print(d.get('phone','n/a'))    #n/a

#keys--ret view object of dict keys
d={'a':1,'b':5}
#print(d.keys(1))   #error  takes no arg
print(list(d.keys()))   #['a', 'b']

#values----ret view of obj dict val
d={'a':1,'b':2}
print(d.values())   #dict_values([1, 2])---without changing to list
print(list(d.values()))   #[1, 2]

for i in d.keys():
    print(i,d[i])   # a 1 b 2

#items----ret a view obj of (key,val)tuples--both keys and val
d={'a':1,'b':2}
print(d.items())   #dict_items([('a', 1), ('b', 2)])
print(tuple(d.items()))   #(('a', 1), ('b', 2))
print(list(d.items()))    #[('a', 1), ('b', 2)]

for k,v in d.items():
    print(k,v)           #a 1    b 2
    
#update---update and add new key to dict with key-value pars from another dict or iterable
d={'a':1,'b':2}
d.update({'c':3})
print(d)       #{'a': 1, 'b': 2, 'c': 3}
d.update([('a',3),('b',10),('c',5)])   #{'a': 3, 'b': 10, 'c': 5}
print(d)

#pop---remove specific key and ret it val
d={'a':1,'b':2}
print(d.pop('a'))   #1
#print(d.pop('c'))  #error
print(d.pop('c','not found'))   #not found

#popitem---remove and ret last inserted item
#if not items in dict if we pop we get error
print(d.popitem())   #('b', 2)

#clear()---remove all items from dict
#it work even for empty dict 
print(d.clear())   #None
d.clear()
print(d)   #{}

#copy---ret shallow copy

org={'x':[1,2]}
shallow=org.copy()
shallow['x'].append(3)
print(org)   #{'x': [1, 2, 3]}


#fromkeys--create a new dict from keys and a common val
keys=['a','b']
new_d=dict.fromkeys(keys,0)
print(new_d)   #{'a': 0, 'b': 0}

#zip--it maps both list
keys=['a','b']
val=[1,2,3]
print(zip(keys,val))   #<zip object at 0x000001B996FDF4C0>
print(dict(zip(keys,val)))   #{'a': 1, 'b': 2}
keys1=['a','b','a','c']
val=[1,2,3]      #{'a': 3, 'b': 2} --a is assign to 1 ,b=2,a=3 so as a is duplicate it is reassigned a:3,b:2
print(dict(zip(keys1,val)))
keys2=['a','b','c']
val=[1,2]
print(dict(zip(keys,val)))   #{'a': 1, 'b': 2}----for key c there is no val so op we are getting fpr 2 keys


#shallowcopy--it share if mutable elm there then 2 will reflect
list1=[1,2,3,[2,5,3]]
list2=list1.copy()
list2[3][0]=10
print(list1)   # [1, 2, 3, [10, 5, 3]]
print(list2)   # [1, 2, 3, [10, 5, 3]]


#deepcopy----it wont share wont reflect they contain inner list
import copy
list2=[1,2,3,[2,4,5]]
list3= copy.deepcopy(list2)
list3[3][0]=1
print(list3)    # [1, 2, 3, [1, 4, 5]]
print(list2)   # [1, 2, 3, [2, 4, 5]]


