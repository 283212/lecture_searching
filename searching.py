from pathlib import Path
import json


def read_data(file_name, field):
    """
    Reads a JSON file and returns data for a given field.

    Args:
        file_name (str): Name of the JSON file.
        field (str): Key to retrieve from the JSON data.
            Must be one of: 'unordered_numbers', 'ordered_numbers' or 'dna_sequence'.

    # # Returns:
    #     list | str | None:
    #          - list: If data retrieved by the selected field contains numeric data.
    # #        - str: If field is 'dna_sequence'.
    #          - None: If the field is not supported.
    """

    cwd_path = Path.cwd()
    
    file_path = cwd_path / file_name

    with open(file_path, "r") as file:
        data = json.load(file)

    if field in data:
        return data[field]

    return None




def linear_search(prohledavana_sekvence, hledane_cislo):

    slovnik = {}
    slovnik["count"] = 0


    for index, hodnota in enumerate(prohledavana_sekvence):
        if hodnota == hledane_cislo:
            slovnik["positions"].append(index)
            slovnik["count"] += 1
            continue

    return slovnik







def main():

    sequential_data = read_data("sequential.json", "unordered_numbers")
    print(sequential_data)
    slovnik = linear_search(prohleda, hleda)
    print(slovnik)



if __name__ == "__main__":
    main()
