import random
from csv_to_dict import get_data


assignments_max = {
    "France WHO" : 1,
    "Brazil WHO" : 1,
    "Canada WHO" : 1,
    "Vietnam WHO" : 1,
    "Brazil UNEP" : 1,
    "Canada UNEP" : 1,
    "France UNEP" : 1,
    "Vietnam UNEP" : 1,
    "Brazil SOCHUM" : 1,
    "Canada SOCHUM" : 1,
    "France SOCHUM" : 1,
    "Vietnam SOCHUM" : 1,
    "Brazil DISEC" : 1,
    "Canada DISEC" : 1,
    "France DISEC" : 1,
    "Vietnam DISEC" : 1,
    "Brazil SPECPOL" : 1,
    "Canada SPECPOL" : 1,
    "France SPECPOL" : 1,
    "Vietnam SPECPOL" : 1,
    "Vietnam UNESCO" : 1,
    "France UNESCO" : 1,
    "Brazil UNESCO" : 1,
    "Canada UNESCO" : 1,
    "France UNSC" : 1,
    "Vietnam UNSC" : 1,
    "Brazil UNODC" : 1,
    "France UNODC" : 1,
    "Vietnam UNODC" : 1,
    "Benjamin Franklin" : 1,
    "Ben Shapiro" : 1,
    "Morpheus" : 1,
    "Pan" : 1,
    "Lafayette" : 1,
    "LGG" : 1
}

assignments = {
    "France WHO" : [],
    "Brazil WHO" : [],
    "Canada WHO" : [],
    "Vietnam WHO" : [],
    "Brazil UNEP" : [],
    "Canada UNEP" : [],
    "France UNEP" : [],
    "Vietnam UNEP" : [],
    "Brazil SOCHUM" : [],
    "Canada SOCHUM" : [],
    "France SOCHUM" : [],
    "Vietnam SOCHUM" : [],
    "Brazil DISEC" : [],
    "Canada DISEC" : [],
    "France DISEC" : [],
    "Vietnam DISEC" : [],
    "Brazil SPECPOL" : [],
    "Canada SPECPOL" : [],
    "France SPECPOL" : [],
    "Vietnam SPECPOL" : [],
    "Vietnam UNESCO" : [],
    "France UNESCO" : [],
    "Brazil UNESCO" : [],
    "Canada UNESCO" : [],
    "France UNSC" : [],
    "Vietnam UNSC" : [],
    "Brazil UNODC" : [],
    "France UNODC" : [],
    "Vietnam UNODC" : [],
    "Benjamin Franklin" : [],
    "Ben Shapiro" : [],
    "Morpheus" : [],
    "Pan" : [],
    "Lafayette" : [],
    "LGG" : []
}

# import from csv
selections = get_data("Raw_data/choices.csv", 0, 1)

# array for people who did not fill out the form
no_choices = []
# assign everyone to their first choice
for person, choices in zip(selections, selections.values()):
    if not choices:
        no_choices.append(person)
    else:
        assignments[choices[0]].append(person)

all_assigned = False
iterations = 1

# iterate until everyone is assigned and no group has more than the max it can be assigned
while not all_assigned:
    # array of people who are in excess of their group (order is probably based on the order in which they filled
    # out the form)
    to_reassign = []
    all_assigned = True
    # loop through all assignment and find those that have people in excess
    # remove those people and put them in the "to_reassign" list
    for option, people in zip(assignments, assignments.values()):
        if len(people) > assignments_max[option]:
            # add in a random.shuffle(people) if a random selection is wanted
            to_reassign += people[assignments_max[option]:]
            assignments[option] = assignments[option][:assignments_max[option]]
            all_assigned = False
    # reassign people to their next choice. If none, assign them to the first empty group
    for person in to_reassign:
        if iterations + 1 > len(selections[person]):
            for option, assigned in zip(assignments, assignments.values()):
                if assignments_max[option] > len(assigned):
                    assignments[option].append(person)
                    break
            else:
                print("There has been an error with {}".format(person))
        else:
            assignments[selections[person][iterations]].append(person)
    iterations += 1

# assign people who did not fill out their choices
for person in no_choices:
    for assignment in assignments:
        if len(assignments[assignment]) < assignments_max[assignment]:
            assignments[assignment].append(person)
            break

for key in assignments:
    print(key, ":", assignments[key][0])
