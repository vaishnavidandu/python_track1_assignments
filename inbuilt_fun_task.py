#len---to find length
list1=[1,4,2,7,8]
print(len(list1))   #5

#append--to add elem 
#but only at end , cant add multiple values---drawbacks
list2=[0,9,8,7]
list2.append(2)
print(list2)  #[0, 9, 8, 7, 2]

#extend--to add multiple elm
#but only at end--drawback
list3=[2,4,1,6,8]
list3.extend([0,9])
print(list3)   #[2, 4, 1, 6, 8, 0, 9]

#insert---to add mutp elem as well as at different positions
list4=[1,2,3,4,5]
list4.insert(1,[0,9,8])
print(list4)    #[1, [0, 9, 8], 2, 3, 4, 5]

#clear---it clear everything
list4=[1,2,3,4,5]
list4.clear()
print(list4)    #[]

#pop---which index to remove
list5=[1,2,3,[6,0],9]
list5.pop(3)
print(list5)   #[1, 2, 3, 9]

#remove--whhich elem to remove
list6=[9,2,3,4,7]
list6.remove(3)
print(list6)  #[9, 2, 4, 7]

#same remove for del same num present n no of tyms
list6=[9,4,2,3,4,7,4]
freq=list6.count(4)
for i in range(freq):
    list6.remove(4)
print(list6)    #[9, 2, 3, 7]

#index--at which index
list7=[1,2,3,4,9]
print(list7.index(1))   #0

#reverse---total rev
list8=[1,2,3,4]
list8.reverse()
print(list8)   #[4, 3, 2, 1]

#sort---in ascending
list9=[1,8,2,7]
list9.sort()
print(list9)   #[1, 2, 7, 8]

#sort---in decending
list9=[1,8,2,7]
list9.sort(reverse=True)
print(list9)   #[8, 7, 2, 1]

