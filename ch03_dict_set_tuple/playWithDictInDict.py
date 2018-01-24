from pprint import pprint

# Map<String, Map>
people = {      # add 4 items
    'Ford': {'Name': 'Ford Prefect', 'Gender': 'Male', 'Occupation': 'Researcher', 'Home Planet': 'Betelgeuse Seven'},
    'Arthur': {'Name': 'Arthur Dent', 'Gender': 'Male', 'Occupation': 'Sandwich-Maker', 'Home Planet': 'Earth'},
    'Trillian': {'Name': 'Tricia McMillan', 'Gender': 'Female', 'Occupation': 'Mathematician', 'Home Planet': 'Earth'},
    'Robot': {'Name': 'Marvin', 'Gender': 'Unknown', 'Occupation': 'Paranoid Android', 'Home Planet': 'Unknown'}
}

print(people)   # ugly print :)
pprint(people)  # pretty print
print('========================')
print(people['Arthur']['Occupation'])   # Sandwich-Maker