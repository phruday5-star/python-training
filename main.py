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
