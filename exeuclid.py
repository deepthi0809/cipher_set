# Function to compute GCD and find modular inverse
def find_gcd_and_inverse(a, m):
    r1 = m
    r2 = a
    t1 = 0
    t2 = 1
    print("Step-by-step computation:")
    print("q\tr1\tr2\tr\tt1\tt2\tt")
    while r2 > 0:
        q = r1 // r2
        r = r1 - q * r2
        r1 = r2
        r2 = r
        t = t1 - q * t2
        t1 = t2
        t2 = t
        print(f"{q}\t{r1}\t{r2}\t{r}\t{t1}\t{t2}\t{t}")
    print(f"\nGCD({a}, {m}) = {r1}")
    # If GCD is not 1, inverse does not exist
    if r1 != 1:
        print("Since GCD ≠ 1, modular inverse does not exist.")
        return
    # Ensure the inverse is positive
    inverse = (t1 % m + m) % m
    print(f"The modular inverse of {a} under modulo {m} is: {inverse}")
def main():
    # Input number and modulus
    a = int(input("Enter number (a): "))
    m = int(input("Enter modulus (m): "))
    # Compute and display results
    find_gcd_and_inverse(a, m)
if __name__ == "__main__":
    main()
