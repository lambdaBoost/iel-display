import time

def display_digit(d, sr):
    
    """
    display 8 bit digit
    inputs:
    d: string, name of digit to display
    sr: shift register object
    """
    
    iel_dict = {'0':0b01010011,
            '1':0b00000010,
            '2':0b10011001,
            '3':0b00011101,
            '4':0b00101100,
            '5':0b00110101,
            '6':0b10110101,
            '7':0b10011000,
            '8':0b10111101,
            '9':0b00111101,
            'A':0b01111010,
            'B':0b11000101,
            'C':0b01010001,
            'D':0b10000111,
            'E':0b11110001,
            'F':0b11110000,
            'G':0b01010101,
            'H':0b11101110,
            'I':0b01000000,
            'J':0b00000011,
            'K':0b01001100,
            'L':0b01000001,
            'M':0b01101010,
            'N':0b01100110,
            'O':0b01010011,
            'P':0b01111000,
            'Q':0b00111100,
            'R':0b01011100,
            'S':0b00110101,
            'T':0b10100001,
            'U':0b01000011,
            'V':0b00101000,
            'W':0b11000110,
            'X':0b10101100,
            'Y':0b00101101,
            'Z':0b10011001}
    
    val = iel_dict[d]
    sr.bits(val,8)
    sr.latch()
    
def display_all(sr):
    
    ls = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    for i in ls:
        display_digit(i, sr)
        time.sleep(1)
    
    
    
    