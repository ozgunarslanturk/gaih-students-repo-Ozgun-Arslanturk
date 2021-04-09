#create a list and swap the 2nd half of the list with the first half of the list and print this list on screen.


list=["1","2","3","4","5","6"]
n=int(len(list))
list1=list[0:n//2]
list2=list[n//2:n]
print(list2 + list1)


#Ask the user to input a single digit integer to a variable 'n'.Then, print out all of the even numbers from 0 to n (including n)


n=int(input("Tek basamaklı bir tam sayı giriniz:"))
if not -10<n<10:
    print("yanlış")
elif n<=0:
    a=(range((n*-1)+1))
    b=[-i for i in a if i%2==0]
    print(b)
elif 0<=n<10:
    a=(range(n+1))
    b= [i for i in a if i%2==0]
    print(b)
else:
    print("Tek basamaklı bir tam sayı girmediniz.")
