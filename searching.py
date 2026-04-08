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
    seznam_indexu = []
    pocet = 0


    for index, hodnota in enumerate(prohledavana_sekvence):
        if hodnota == hledane_cislo:
            seznam_indexu.append(index)
            pocet += 1
            continue

    slovnik["positions"] = seznam_indexu
    slovnik["count"] = pocet

    return slovnik



def binary_search(prohledavany_seznam, hledane_cislo):

    index_pul = 0

    while True:

        index_middle = int((len(prohledavany_seznam) / 2) -1)
        middle = prohledavany_seznam[index_middle]

        if hledane_cislo == middle:
            return index_middle

        if hledane_cislo > middle:
            prohledavany_seznam = prohledavany_seznam[index_middle:]
            index_pul += index_middle + 1
            continue

        if hledane_cislo < middle:
            prohledavany_seznam = prohledavany_seznam[:index_middle]

            continue

    return None






def main():

    sequential_data = read_data("sequential.json", "unordered_numbers")
    print(sequential_data)
    slovnik = linear_search(sequential_data, 2)
    print(slovnik)



if __name__ == "__main__":
    main()
