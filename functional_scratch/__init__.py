import functools

people = [{'name': 'Mary', 'height': 160},
          {'name': 'Isla', 'height': 80},
          {'name': 'Sam'}]

people_with_height = list(filter(lambda person: True if 'height' in person else False, people))

print(functools.reduce(lambda average, person: average + person['height'],
                       people_with_height,
                       0) / len(people_with_height))
