from datetime import datetime


def convert2ampm(time24: str) -> str:
    return datetime.strptime(time24, '%H:%M').strftime('%I:%M%p')


flights = {'7:58': 'DENVER', '12:02': 'NEW YORK', '17:15': 'KYIV'}


# 1 standard way
just_kyiv = {}
for k, v in flights.items():
    if v == 'KYIV':
        just_kyiv[convert2ampm(k)] = v.title()


print(just_kyiv)


# 2 use generator
just_kyiv2 = {convert2ampm(k): v.title() for k, v in flights.items() if v == 'KYIV'}
print(just_kyiv2)