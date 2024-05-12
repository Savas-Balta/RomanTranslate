def integer_to_roman(num):
    symbols = {
        1000: 'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I'}

    roman = ''
    for value in sorted(symbols.keys(), reverse=True):
        while num >= value:
            roman += symbols[value]
            num -= value

    return roman

# tam sayı giriniz
number = 250
print('Input integer number:',number)

roman_numeral = integer_to_roman(number)
print(f"The Roman numeral representation of {number} is: {roman_numeral}")