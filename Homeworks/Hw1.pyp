#create a list and swap the 2nd half of the list with the first half of the list and print this list on screen.


list=["1","2","3","4","5","6"]
n=int(len(list))
list1=list[0:n//2]
list2=list[n//2:n]
print(list2 + list1)
