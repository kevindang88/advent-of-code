with open ('day_08/input_08.txt') as input:
    count = 0
    

    for line in input:
        patterns, values = [x.strip().split(' ') for x in line.split('|')]

        # decode 1, 4, 7, 8
        decoded_digits = [None] * 10
        for p in patterns:
            match len(p):
                case 2:
                    decoded_digits[1] = p
                case 3:
                    decoded_digits[7] = p
                case 4:
                    decoded_digits[4] = p
                case 7:
                    decoded_digits[8] = p

        decoded_segments = {}
        for char in decoded_digits[7]:
            if char not in decoded_digits[1]:
                decoded_segments['a'] = char
                break
        
                


    print(patterns)
    print(decoded_digits)