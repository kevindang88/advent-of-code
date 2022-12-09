import collections

buffer = collections.deque([], maxlen = 14)
buffer_set = set()

with open('input.txt') as file:
    input = file.readline()
    for i in range(14):
        buffer.append(input[i])
    for i in range(len(input)):
        buffer_set.update(buffer)
        if len(buffer_set) == 14:
            marker = i
            break
        buffer_set.remove(buffer.popleft())
        buffer.append(input[i])

print(marker)