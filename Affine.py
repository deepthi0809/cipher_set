import math
# Function to compute GCD 
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
# Function to find modular inverse of 'a' under mod 26
def mod_inverse(a, m):
    for i in range(m):
        if (a * i) % m == 1:
            return i
    return None  # No modular inverse if not coprime
# Function to encrypt the message
def encrypt_message(msg, a, b):
    cipher = ""
    b = ((b % 26) + 26) % 26  # Ensure b is in range [0, 25]
    for char in msg:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            char_pos = ord(char) - base
            encrypted_char = chr(((a * char_pos + b) % 26) + base)
            cipher += encrypted_char
        else:
            cipher += char  # Preserve spaces or any other characters
    return cipher

# Function to decrypt the cipher text
def decrypt_cipher(cipher, a, b):
    msg = ""
    a_inv = mod_inverse(a, 26)
    if a_inv is None:
        return "Error: No modular inverse exists for 'a'. Choose a different 'a' coprime with 26."
    b = ((b % 26) + 26) % 26  # Ensure b is in range [0, 25]
    for char in cipher:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            char_pos = ord(char) - base
            decrypted_char = chr(((a_inv * (char_pos - b + 26)) % 26) + base)
            msg += decrypted_char
        else:
            msg += char  # Preserve spaces
    return msg

# Main function
def main():
    msg = input("Enter encryption message: ").lower()
    
    if not all(c.isalpha() or c.isspace() for c in msg):
        print("Invalid input! Please enter only letters and spaces.")
        return
    a = int(input("Enter 'a' (the key must be coprime with 26): "))
    
    if gcd(a, 26) != 1:
        print("Error: The key 'a' must be coprime with 26! Please enter a valid 'a'.")
        return
    b = int(input("Enter 'b' (this key can be negative): "))
    cipher_text = encrypt_message(msg, a, b)
    print("Encrypted Message :", cipher_text)
    decrypted_message = decrypt_cipher(cipher_text, a, b)
    print("Decrypted Message :", decrypted_message)

if __name__ == "__main__":
    main()
