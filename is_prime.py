def is_prime(num: int) -> bool:
    '''this function returns True if there is a prime number, else returns False'''
    for i in range(2, round(num**0.5)+1):
        if num%i==0:
            return False
    return True

if __name__=='__main__':
    for i in range(20):
        print(i, is_prime(i))

