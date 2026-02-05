import random
mean=1437
std=527
weeklySal=[abs(round(random.normalvariate(mean, std))) for i in range(10)]
print(weeklySal)
print("----------------------------------")

    
incomeTax=[]
for i in weeklySal:
    ann=i*52
    if ann<=18200:
        tax=0
    elif ann<=45000:
        tax=0.19*(ann-18200)
    elif ann<=120000:
        tax=5092+0.325*(ann-45000)
    elif ann<=180000:
        tax=29467+0.37*(ann-120000)
    else:
        tax=51667+0.45*(ann-180000)
    incomeTax.append(round(tax))
    
print(incomeTax)
print("---------------------------------------------")

withTax=[]
for w in weeklySal:
    if w<359:
        tax=0
    else:
        tax=round(0.39*(w+0.99)-286.5965)
    withTax.append(tax)
    
print(withTax)
print("------------------------------------------------------")