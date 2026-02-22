import sys

def solve_rsa():
    print("--- RSA Challenge Solver (List Mode) ---")

    # 1. Inputs
    try:
        n_input = input("Enter n: ").strip()
        if not n_input: return
        n = int(n_input)

        e_input = input("Enter e (default 65537): ").strip()
        e = int(e_input) if e_input else 65537

        c_input = input("Enter ciphertext (space separated): ").strip()
        # Convert "996 894 ..." -> [996, 894, ...]
        cipher_list = [int(x) for x in c_input.split()]
        
    except ValueError:
        print("Error: Please enter valid integers.")
        return

    # 2. Factorize n -> p, q
    p, q = None, None
    
    # Simple trial division
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            p = i
            q = n // i
            break
            
    if p is None:
        print("Error: Could not factorize n.")
        return

    print(f"[*] Factors found: p={p}, q={q}")

    # 3. Calculate phi & d
    phi = (p - 1) * (q - 1)
    
    try:
        d = pow(e, -1, phi)
    except ValueError:
        print("Error: Modular inverse does not exist.")
        return

    print(f"[*] Private key d: {d}")

    # 4. Decrypt each number individually
    decrypted_chars = []
    
    print("[*] Decrypting...")
    for c_val in cipher_list:
        # m = c^d mod n
        m = pow(c_val, d, n)
        
        # Convert integer to character (ASCII)
        # If m is larger than 255/1114111, this might fail or be a block
        try:
            char = chr(m)
            decrypted_chars.append(char)
        except ValueError:
            decrypted_chars.append('?')

    # 5. Join and print result
    result = "".join(decrypted_chars)
    print(f"[*] Decrypted Message: {result}")

if __name__ == "__main__":
    solve_rsa()
