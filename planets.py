planet_list = ["Mercury", "Mars"]

planet_list.append('Jupiter')
planet_list.append('Saturn')
print(planet_list)
planet_list.extend(['Uranus', 'Neptune', 'Pluto'])
print(planet_list)
planet_list.insert(1, 'Venus')
planet_list.insert(2, 'Earth')
print(planet_list)
#This is Python's slice method [i:i]
rocky_planets = planet_list[0:4]
print(rocky_planets)
#Remove Pluto from the end of the list
del planet_list[8]
print(planet_list)
