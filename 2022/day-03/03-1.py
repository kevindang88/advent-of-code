UTF_LOWERCASE_OFFSET = -96
UTF_UPPERCASE_OFFSET = -38

priorities = ({chr(i): ord(chr(i)) + UTF_LOWERCASE_OFFSET
               for i in range(97, 123)} |
              {chr(i): ord(chr(i)) + UTF_UPPERCASE_OFFSET
               for i in range(65, 91)})

priority_sum = 0

item_set = set()

with open('input.txt') as input:
    while True:
        items = input.readline().strip()
        if not items:
            break

        item_count = len(items)
        
        for i in range(item_count):
            item = items[i]
            if item in item_set and i > item_count / 2:
                priority_sum += priorities.get(item)
                break
            item_set.add(item)
        item_set.clear()

print(priority_sum)
