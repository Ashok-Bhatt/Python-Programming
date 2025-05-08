# alphabet will contain all the small case alphabets and hence listed from chr(97) i.e. 'a' to chr(122) i.e. 'z'
alphabet = [chr(i) for i in range(97,123)]

# cipher_text and real_text will contain the encoded and decode text. Initially, they are taken as empty string
cipher_text = ""
real_text = ""


def encrypt(text, shift):
    """
encrypt function will take two parameters: text and shift
It will generate an encrypted message for text with shifting the characters shift times rightwards
    """

    # We are changing the cipher_text at global level so that it can be accessed outside the function as well
    global cipher_text
    for character in text:
        if character not in alphabet:
            # We will be adding the same character to the cipher_text if it is not an alphabet
            cipher_text += character  
        else:
            # If the character is an alphabet, then will will add the encode character to the cipher_text
            # We will be adding shift to the index of character in alphabet list but will take the modulo 26 to prevent list indices out of range
            cipher_text += alphabet[(alphabet.index(character) + shift) % 26]

    return cipher_text
    

def decrypt(text, shift):
    """
decrypt function will take two parameters: text and shift
It will generate an decrypted message for text with shifting the characters shift times leftwards to get the original text
    """

    global real_text
    for character in text:
        if character not in alphabet:
            real_text += character
        else:
            # Same as of cipher_text, but we are subtracting with shift number instead of adding it
            real_text += alphabet[(alphabet.index(character) - shift) % 26]

    return real_text


while (True):

    # direction is the variable that will decide whether we want to decode or encode the statement or want to exit the program
    direction = input("Enter 'encode' for encoding, 'decode' for decoding and anything else to exit the program:")

    if direction in ["encode","decode"]:
        # We will ask about the text that we want to encode-decode w.r.t. shift number if and only if direction is either 'encode' or 'decode'
        text = input("Enter your message:").lower()     # We will convert the text to smaller case as alphabet list conatins small letters
        shift = int(input("Enter the number of characters you want to shift:"))

        if direction == "encode":
            # if direction is encode then we will call the encrypt() function
            encrypt(text, shift)
            print(f"The encoded text is given by: {cipher_text}")
            # We will empty the cipher_text after calling the encrypt() function so that it can be used for other text also
            cipher_text = ""

        elif direction == "decode":
            # if direction is decode then we will call the decrypt() function
            decrypt(text, shift)
            print(f"The decoded text is given by: {real_text}")
            # Same as of cipher_text
            real_text = ""

        print("")

    else:
        print("\nThanks for using our services.")
        break