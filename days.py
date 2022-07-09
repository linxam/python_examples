def days(year, month, day):
    '''Возвращает количество дней между двумя датами'''
    from datetime import date
    delta = abs(date.today() - date(year, month, day))
    return delta.days

if __name__ == '__main__':
    print(days(2022, 7, 1))
