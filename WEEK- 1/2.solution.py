## Solution for assignment 2
def compress_string(S):
    if not S:
        return ""
    
    result = []
    current_char = S[0]
    count = 1
    
    for i in range(1, len(S)):
        if S[i] == current_char:
            count += 1
        else:
            result.append(f"({count}, {current_char})")
            current_char = S[i]
            count = 1
    
    # Append the last set of counts
    result.append(f"({count}, {current_char})")
    
    return " ".join(result)

# Example usage
input_string = input()
output_string = compress_string(input_string)
print(output_string)