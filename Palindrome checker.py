def is_palindrome(s):
    # Convert the string to lowercase
    s = s.lower()
    # Remove non-alphanumeric characters
    s = ''.join(char for char in s if char.isalnum())
    # Check if the string is equal to its reverse
    return s == s[::-1]

# Test the function
string_to_check = input("Enter a string: ")
if is_palindrome(string_to_check):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
