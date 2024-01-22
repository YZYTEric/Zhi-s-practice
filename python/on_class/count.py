def string_test(s):
    # Create a dictionary 'd' to store the count of upper and lower case characters
    d = {"UPPER_CASE": 0, "LOWER_CASE": 0}
    
    # Iterate through each character 'c' in the string 's'
    for x in s:
        # Check if the character 'c' is in upper case
        if x.isupper():
            # If 'c' is upper case, increment the count of upper case characters in the dictionary
            d["UPPER_CASE"] += 1
        # Check if the character 'c' is in lower case
        elif x.islower():
            # If 'c' is lower case, increment the count of lower case characters in the dictionary
            d["LOWER_CASE"] += 1
        else:
            # If 'c' is neither upper nor lower case (e.g., punctuation, spaces), do nothing
            pass
    
    # Print the original string 's'
    print("Original String: ", s)
    
    # Print the count of upper case characters
    print("No. of Upper case characters: ", d["UPPER_CASE"])
    
    # Print the count of lower case characters
    print("No. of Lower case Characters: ", d["LOWER_CASE"])

# Call the 'string_test' function with the input string 'The quick Brown Fox'
string_test('HELLO, world') 


