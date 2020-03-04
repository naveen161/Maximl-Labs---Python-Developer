s = input()
n = len(s)
k = len(set(s))
ans = float('inf')
i, j = 0, 0
while True:
    if len(set(s[j:i+1])) == k:
        ans = min(ans, i+1-j)
        j+=1
    else:
        i+=1
    if i > len(s):
        break
print(ans)