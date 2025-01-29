from math import gcd

# Function to compute the modular inverse using the Extended Euclidean Algorithm
def mod_inverse(e, phi):
    t1, t2 = 0, 1
    r1, r2 = phi, e

    while r2 > 0:
        q = r1 // r2
        r = r1 - q * r2
        r1, r2 = r2, r

        t = t1 - q * t2
        t1, t2 = t2, t

    if r1 != 1:
        raise ValueError("No modular inverse exists (e and φ(n) are not coprime).")

    return (t1 + phi) % phi  # Ensure d is positive

# Function to encrypt a single number
def encrypt_number(num, e, n):
    return pow(num, e, n)

# Function to decrypt a single number
def decrypt_number(encrypted_num, d, n):
    return pow(encrypted_num, d, n)

def main():
    # Step 1: Take input for prime numbers
    p = int(input("Enter first prime number (p): "))
    q = int(input("Enter second prime number (q): "))

    # Step 2: Compute n and φ(n)
    n = p * q
    phi = (p - 1) * (q - 1)
    print(f"The value of φ(n) = {phi}")

    # Step 3: Input public exponent 'e'
    while True:
        e = int(input("Enter the public exponent (e): "))
        if gcd(e, phi) == 1:
            break  # Valid e
        else:
            print(f"Invalid e! It must be coprime with {phi}")

    print(f"The public exponent (e) = {e}")

    # Step 4: Compute private exponent 'd'
    d = mod_inverse(e, phi)
    print(f"The private exponent (d) = {d}")

    # Print the public and private keys
    print(f"Public Key: ({e}, {n})")
    print(f"Private Key: ({d}, {n})")

    # Step 5: Encrypt & decrypt a number
    num = int(input("Enter a number to encrypt: "))
    encrypted_num = encrypt_number(num, e, n)
    print(f"Encrypted number: {encrypted_num}")

    decrypted_num = decrypt_number(encrypted_num, d, n)
    print(f"Decrypted number: {decrypted_num}")

if __name__ == "__main__":
    main()
