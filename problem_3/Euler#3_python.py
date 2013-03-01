__author__ = 'Erin Depew'

'''The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ? '''

def make_prime(target_num):
    '''
    (int) -> list

    This function takes an int target_num, then makes a list of all the prime numbers in the range 2 to in target_num
    '''
    sieve = set()
    prime_list = []

    for i in range(2,target_num +1):
        if i not in sieve:

            sieve = sieve.union(make_mult(i,target_num))
            prime_list.append(i)

    return prime_list


def make_mult(base_num, largest):
    '''
     (int, int) -> set

     Helper function to make_prime, takes an int base_num and creates a set result from all of it's multiples within the range base_num +1 to int largest
    '''
    result = set()
    for i in range(2, (largest/base_num) +1):
        result.add(base_num * i)

    return result

def find_largest_prime(target_num):
    '''
    (int) -> int

    takes an int target_num and returns it's largest prime factor
    '''

    prime_list = make_prime(10000) #can't have unlimited prime list or the stack overflows
    prime_list.reverse()

    for i in prime_list:
        if target_num % i == 0:
            return i

    return target_num


print find_largest_prime(600851475143)





