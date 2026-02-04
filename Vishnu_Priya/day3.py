#discussion on the test cases on the fruite problem 
#- taking equal number of fruites
#- and when does the total amount will become 0
#---------------------------------------------------------------------------------------------
#LOOPS:

#while loops:
#starting point
#conditon 
#no. of iteration
#increament(option)
#exit condition


#write a condition to print hello world for particular no.of times:
# n=int(input())
# i=int(input())
# j=i
# while i<n+j:
#     print("Hello")
#     i+=1


# n=int(input())
# i=int(input())
# j=i
# while i<n*3+j:
#     print("hello")
#     i +=3

#n=0 i=2
#n=6 i=0
#n=6 i=6


# n=int(input())
# i=int(input())
# j=i
# x=int(input())
# while i<n*x+j:
#     print("hello")
#     i +=x

#print power of a number until less than n

# i=0
# n=int(input())
# num=0
# while num<n:
#     print(num)
#     num=i**3
#     i+=1
# import math
# a=0**3
# while a<100:
#     print(a)
#     a=int((math.cbrt(a)+1)**3)


#limited number (first few num)
# n=int(input("num: "))
# i=3
# c=0
# while c<n:
#     if (i%3==0):
#         print(i)
#         c+=1
#     i+=3 #increamenting the value




# #maximum number below 100
# print("max num")
# n=100
# i=0
# while i<=100:
#     if(i%3==0):
#         print(i)
#     i+=1




# #starting with i as input
# i=int(input("starting value:"))
# n=int(input("no.of values:"))
# c=0
# while c<n:
#     if (i%3==0):
#         print(i)
#         c+=1
#     # print("*")
#     i+=1




# solving without if statement and reduces no.of iteration 
# i=int(input("starting value:"))
# i=i+( 3 - i%3)
# n=int(input("no.of values:"))
# c=0
# while c<n:
#     print(i)
#     c+=1
#     i+=3











# #starting form i as input print untill less than 100
# i=int(input("starting value:"))
# n=int(input("max: ")) #max value
# while i<=n:
#     if (i%3==0):
#         print(i)
#     i+=1 


#printing untill the limit :


#TO DO: fibbonoci

# -----------------------------------------------------------------------------------------------------

# NESTED LOOPS:
#time complexity of the nested loops 
#works on the 2d data
#pattern logic with nested loops
# pattern N
# 

# x=1
# n=5
# while x<=n:
#     y=1
#     while y<=n:
#         print(x,y,end="  ")
#         y+=1
#     print()
#     x+=1






# x=1
# n=5
# while x<=n:
#     y=1
#     while y<=n:
#         if  y==1 or y==5 or y==x:
#             print("*",end='')
#         else:
#             print(" ",end="")
#         y+=1
#     print()
#     x+=1

# x=1
# n=5
# while x<=n:
#     y=1
#     while y<=n:
#         if  y==1 or y==5 or y==x:
#             print("*",end='')
#         else:
#             print(" ",end="")
#         y+=1
#     print()
#     x+=1

# print(end=" ")
# # pattern A
# n=5
# i=1
# while i<=n:
#     j=1
#     while j<=(n*2)-1:
#         c=n//2 +1
#         if ((i+j)==6) or abs(i-j)==4 or (i==c and j>=c and j<=2*c+1):
#             print("*",end="")
#         else:
#             print(" ",end="")
#         j+=1
#     print()
#     i+=1

# n=5
# i=1
# while i<=n:
#     j=1
#     while j<=n:
#         if j==1 or (i==1 and j<n)or (i==n and i!=j) or (j==n and i>1 and i<n):
#             print("*",end="")
#         else:
#             print(" ",end='')
#         j+=1
#     print()
#     i+=1

#TO DO: your name letters

#--------------------------------------------------------------------------------------------------------------------------------
#LIST 

#ordered seq and unordered seq:
#Ordered: list,tuple,string
#unordered: set,frozen set, dictionary
 
#---> List is a ordered group of elements
#---> ordered group of elements means the isertion order not ascending or descending 
#---> ELements in the list are enclosed with the square brackets and seperated with the commas(,)

# a=[1,2,"pytyhon",30]
# print(a)

# print(isinstance(a,int))

#----> to get the element from the list, with the help of the indexing we can acess the elements
#----> index is used to indentify the particular element in the order
#----> Index always start with 0 and diff btw any two consecutive index is 1
#----> The Max elements is the number of element in list - 1 
#----> Why do we use the Negative indexing ?




#-------------------------------------TO DO----------------------------------------------------------------------
# letter V
# n=5
# i=1
# while i<=n:
#     j=1
#     while j<=(n*2)-1:
#         if i==j or i+j==10:
#             print("*",end=' ')
#         else:
#             print("",end=' ')
#         j+=1
#     print()
#     i+=1

# Letter P
# n=5
# i=1
# while i<=n:
#     j=1
#     while j<=n:
#         if i==1 or j==1 or i==(n//2)+1 or (j==n and i<=3):
#             print("*",end='')
#         else:
#             print(" ",end='')
#         j+=1
#     print()
#     i+=1


#letter Y
# n=5
# i=1
# while i<=n:
#     j=1
#     while j<=n:
#         if (i==j and j<=(n//2)+1) or (i<=(n//2)+1 and i+j==6) or (j==(n//2+1) and i>=(n//2+1)):
#             print("*",end='')
#         else:
#             print(" ",end='')
#         j+=1
#     print()
#     i+=1


#Fibinocci sequence :

# 0 1 1 2 3 5 8 13 21


#min 8
#first five
#till a given number
#even num and odd num 
#count of no.of in fib seq

#with range:
#min 8
#first five
#till a given number
#even num and odd num 
#count of no.of in fib seq


#print the number that is less than 8 in fibinocci
# a=-1
# b=1
# i=0
# n=8
# c=0
# while c<n and i<n:
#     c=a+b
#     print(c,end=" ")
#     a,b=b,c
#     i+=1


#first five number in fibinocci sequence:
# a=-1
# b=1
# i=0
# n= 5#int(input("number of fib:"))
# c=0
# while c<n:
#     res=a+b
#     print(res,end=" ")
#     a,b=b,res
#     c+=1

#limit till the number in the fibinocci seq 



#print numbers in fibinocci in a range
# a=0
# b=1
# n=int(input("start:"))
# m=int(input("end:"))
# while a<=m:
#     if a>=n:
#         print(a)
#     a,b=b,a+b


#print few no.of fibinocci in a range:
# a=0
# b=1
# n=int(input("start:"))
# m=int(input("end:"))
# c=int(input("numbers in fibinocci:"))
# f=0
# while a<=m and f<c:
#     if a>=n:
#         print(a)
#         f=f+1
#     a,b=b,a+b

