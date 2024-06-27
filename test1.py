import bisect
from collections import defaultdict

#从终端输入source 和 target
source = str(input())
target = str(input())

char_indices = defaultdict(list)
for index, char in enumerate(source):
    char_indices[char].append(index)

res = 0
target_idx = 0
current_pos = -1  
not_None = True
while target_idx < len(target):
    target_char = target[target_idx]
    if target_char not in char_indices:
        print(-1)
        not_None = False
        break   
    indices_list = char_indices[target_char]
    pos = bisect.bisect_right(indices_list, current_pos)
    if pos == len(indices_list):  
        res += 1
        current_pos = -1  
    else:
        current_pos = indices_list[pos]
        target_idx += 1

if not_None:
    print(res+1)



