def mymin(l):
    '''Custom min function. Python example/exercise.'''
    m = l[0]
    for i in l:
        if i<m:
            m = i
    return m
    
print(mymin([4,2,8,1]))
print(mymin('asdf'))
print(mymin(('asdf', 'qwer', 'zxcv')))
