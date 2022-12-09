import collections

MARKER_LENGTH = 14

buffer = collections.deque([], maxlen = MARKER_LENGTH)

with open('input.txt') as file:
    input = file.readline()
    for i in range(MARKER_LENGTH):
        buffer.append(input[i])
    for i in range(len(input)):
        if len(set(buffer)) == MARKER_LENGTH:
            marker = i
            break
        buffer.popleft()
        buffer.append(input[i])

print(marker)