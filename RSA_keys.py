import math
import random

def is_prime(n:int):
    """Takes an integer n and returns True if n is prime.
    This function's basic structure found online. We only check
    positive numbers greater than 1. 2 is the only even prime."""
    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False

    for x in range(3, int(math.sqrt(n)+1), 2):
        if n % x == 0:
            return False

    return True


def get_starting_primes():
    p = 0
    while not is_prime(p) or p == 1:
        p = int(input("Enter 1st prime: "))
    q = 0
    while not is_prime(q) or q == 1:
        q = int(input("Enter 2nd prime: "))

    if p*q < 10:
        print("That combination won't work. Try another.")
        p, q = get_starting_primes()

    return (p, q)


def find_coprime(phi):
    options = [n+1 for n in range(phi-1)]
    while options:
        e = random.choice(options)
        print(f"Trying with e = {e}")
        gcd = euclidian_rec(phi, e)
        if gcd == 1:
            return e
        else:
            options.remove(e)
    
    print(f"There isn't a prime below phi (phi = {phi})")
    return False


def euclidian_rec(a, b, prev_remainder=None):
    """Takes two positive integers, and
    returns their greatest common divsor"""
    if a < b:
        c = a
        a = b
        b = c
    floor = a // b
    remainder = a % b
    print(f"{a} = {b}({floor}) + {remainder}")
    if remainder == 0:
        if not prev_remainder:
            prev_remainder = b
        return prev_remainder
    else:
        return euclidian_rec(remainder, b, prev_remainder=remainder)



def public_private_keys():
    ## STEP 1
    p, q = get_starting_primes()
    print(f"p = {p}\nq = {q}")

    ## STEP 2
    n = p * q
    print(f"n = {n}")

    ## STEP 3
    phi = (p-1) * (q-1)
    print(f"phi = {phi}")

    ## STEP 4
    e = find_coprime(phi)
    print(f"e = {e}")
    #e = int(input("testing, give e: "))
    #n = int(input("testing, give n: "))

    if not e:
        public_private_keys()

    ## STEP 5
    #print(euclidian_rec(n, e))

def main():
    public_private_keys()



if __name__ == "__main__":
    main()