destinations = [
  'Paris, France', 
  'Shanghai, China', 
  'Los Angeles, USA', 
  'São Paulo, Brazil', 
  'Cairo, Egypt'
  ]
#print(destinations)

#set variable to access
test_traveler = [
  'Erin Wilkes', 
  'Shanghai, China', 
  ['historical site', 'art']
  ]

def get_destination_index(destination):
  destination_index = destinations.index(destination)
  return destination_index

#calling the function
# print(get_destination_index("Los Angeles, USA"))

def get_traveler_location(traveler):
  traveler_destination = test_traveler[1]
  traveler_destination_index = get_destination_index(traveler_destination)
  return traveler_destination_index

test_destination_index = get_traveler_location(test_traveler)

# print(test_destination_index)
#26
attractions = [[] for i in range(len(destinations))]
# print(attractions)

def add_attraction(destination, attraction):
  destination_index = get_destination_index(destination)
  attractions_for_destination = attractions[destination_index]
  attractions_for_destination.append(attraction)

#33
add_attraction('Los Angeles, USA', ['Venice Beach', ['beach']])

#34
# print(attractions)

#35
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("Los Angeles, USA", ["MOCA", ["art", "museum"]])
add_attraction("Los Angeles, USA", ["La Brea Tar Pits", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])

#38
def find_attractions(destination, interests):
  destination_index = get_destination_index(destination)
  attractions_in_city = attractions[destination_index]
  # print(attractions_in_city)
  attractions_with_interest = []
  for attraction in attractions_in_city:
    attraction_tags = attraction[1]
    # print(attraction_tags)
    for interest in interests:
      if interest in attraction_tags:
        attractions_with_interest.append(attraction[0])
        # print(attractions_with_interest)
  return attractions_with_interest
    
la_arts = find_attractions("Los Angeles, USA", ['art'])

# print(la_arts)

#53
def get_attractions_for_traveler(traveler):
  traveler_destination = traveler[1]
  traveler_interests = traveler[2]
  traveler_attractions = find_attractions(traveler_destination, traveler_interests)
  interests_string = "Hi " 
  if len(traveler_attractions) == 1:
    interests_string = interests_string + traveler[0] + ", we think you'll like this place around " + traveler[1] +": "
    for traveler_attraction in traveler_attractions:
      if len(traveler_attractions) == 1:
          interests_string += "the " + traveler_attraction + "."
      elif len(traveler_attractions) == 2:
        if traveler_attraction != traveler_attractions[-1]:
          interests_string += "the " + traveler_attraction
        else:
          interests_string += " and the " + traveler_attraction + "."
      else:
        if traveler_attraction != traveler_attractions[-1]:
          interests_string += "the " + traveler_attraction + ", "
        else:
          interests_string += "and the " + traveler_attraction + "."
  else:
    interests_string = interests_string + traveler[0] + ", we think you'll like these places around " + traveler[1] +": "
    for traveler_attraction in traveler_attractions:
      if len(traveler_attractions) == 1:
          interests_string += "the " + traveler_attraction + "."
      elif len(traveler_attractions) == 2:
        if traveler_attraction != traveler_attractions[-1]:
          interests_string += "the " + traveler_attraction
        else:
          interests_string += " and the " + traveler_attraction + "."
      else:
        if traveler_attraction != traveler_attractions[-1]:
          interests_string += "the " + traveler_attraction + ", "
        else:
          interests_string += "and the " + traveler_attraction + "."
  return interests_string

smills_france = get_attractions_for_traveler(['Dereck Smill', 'Paris, France', ['monument']])

print(" ")
print(smills_france )
print(" ")
print(get_attractions_for_traveler(test_traveler))
print(" ")
print(get_attractions_for_traveler(['Lara Robinson', 'Los Angeles, USA', ['museum']]))
