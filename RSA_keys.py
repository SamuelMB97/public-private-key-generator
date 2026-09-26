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
    """Gets input for q, p prime numbers
    and verifies the numbers will work."""
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
    """finds an appropriate e coprime with a given phi"""
    options = [n+1 for n in range(phi-1)]
    while options:
        e = random.choice(options)
        gcd = euclidian_rec(phi, e)
        if gcd == 1:
            return e
        else:
            options.remove(e)
    
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
    #print(f"{a} = {b}({floor}) + {remainder}")
    if remainder == 0:
        if not prev_remainder:
            prev_remainder = b
        return prev_remainder
    else:
        return euclidian_rec(remainder, b, prev_remainder=remainder)


def public_private_keys():
    """Asks user for starting prime numbers p and q,
    then generates public and private keys."""
    ## STEP 1
    p, q = get_starting_primes()

    ## STEP 2
    n = p * q

    ## STEP 3
    phi = (p-1) * (q-1)

    ## STEP 4
    e = find_coprime(phi)

    if not e:
        public_private_keys()

    ## STEP 5
    intercept = pow(e, -1, phi)
    num = 1

    d = phi*num + intercept
    return ((e, n), d)


def encode(x, e, n, printing=False):
    """takes a message int and the public key values,
    returns encoded value"""
    if x > n:
        return -1
    result = (x ** e) % n
    if printing:
        print(f"\t({x}^{e}) % {n} = {result}")
    return result

def decode(y, d, n, printing=False):
    """takes a encoded int and the private key values,
    returns the decoded message"""
    if y > n:
        return -1
    result = (y ** d) % n
    if printing:
        print(f"\t({y}^{d}) % {n} = {result}")
    return result


def testit(num, e, n, d):
    """Tests the keys against a given num,
    returns True if coding works"""
    if num > n:
        return -1
    secret = encode(num, e, n, printing=True)
    decoded = decode(secret, d, n, printing=True)
    passes = decoded == num
    #print(f"num: {num}, secret: {secret}, decoded: {decoded}, correct: {passes}")
    return passes


def main():
    public, private = public_private_keys()
    e = public[0]
    n = public[1]
    d = private

    print(f"public key: ({e}, {n})")
    print(f"private key: {d}")

    command = "go"
    while command.lower() not in ['q', 'exit', 'stop']:
        command = input(f"""public: ({e}, {n}), private: {d}
        Encode/decode? (e/d, q=stop): """)

        if command == "e":
            message = int(input(f"\tenter number to encode (max {n}): "))
            encoded = encode(message, e, n, printing=True)
            print(f"\tresult: {encoded}")

        elif command == "d":
            secret = int(input(f"\tenter number to decode (max {n}): "))
            decoded = encode(secret, d, n, printing=True)
            print(f"\tresult: {decoded}")
    print("Ending...")

    """
    test_numbers = [259, 1895, 5532, 112, 5, 66, 23, 288]
    scores = [testit(t, e, n, d) for t in test_numbers]
    print(scores)
    #"""


if __name__ == "__main__":
    main()