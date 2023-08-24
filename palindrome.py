import string

def is_palindrome(sentence):
    # Remove punctuation and spaces, and convert to lowercase
    cleaned_sentence = ''.join(char for char in sentence if char not in string.punctuation).replace(" ", "").lower()
    
    # Check if the cleaned sentence is equal to its reverse
    return cleaned_sentence == cleaned_sentence[::-1]

# Get input from the user
sentence = input("Enter a sentence: ")

# Check if the sentence is a palindrome
if is_palindrome(sentence):
    print(f"'{sentence}' is a palindrome!")
else:
    print(f"'{sentence}' is not a palindrome.")
