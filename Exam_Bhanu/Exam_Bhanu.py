#1.

t = int(input())
for _ in range(t):
    s = input().strip()
    char_set = set()
    left = 0
    max_len = 0
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_len = max(max_len, right - left + 1)
    print(max_len)

#2.

a = int(input())
for _ in range(a):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    count = 0

    for i in range(n):
        s = 0
        for j in range(i, n):
            s += arr[j]
            if s == k:
                count += 1

    print(count)


#3.

n = int(input("Enter a Number:"))
arr = list(map(int, input().split()))
result = []
for i in range(n):
    next_greater = -1
    for j in range(i + 1, n):
        if arr[j] > arr[i]:
            next_greater = arr[j]
            break
    result.append(next_greater)
for x in result:
    print(x, end=" ")

#4.

s = input()
stack = []
balanced = True
for ch in s:
    if ch == '(' or ch == '{' or ch == '[':
        stack.append(ch)
    else:
        if len(stack) == 0:
            balanced = False
            break
        top = stack.pop()
        if (ch == ')' and top != '(') or \
          (ch == '}' and top != '{') or \
          (ch == ']' and top != '['):
            balanced = False
            break
if balanced and len(stack) == 0:
    print("YES")
else:
    print("NO")

#5

n=int(input())
a=[]
for i in range(n):
    a.append(list(map(int, input().split())))
a.sort()
k=[]
for i in a:
    if not k or i[0]>k[-1][1]:
        k.append(i)
    else:
        k[-1][1]=max(k[-1][1],i[1])
for i in k:
    print(i[0], i[1])

#7.

n=int(input())
a=[]
for i in range(n):
    a=a+list(map(int,input().split()))
b=int(input())
a.sort()
print(a[b-1])

#9.

n = int(input("Enter how many numbers:"))
arr = list(map(int, input().split()))
s = []
for i in range(n):
    s.append(arr[i])
    s.sort()
    length = len(s)
    if length % 2 == 1:
        median = s[length // 2]
    else:
        mid1 = s[length // 2 - 1]
        mid2 = s[length // 2]
        median = (mid1 + mid2) / 2
    print(float(median), end=" ")



# Normally distributed
import random
mean = 1437
std_dev = 527
salaries = []
for i in range(10):
    salary = random.gauss(mean, std_dev)
    salaries.append(round(salary, 2))
for s in salaries:
    print(s)

# income tax
weeklySalary = [500, 800, 1200, 2500]
incomeTax = []
for salary in weeklySalary:
    annualIncome = salary * 52
    if annualIncome <= 18200:
        tax = 0
    elif annualIncome <= 45000:
        tax = 0.19 * (annualIncome - 18200)
    elif annualIncome <= 120000:
        tax = 5092 + 0.325 * (annualIncome - 45000)
    else:
        tax = 29467 + 0.37 * (annualIncome - 120000)
    incomeTax.append(tax)
print(incomeTax)

# Withholding Tax
weeklySalary = int(input("Enter your weekly salary: "))
if weeklySalary < 359:
    tax = 0
else:
    x = weeklySalary + 0.99
    tax = 0.39 * x - 286.5965
print(round(tax))




