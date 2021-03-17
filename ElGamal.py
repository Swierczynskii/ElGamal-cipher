import random  
from math import pow
 
def encrypt(M, P, Gk, G): 
  
    en_M = [] 
  
    k = create_key(P)                  
    a = mod_exp(Gk, k, P) 
    b = mod_exp(G, k, P) 
      
    for i in range(0, len(M)): 
        en_M.append(M[i]) 
  
    print("C1                       :", b) 
    print("Shared Secret            :", a) 
    for i in range(0, len(en_M)): 
        en_M[i] = a * ord(en_M[i]) 
  
    return en_M, b 
  
def decrypt(en_M, b, key, P): 
  
    dec_M = [] 
    h = mod_exp(b, key, P) 
    for i in range(0, len(en_M)): 
        dec_M.append(chr(int(en_M[i]/h))) 
          
    return dec_M 
  
   
def gcd(a, b): 
    if a < b: 
        return gcd(b, a) 
    elif a % b == 0: 
        return b 
    else: 
        return gcd(b, a % b)

def mod_exp(a, b, c): 
    x = 1
    y = a 
  
    while b > 0: 
        if b % 2 == 0: 
            x = (x * y) % c 
        y = (y * y) % c 
        b = int(b / 2) 
  
    return x % c 
    
def create_key(P): 
  
    key = random.randint(1, P-1) 
    while gcd(P, key) != 1: 
        key = random.randint(1, P-1) 
  
    return key 
  
def test():
    
    M = 'Hi Bob!'
    print("Alice's message to Bob   :", M) 
  
    P = random.randint(pow(10, 20), pow(10, 50)) 
    key = create_key(P)                 
    G = random.randint(2, P)  
    Gk = mod_exp(G, key, P) 
    print("G                        :", G) 
    print("G^priv_key_receiver      :", Gk) 
  
    en_M, b = encrypt(M, P, Gk, G)      # Alice sends Bob a ciphertext (c1, c2)

    dec_M = decrypt(en_M, b, key, P)    # Bob starts decrypting using ciphertext, message and his key

    dM = ''.join(dec_M) 
    print("Decrypted Message        :", dM)

def main():
    test() 
  
  
if __name__ == '__main__': 
    main() 