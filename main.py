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
        
