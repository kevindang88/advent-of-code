import collections

MARKER_LENGTH = 14

buffer = collections.deque([], maxlen = MARKER_LENGTH)
buffer_set = set()

with open('input.txt') as file:
    input = file.readline()
    for i in range(MARKER_LENGTH):
        buffer.append(input[i])
    for i in range(len(input)):
        buffer_set.update(buffer)
        if len(buffer_set) == MARKER_LENGTH:
            marker = i
            break
        buffer_set.remove(buffer.popleft())
        buffer.append(input[i])

print(marker)