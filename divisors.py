def divisors(num):
    '''Возвращает список делителей натурального числа'''
    if num == 1:
        return [1]
    
    l = []
    for i in range(1, int(num**0.5) + 1):
        if num % i == 0 and num // i != i:
            l.append(i)
            l.append(num//i)

    return sorted(l)


if __name__ == '__main__':
    for i in range(1, 20):
        print(i, divisors(i))
