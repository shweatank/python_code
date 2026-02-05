from __future__ import annotations

import sys

# ----------------------------
# Implement these 12 solvers
# ----------------------------

def solve_q1(data: list[str]) -> str:
    # Q1: t, then t strings -> output t lines of lengths
    def lengthOfLongestSubstring(s: str) -> int:
        start = 0
        end = 0
        maxLen = 0

        while end < len(s):
            if s[end] not in s[start:end]:
                end += 1
            else:
                start += 1
            
            if len(s[start:end]) > maxLen:
                maxLen = len(s[start:end])

        return maxLen
    
    solution = ""
    t = int(input())
    for k in range(t):
        s = input()
        solution += str(lengthOfLongestSubstring(s))+'\n'
    
    return solution



def solve_q2(data: list[str]) -> str:
    # Q2: t, then for each: n k and n ints -> output t lines of counts
    def subarraySum(nums: list[int], k: int) -> int:
        # solving using prefix sum
        n_sa = 0
        s = 0
        p = {}
        for num in nums:
            s += num

            if s == k:
                n_sa += 1
            
            if s - k in p:
                n_sa += p[s-k]
            
            p[s] = p.get(s, 0) + 1

        return n_sa
    
    solution = ""
    t = int(input())
    for i in range(t):
        n, k = map(int, input().split())
        arr = map(int, input().split())

        solution += str(subarraySum(arr)) + '\n'

    return solution
    
    

def solve_q3(data: list[str]) -> str:
    # Q3: n then n ints -> output one line of n ints
    def nextGreater(nums: list[int]) -> list[int]:
        result = [-1] * len(nums)
        stack = []

        for i in range(len(nums)): # O(n)
            while stack and nums[i] > nums[stack[-1]]: 
                index = stack.pop()
                result[index] = i
            stack.append(i)
        return result
    
    n = int(input())
    arr = list(map(int, input().split()))

    return " ".join(nextGreater(arr))

def solve_q4(data: list[str]) -> str:
    # Q4: one bracket string -> YES/NO
    def isValid(s: str) -> bool:
        i = 0
        stack = []
        for i in range(len(s)):
            if s[i] == '(' or s[i] =='[' or s[i] == '{':
                stack.append(s[i])
            else:
                if not stack:
                    return False
                top = stack.pop()
                if s[i] == ')' and top != '(':
                    return False
                if s[i] == ']' and top != '[':
                    return False
                if s[i] == '}' and top != '{':
                    return False
        return len(stack) == 0

    data = input()
    return "YES" if isValid(data) else "NO"

def solve_q5(data: list[str]) -> str:
    # Q5: n then n intervals -> merged intervals lines
    def merge(intervals: list[list]):
        intervals.sort(key=lambda x: x[0]) # O(nlogn)

        stack = []
        stack.append(intervals[0])
        i = 1
        n = len(intervals)
        while i < n: # O(n)
            if intervals[i][0] <= stack[-1][1]:
                stack[-1][1] = max(intervals[i][1], stack[-1][1])
            else:
                stack.append(intervals[i])
            i+=1 
            
        intervals.clear()
        while len(stack):
            intervals.append(stack.pop())
            # stack.pop()

        return intervals
    
    n = int(input())
    data = []
    for _ in range(n):
        i, k = map(int, input().split())
        data.append([i,k])
    
    output = merge(data)
    solution = ""
    for interval in output:
        solution += " ".join(interval) + '\n'
    
    return solution

def solve_q6(data: list[str]) -> str:
    # Q6: s then t -> min window substring (or empty line)
    def minWindowSubstr(s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        freq = {}
        for c in t:
            freq[c] = freq.get(c, 0) + 1

        required = len(freq)

        l, r = 0, 0

        match = 0
        window_freq = {}

        minLen = float('inf')
        minl = 0

        while r < len(s):
            c = s[r]
            window_freq[c] = window_freq.get(c, 0) + 1

            if c in freq and window_freq[c] == freq[c]:
                match += 1

            while l <= r and match == required:
                if r - l + 1 < minLen:
                    minLen = r - l + 1
                    minl = l
                left_char = s[l]
                window_freq[left_char] -= 1

                if left_char in freq and window_freq[left_char] < freq[left_char]:
                    match -= 1

                l += 1
            r += 1

        return "" if minl == float('inf') else s[minl:minl + minLen]
    
    s = input()
    t = input()
    return minWindowSubstr(s,t)

def solve_q7(data: list[str]) -> str:
    # Q7: n, n lines of n ints, k -> kth smallest
    def smallestElement(matrix: list[list], k: int) -> int | None:
        m = len(matrix)
        n = len(matrix[0])
        if k  > m*n:
            return None

        for i in range(m):
            for j in range(n):
                if  i*n + j + 1== k:
                    return matrix[i][j]

    n = int(input())
    matrix = []
    for _ in range(n):
        matrix.append(list(map(int, input().split())))
    
    return str(smallestElement(matrix))


def solve_q8(data: list[str]) -> str:
    # Q8: n m, then m edges a b -> YES/NO
    raise NotImplementedError

def solve_q9(data: list[str]) -> str:
    # Q9: n then n ints -> n medians with one decimal (space-separated)
    raise NotImplementedError

def solve_q10(data: list[str]) -> str:
    # Q10: n then n points x y -> MST Manhattan cost
    raise NotImplementedError

def solve_q11(data: list[str]) -> str:
    # Q11: r c then grid -> distinct islands count
    raise NotImplementedError

def solve_q12(data: list[str]) -> str:
    # Q12: q then q ops -> output for op=3
    raise NotImplementedError



if __name__ == "__main__":
    pass