#version1
x=int(input())
for i in range(1,x+1):
    if(i%3==0) and (i%5==0):
        print("fizz buzz")
    elif(i%5==0):
        print("buzz")
    elif(i%3==0):
        print("fizz")
    else:
        print(i)

#version2
x=int(input())
for i in range(1,x+1):
    if(i%3==0):
        if(i%5==0):
            print("fizz buzz")
    elif(i%5==0):
        print("buzz")
    elif(i%3==0):
        print("fizz")
    else:
        print(i)

#square pattern
x=int(input())
for i in range(x):
    for j in range(x):
        print("*",end=" ")
    print()    

#sequence pattern
x=int(input())
for i in range(x):
    for j in range(i+1):
        print("*",end=" ")
    print()    

#number pattern
x=int(input())
for i in range(x):
    for j in range(i+1):
        print(j,end=" ")
    print()    


#pyramid pattern 
x=int(input())
for i in range(x):
    for j in range(x-i-1):
        print(" ",end="")
    for j in range(i+1):
        print("*",end=" ")
    print()    

#diamond pattern
x=int(input())
for i in range(x):
    for j in range(x-i-1):
        print(" ",end="")
    for j in range(i+1):
        print("*",end=" ")
    print()
for i in range(x-2,-1,-1):
    for j in range(x-i-1):
        print(" ",end="")
    for j in range(i+1):
        print("*",end=" ")
    print()   
    
#odd pattern
x=int(input())
for i in range(x):
    for j in range(x-i-1):
        print(" ",end=" ")
    for j in range(2*i+1):
        print("*",end=" ")
    print()

#hallow square
n=int(input())
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or j==n-1:
           print("*",end=" ")
        else:
             print(" ",end=" ")
    print()
        
#hallow pyramid
n=int(input())
for i in range(n):
    for j in range(i+1):
        if i==n-1 or j==0 or i==j:
           print("*",end=" ")
        else:
             print(" ",end=" ")
    print()

#write a progam to check whether the given year is leaper or not
year=int(input())
if year%4==0 and year%100!=0:
    print("leap year")
else:
    print("not a leap year")


    #(you are given an arrey A of size N, where each element represent 
    #the numberof cupceakes sold in a single transaction. your task is 
    #to find and return an integer value representing the sum of the cupceakes
    #from the transactions where 5 or more cupceackes where sold. return 0 if 
    #there is no transaction with more than 5 cupcakes sold ?)
def cupcakes(n,arr):
 sum=0
 for i in range(n):
        if arr[i]>=5:
            sum+=arr[i]
 print(sum)
n=5
arr=[1,2,5,3,8,7]
cupcakes(n,arr)
        
#you are given two strings A,B.your task is to find and return a string representing 
#the a leftover string in A after removing al the letters that exist in string B.
# return EMPTY if the outputs does not contain any value?
def leftover(a,b):
    left=""
    remove=set(b)
    for ch in a:
        if ch not in remove:
            left+=ch
        if left:
            print(left)
        else:
            print("empty")
a="bde"
b="bde"
leftover(a,b)
        
#hallow pyramid
n=int(input())
for i in range(n):
    for j in range(n-i-1):
         print(" ",end=" ")
    for j in range(2*i+1):
        if j==0 or i==n-1 or j==2*i:
            print("*",end=" ")
        else:
            print(" ",end=" ") 
    print()


#hallow x in square
n=int(input())
for i in range (n):
    for j in range (n):
        if j==0 or i==n-1 or i==j or j==n-i-1 or j==n-1 or i==0:
            print("*",end=" ")
        else: 
            print(" ",end=" ")
    print()

#min and max values
x=list(map(int,input().split()))
min1=max1=x[0]
for i in range(1,len(x)):
    if x[i]<min1:
       min1=x[i]
    if x[i]>max1:
        max1=x[i]
print(min1,max1)

#inpalce rotations of an bytearray
x=[1,2,3,4,5]
l=0
r=len(x)-1
while l<r:
    x[l],x[r]=x[r],x[l]
    l+=1
    r-=1
print(x)

#problem 283 in leetcode
def movezeroes(nums):
    x=[]
    y=[]
    for i in range(len(nums)):
        if nums[i]==0:
            x.append(nums[i])
        else:

            #operation overload
class complex:
    def __init__(self,real,imag):
        self.real=real
        self.imag=imag
    def shownumber(self):
        print(f"{self.real}i+{self.imag}j")
    def add(self,num2):
        newreal=self.real+num2.real
        newimag=self.imag+num2.imag
        return complex(newreal ,newimag)
num1=complex(1,6)
num1.shownumber()
num3=complex(2,5)
num3.shownumber()
num4=num1.add(num3)
num4.shownumber()
    
            y.append(nums[i])
    z=y+x
    print(z)
nums=[0,1,0,3,12]
movezeroes(nums)

#recorrection
def kk(n):
    if n==5:
        return
    kk(n+1)
    print((n))
kk(1)

#fibbanoci value
def fib(n):
    a=0
    b=1
    print(a)
    print(b)
    for i in range(2,n):
        c=a+b
        a=b 
        b=c 
        print()
n=int(input())
fib(n)

#liear serch

def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:

            #Binary_search
def binary_search(arr,target):
    left=0
    right=len(arr)-1
    while left<=right:
        mid=(left+right)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            left=mid+1
        else:
            right=mid-1
    return-1
arr=[6,7,8,55]
target=55
print(binary_search(arr,target))
            return i
    return-1
arr=list(map(int,input().split(",")))
target=int(input())
print(linear_search(arr,target))


#Bubble sort
def bubble_sort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
arr=list(map(int,input().split(",")))
bubble_sort(arr)
print("sorted array:",arr)
    
#insertion_sort
def insertion_sort(arr):
    for i in range(1,len(arr)):
        start=arr[1]
        j=i-1
        while j>=0 and start<arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=start
arr=[2,6,3,1,4]
insertion_sort(arr)
print("sorted array:",arr)
