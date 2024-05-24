def print_formatted(number):
    # Calculate the width needed for the binary representation of the largest number
    width = len(bin(number)) - 2
    
    for i in range(1, number + 1):
        # Generate formatted string for each representation
        decimal = str(i).rjust(width)
        octal = oct(i)[2:].rjust(width)
        hexadecimal = hex(i)[2:].upper().rjust(width)
        binary = bin(i)[2:].rjust(width)
        
        # Print all representations space-separated
        print(f"{decimal} {octal} {hexadecimal} {binary}")