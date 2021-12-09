with open ('day_08/input_08.txt') as input:
    result = 0
    for line in input:
        patterns, values = [list(map(frozenset, x.strip().split(' '))) for x in line.split('|')]

        digits = {}
        has_5_segments, has_6_segments = [], []

        for p in patterns:
            match len(p):
                case 2:
                    digits[1] = p
                case 3:
                    digits[7] = p
                case 4:
                    digits[4] = p
                case 5:
                    has_5_segments.append(p)
                case 6:
                    has_6_segments.append(p)
                case 7:
                    digits[8] = p

        # deduce 6, 9, 0
        for p in has_6_segments:
            if not p.issuperset(digits[1]):
                digits[6] = p
            elif p.issuperset(digits[4]):
                digits[9] = p
            else:
                digits[0] = p

        # deduce 3, 5, 2
        for p in has_5_segments:
            if p.issuperset(digits[1]):
                digits[3] = p
            elif p.issubset(digits[9]):
                digits[5] = p
            else:
                digits[2] = p

        decoded_value = ''
        for v in values:
            for i, k in enumerate(digits):
                if v == digits[k]:
                    decoded_value += str(k)

        result += int(decoded_value)

    print(result)
    