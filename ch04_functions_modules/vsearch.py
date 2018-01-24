def search4vowels(phrase: str) -> set:
    """Return any vowels found in a supplied phrase."""
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))


def search4letters(phrase: str, letters: str='aeiou') -> set:   # letters is optional arg
    """Return a set of the 'letters' found in 'phrase'."""
    return set(letters).intersection(set(phrase))


print(search4vowels('hitch-hiker'))
print(search4vowels('galaxy'))
print(search4vowels('sky'))

print(search4letters('hitch-hiker', 'hit'))
print(search4letters('hitch-hiker'))
print(search4letters(letters='xyz', phrase='galaxy'))       # named args
