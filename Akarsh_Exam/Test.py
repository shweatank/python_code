'''

#--------------sec-A------------------------------
#Q1:Longest Substring Without Repeating Characters

s=input().strip()
max_len=0
curr=""
for char in s:
    if char in curr:
        curr=curr[curr.index(char)+1:]
    curr+=char
    max_len=max(max_len,len(curr))
print(max_len)


#Q2:Subarray Sum Equals K
n,k=map(int,input().split())
nums=list(map(int,input().split()))
count=0
for i in range(n):
    total=0
    for j in range(i,n):
        total+=nums[j]
        if total==k:
            count+=1
print(count)


#Q3:Next Greater Element to the Right 
n=int(input())
l=list(map(int,input().split()))
for i in range(n):
    ans=-1
    for j in range(i+1,n):
        if l[j]>l[i]:
            ans=l[j]
            break
    print(ans)
    

#Q4: Valid Parentheses
s=input()
st=[]
for c in s:
    if c=='(' or c=='{' or c=='[':
        st.append(c)
    elif c==')' or c=='}' or c==']':
        if not st:
            print(False)
            break
        last=st[-1]            
        if c==')' and last!='(':
            print(False)
            break
        elif c=='}' and last!='{':
            print(False)
            break
        elif c==']' and last!='[':
            print(False)
            break
        st.pop()
else:
    if not st:
        print(True)
    else:
        print(False)
        
#-----------------------------sec-B---------------------

# Q5. Merge Overlapping Intervals

n=int(input())
l=[]
for i in range(n):
    l.append(list(map(int,input().split())))
l.sort()
new=[]
for i in l:
    if not new or i[0]>new[-1][1]:
        new.append(i)
    else:
        new[-1][1]=max(new[-1][1],i[1])
for i in new:
    print(i[0],i[1])


#Q7:Kth Smallest Element in Sorted Matrix
n=int(input())
matrix=[list(map(int,input().split())) for i in range(n)]
l=[num for row in matrix for num in row]
k=int(input())
l.sort()
print(l[k-1])


        
#---------------------sec-C------------------------------
#Q9: Streaming Median
n=int(input())
l=list(map(int,input().split()))
ans=[]
for num in l:
    ans.append(num)
    ans.sort()
    m=len(ans)
    if m%2==1:
        median=float(ans[m//2])
    else:
        median=(ans[m//2-1]+ans[m//2])/2
    print(median)
'''


