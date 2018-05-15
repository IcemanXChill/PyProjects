import datetime


def print_header():
    print('--------------------------------')
    print('             Birthday APP')
    print('--------------------------------')


def get_birthday():
    year = int(input('What year were you born?: '))
    month = int(input('What month were you born?: '))
    day = int(input('What day were you born?: '))

    bday = datetime.date(year, month, day)
    return bday


def compute_days_between_dates(date1, date2):
    this_year = datetime.date(date2.year, date1.month, date1.day)
    return (this_year - date2).days


def print_birthday_information(days):
    if days > 0:
        print('your birthday is {0} days away.'.format(days))
    elif days < 0:
        print('your birthday was {0} days ago.'.format(-days))
    else:
        print('It is currently your birthday, congrats!')


def main():
    print_header()
    birthday = get_birthday()
    now = datetime.date.today()
    number_of_days_left = compute_days_between_dates(birthday, now)
    print_birthday_information(number_of_days_left)


main()
