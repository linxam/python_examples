def mymax(l):
    '''Custom max function. Python example/exercise.''' 
    m = l[0]
    for i in l:
        if i > m:
            m = i
    return m
    
print(mymax([2, 5, 3, 1]))
print(mymax('zxcvzxcvzxcvxz'))
print(mymax(('asdf', 'qwer', 'zxcv')))
