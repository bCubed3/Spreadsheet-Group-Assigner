import random
from csv_to_dict import get_data


assignments_max = {
    "a": 1,
    "b": 1,
    "c": 1,
    "d": 1
}

assignments = {
    "a": [],
    "b": [],
    "c": [],
    "d": []
}

selections = get_data("Raw_data/choices.csv")

for person, choices in zip(selections, selections.values()):
    assignments[choices[0]].append(person)

all_assigned = False
iterations = 1

while not all_assigned:
    to_reassign = []
    all_assigned = True
    for option, people in zip(assignments, assignments.values()):
        if len(people) > assignments_max[option]:
            # add in a random.shuffle(people) if a random selection is wanted
            to_reassign += people[assignments_max[option]:]
            assignments[option] = assignments[option][:assignments_max[option]]
            print(to_reassign)
            print(assignments)
            all_assigned = False
    to_remove = []
    for person in to_reassign:
        if iterations + 1 > len(selections[person]):
            for option, assigned in zip(assignments, assignments.values()):
                if assignments_max[option] > len(assigned):
                    assignments[option].append(person)
                    break
            else:
                print(person)
        else:
            assignments[selections[person][iterations]].append(person)
    iterations += 1

print(assignments)
