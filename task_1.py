class MyCustomDate:
    
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
        self.all_day = self.day + (self.month * 30) + (self.year * 365)
        self.name = f'{day}.{month}.{year}'

    def __str__(self):
        print(self.name)

    def __eq__(self, other):
        if self.all_day == other.all_day:
            print(f'Даты {self.name} и {other.name} равны')
        else:
            print(f'False __eq__')

    def __ne__(self, other):
        if self.all_day != other.all_day:
            print(f'Даты {self.name} и {other.name} неравны')
        else:
            print(f'False __ne__')

    def __gt__(self, other):
        if self.year > other.year:
            print(f'Дата {self.name} младше даты {other.name}')
        else:
            print(f'False __gt__')

    def __lt__(self, other):
        if self.year < other.year:
            print(f'Дата {self.name} старше даты {other.name}')
        else:
            print(f'False __lt__')

    def __ge__(self, other):
        if self.year >= other.year:
            print(f'Дата {self.name} младше даты {other.name} или равно')
        else:
            print(f'False __ge__')

    def __le__(self, other):
        if self.all_day <= other.all_day:
            print(f'Дата {self.name} старше даты {other.name} или равно')
        else:
            print(f'False __le__')

    def __add__(self, other):
        sum_days = self.all_day + other.all_day
        sum_months = (sum_days / 365)
        sum_years = sum_months / 12
        print(
            f'\nСумма двух дат {self.name} и {other.name} равна:\n'
            f'В днях: {sum_days}\n'
            f'В месяцах: {sum_months: .3f}\n'
            f'В годах: {sum_years: .3f}')

    def __sub__(self, other):
        diff_days = self.all_day - other.all_day
        diff_months = (diff_days / 365)
        diff_years = diff_months / 12
        if diff_days < 0:
            print(
            f'\nРазница двух дат {self.name} и {other.name} равна:\n'
            f'В днях: {-diff_days}\n'
            f'В месяцах: {-diff_months: .3f}\n'
            f'В годах: {-diff_years: .3f}')
        else:
            print(
            f'\nРазница двух дат {self.name} и {other.name} равна:\n'
            f'В днях: {diff_days}\n'
            f'В месяцах: {diff_months: .3f}\n'
            f'В годах: {diff_years: .3f}')

test = MyCustomDate
custom_date_1 = MyCustomDate(11, 9, 2011)
custom_date_2 = MyCustomDate(30, 11, 1996)
custom_date_3 = MyCustomDate(8, 11, 2003)
custom_date_4 = MyCustomDate(3, 3, 2000)
custom_date_5 = MyCustomDate(18, 2, 1971)

def show (*args):
    for i in args:
        i.__str__()
show(custom_date_1, custom_date_2, custom_date_3, custom_date_4, custom_date_5)


def test_all(*args):
    for a in args:
        a(custom_date_1, custom_date_2)
        a(custom_date_3, custom_date_4)
test_all(
        test.__add__,
        test.__sub__,
        test.__eq__,
        test.__ne__,
        test.__lt__,
        test.__gt__,
        test.__le__,
        test.__ge__
        )
