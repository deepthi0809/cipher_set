# This function generates the key in a cyclic manner until it's length isn't equal to the length of the original text
def generate_key(text, key):
    x = len(text)
    i = 0
    while len(key) < len(text):
        key += key[i]
        i = (i + 1) % x
    return key
# This function returns the encrypted text generated with the help of the key
def cipher_text(text, key):
    cipher_text = ""
    for i in range(len(text)):
        if text[i] == ' ':
            cipher_text += ' '  # preserve spaces
            continue
        x = (ord(text[i]) + ord(key[i])) % 26
        x += ord('A')
        cipher_text += chr(x)
    return cipher_text
# This function decrypts the encrypted text and returns the original text
def original_text(cipher_text, key):
    orig_text = ""
    for i in range(len(cipher_text)):
        if cipher_text[i] == ' ':
            orig_text += ' '  # preserve spaces
            continue
        x = (ord(cipher_text[i]) - ord(key[i]) + 26) % 26
        x += ord('A')
        orig_text += chr(x)
    return orig_text
# This function will convert the lowercase character to uppercase
def lower_to_upper(s):
    return s.upper()
# Driver code
def main():
    # Taking input from the user
    text = input("Enter the message to encrypt: ").upper()  # Convert to upper case
    keyword = input("Enter keyword: ").upper()  # Convert to upper case
    # Generate key, encrypt and decrypt
    key = generate_key(text, keyword)
    cipher_text_result = cipher_text(text, key)
    print("Ciphertext: " + cipher_text_result)
    print("Decrypted message: " + original_text(cipher_text_result, key))
if __name__ == "__main__":
    main()
