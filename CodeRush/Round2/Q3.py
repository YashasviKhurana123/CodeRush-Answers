import math

def circular_primes(num):
    # Helper function to check if a number is prime
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    # Helper function to get all rotations of a number
    def get_rotations(n):
        s = str(n)
        rotations = [int(s[i:] + s[:i]) for i in range(len(s))]
        return rotations

    # Calculate the sum of circular primes below the given number
    total_sum = 0
    for n in range(2, num):
        rotations = get_rotations(n)
        # Ensure all rotations are prime before adding the number
        if all(is_prime(rot) for rot in rotations):
            total_sum += n

    print(total_sum)  # Output the result as required