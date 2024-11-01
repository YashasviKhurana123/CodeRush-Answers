def is_prime(num):
    # Write your code here
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

#
# Complete the 'generate_prime_multiples_list' function below.
#
# The function accepts INTEGER_ARRAY num_array as parameter.
#

def generate_prime_multiples_list(num_array):
    # Write your code here
    n = len(num_array)  # Use num_array instead of arr
    primes = [num for num in num_array if is_prime(num)]  # Identify primes in the list
    
    result = []
    for prime in primes:
        multiples = [prime * i for i in range(1, n + 1)]  # Generate multiples for each prime
        result.append([prime] + multiples)
    
    print(result)