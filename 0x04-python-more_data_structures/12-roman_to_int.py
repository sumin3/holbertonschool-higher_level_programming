#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) != str:
        return 0
    total = 0
    sym = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    val = [1, 5, 10, 50, 100, 500, 1000]
    for i in range(0, len(roman_string)):
        for idx in range(0, 7):
            if roman_string[i] == sym[idx]:
                total += val[idx]
                if i != 0:
                    if roman_string[i - 1] == 'I' and roman_string[i] != 'I':
                        total = total - 2
    return total
