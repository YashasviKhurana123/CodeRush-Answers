def string_compression(text):
    # Write your code here
    compressed = []
    count = 1
    
    # Traverse the string
    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            count += 1
        else:
            # Append the character and its count
            compressed.append(text[i - 1] + str(count))
            count = 1
    
    # Append the last character and its count
    compressed.append(text[-1] + str(count))
    
    # Join the list to form the compressed string
    compressed_str = ''.join(compressed)
    
    # Return the compressed string if it's shorter, otherwise return the original string
    print(compressed_str if len(compressed_str) < len(text) else text)