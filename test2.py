line = str(input())
results = []
stack = []
res_line = [' '] * len(line)
for i, char in enumerate(line):
    if char == '(':
        stack.append(i)
    elif char == ')':
        if stack:
            stack.pop()
        else:
            res_line[i] = '?'
while stack:
    res_line[stack.pop()] = 'x'

results.append(line)
results.append(''.join(res_line))

for result in results:
    print(result)
