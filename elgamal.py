def mod_exp(base, exp, mod):
    """Perform modular exponentiation: (base^exp) % mod efficiently."""
    result = 1
    base = base % mod

    while exp > 0:
        if exp % 2 == 1:  # If exp is odd
            result = (result * base) % mod
        exp = exp // 2  # Divide exp by 2
        base = (base * base) % mod

    return result

def elgamal():
    # Input values
    p = int(input("Enter a prime number (p): "))  # Prime number
    e1 = int(input("Enter e1 (primitive root modulo p): "))  # Primitive root
    d = int(input("Enter d (private key): "))  # Private key

    # Compute e2 = (e1^d) mod p
    e2 = mod_exp(e1, d, p)
    print(f"Value of e2 (public key e2 = e1^d mod p): {e2}")

    r = int(input("Enter r (random number): "))

    m = int(input("\nEnter the message to encrypt (m): "))  # Message

    # Encryption
    c1 = mod_exp(e1, r, p)
    c2 = (mod_exp(e2, r, p) * m) % p

    print("\nEncrypted values:")
    print(f"c1 = {c1}")
    print(f"c2 = {c2}")

    # Decryption
    temp = mod_exp(c1, d, p)  # c1^d mod p
    temp_inverse = mod_exp(temp, p - 2, p)  # Modular inverse using Fermat's theorem
    decrypted_message = (c2 * temp_inverse) % p

    print(f"\nDecrypted message: {decrypted_message}")

# Run the ElGamal encryption and decryption
if __name__ == "__main__":
    elgamal()
