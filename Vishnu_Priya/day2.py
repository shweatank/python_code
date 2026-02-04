# f1=10
# f2=30
# tot_amt=500
# mobile=120
# tot=tot_amt//(f1+f2)
# rem=(tot%(f2+f2))
# max_fruite=tot_amt//min(f1,f2)
# max_fruite_equal=rem//min(f1,f2)
# ans=mobile-(rem%min(f1,f2))
# print("No.of he can buy",tot*2)
# print("Maximum no.of Fruite",max_fruite)
# print("Maximum no.of fruite after equal distribution",max_fruite_equal+(tot*2))
# print(ans)






# a,b,c,d=map(int,input().split())
# if a==b or a==c or a==d or b==c or b==d or c==d:
#     print("error")
# elif a>b and a>c and a>d:
#     print("a is largest")
# elif b>c and b>d:
#     print("B is largest")
# elif c>d:
#     print("C is lagest")
# else:
#     print('D is largest')


# cash=500
# f1=int(input())
# f2=int(input())
# charger=150

# qty=cash//(f1+f2)

# spent=qty*(f1+f2)
# remaining=cash-spent
# borrow=charger-remaining

# if f1<f2:
#     add_f=remaining//f1
# else:
#     add_f=remaining//min(f1,f2)

# print("Each frts quantity:",qty)
# print("Total frts:",qty*2)
# print("spent on frts:",spent)
# print("Remaining money:",remaining)

# print("Max quantity after equal: ",(qty*2)+add_f)
# print("Quantity of f1 and f2 or F2 and f1: ",qty+add_f,"and",qty)

# print("-----Afr buyingy the Fruits Equally-----")
# print("Remaining money:",remaining)
# print("borrow for charger:",borrow)





#OPERATORS:
a=4
b=2

#INT FLOAT
print(int(a)+float(b),int(a)-float(b),int(a)*float(b),int(a)//float(b))

#INT INT
print(int(a)+int(b),int(a)-int(b),int(a)*int(b),int(a)//int(b))

#FLOAT FLOAT
print(float(a)+float(b),float(a)-float(b),float(a)*float(b),float(a)//float(b))

