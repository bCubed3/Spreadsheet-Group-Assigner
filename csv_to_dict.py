def get_data(filename="Raw_data/choices.csv", id_column=1, choices_column=2):
    with open(filename) as file:
        data = list(file.read().split("\n"))
        data_dict = {}
        for index, answer in enumerate(data):
            data[index] = answer.split(", ")
            data_dict[data[index][id_column - 1]] = data[index][choices_column - 1:]
        return data_dict
