import random
from csv_to_dict import get_data


assignments_max = {
    "a": 1,
    "b": 2,
    "c": 1,
    "d": 1
}

assignments = {
    "a": [],
    "b": [],
    "c": [],
    "d": []
}

# import from csv
selections = get_data("Raw_data/choices.csv")

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

print(assignments)
