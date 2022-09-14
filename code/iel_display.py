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
            '9':0b00111101}
    
    val = iel_dict[d]
    sr.bits(val,8)
    sr.latch()
    
    
    
    