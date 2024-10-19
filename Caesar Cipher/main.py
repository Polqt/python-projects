# Alphabet list with repeated alphabet to handle shift wrapping
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Caesar cipher function
def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    # Reverse shift for decoding
    if cipher_direction == "decode":
        shift_amount *= -1
    # Loop through each character in the text
    for char in start_text:
        # Encode/Decode only if character is a letter
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            # Keep non-letter characters as they are
            end_text += char
    # Print the result
    print(f"Here's the {cipher_direction}d result: {end_text}")

# Import and print the logo from art.py
import art
print(art.logo)

# Loop to allow restarting the program
is_continue = False
while not is_continue:
    # Get user inputs for direction, message, and shift
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    # Handle shift values larger than 26
    shift = shift % 26
    # Call the Caesar cipher function
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    # Ask if the user wants to restart the program
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no':\n").lower()
    if restart == "no":
        is_continue = True
        print("Goodbye")
