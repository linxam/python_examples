def lifedays(year, month, day):
    '''returns life days. Today is included'''
    from datetime import date, timedelta
    delta = date.today() - date(year, month, day)
    return delta.days+1

if __name__ == '__main__':
    print(lifedays(2021, 6, 20))
