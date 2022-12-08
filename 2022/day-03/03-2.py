UTF_LOWERCASE_OFFSET = -96
UTF_UPPERCASE_OFFSET = -38

priorities = ({chr(i): ord(chr(i)) + UTF_LOWERCASE_OFFSET
               for i in range(97, 123)} |
              {chr(i): ord(chr(i)) + UTF_UPPERCASE_OFFSET
               for i in range(65, 91)})

priority_sum = 0

elf_1 = set()
elf_2 = set()
elf_3 = set()

with open('input.txt') as input:
    while True:
        elf_1.update(input.readline().strip())
        elf_2.update(input.readline().strip())
        elf_3.update(input.readline().strip())
        if not elf_3:
            break
        badge = elf_1.intersection(elf_2.intersection(elf_3)).pop()
        priority_sum += priorities.get(badge)
        elf_1.clear()
        elf_2.clear()
        elf_3.clear()

print(priority_sum)
