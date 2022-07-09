def is_prime(num: int) -> bool:
    '''this function returns True if there is a prime number, else returns False'''
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, round(num**0.5)+1, 2):
        if num % i == 0:
            return False
    return True

if __name__=='__main__':
    for i in range(20):
        print(i, is_prime(i))

