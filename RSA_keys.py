import math

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
    while not is_prime(p):
        p = int(input("Enter 1st prime: "))
    q = 0
    while not is_prime(q):
        q = int(input("Enter 2nd prime: "))

    return (p, q)


def public_private_keys():
    p, q = get_starting_primes()
    print(f"p = {p}\nq = {q}")


def main():
    public_private_keys()



if __name__ == "__main__":
    main()