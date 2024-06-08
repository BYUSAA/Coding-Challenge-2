def transform_string(s):
    # Check if the length of the string is divisible by 15
    if len(s) % 15 == 0:
        # Replace each character with its ASCII code
        ascii_string = ''.join(str(ord(c)) for c in s)
        # Reverse the entire string
        result = ascii_string[::-1]
    # Check if the length of the string is divisible by 5
    elif len(s) % 5 == 0:
        # Replace each character with its ASCII code
        result = ' '.join(str(ord(c)) for c in s)
    # Check if the length of the string is divisible by 3
    elif len(s) % 3 == 0:
        # Reverse the entire string
        result = s[::-1]
    else:
        # If the length of the string is not divisible by 3, 5, or 15, return the original string
        result = s
    return result

# Test the function
print(transform_string("Hamburger"))  # Output: "regrubmaH"
print(transform_string("Pizza"))  # Output: "80 105 122 122 97"
print(transform_string("Chocolate Chip Cookie"))  # Output: "eikooCpihCetalocohC"