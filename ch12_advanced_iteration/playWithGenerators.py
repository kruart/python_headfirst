from datetime import datetime

flights = {'7:58': 'DENVER', '12:02': 'NEW YORK', '17:15': 'KYIV'}

# 1 - standard way
destinations = []
for dest in flights.values():
    destinations.append(dest.title())

print(destinations)


# 2 - use generators, the same result in more short way
more_dests = [dest.title() for dest in flights.values()]
print(more_dests)


def convert2ampm(time24: str) -> str:
    return datetime.strptime(time24, '%H:%M').strftime('%I:%M%p')


# 3 - standard way
flights2 = {}
for k, v in flights.items():
    flights2[convert2ampm(k)] = v.title()

print(flights2)

# 4 - use generators for dict
more_flights = {convert2ampm(k): v.title() for k, v in flights.items()}
print(more_flights)
