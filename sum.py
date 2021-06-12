def mysum(l, start=0):
    '''
    sum function. Python example/exercise.
    
    l -> list.
    start -> start point, that added to sum.
    
    function can also sum list with strings. In this case it converts 
    all list items to str. In this case start point is - empty string
    (c) Alexander Kilinkarov
    '''
    
    # check if there is string in list. And if there is, so convert
    # all list items to str
    for i in l:
        if isinstance(i, str):
            l = map(str, l)
            if start==0:
                start=''
            else:
                start = str(start)
            break
            
    # s is total sum
    s = start
    for i in l:
        s+=i
    return s

print(mysum([1, 2, 3], 6))
print(mysum(['1', '2', '3'], 'asdsa'))
