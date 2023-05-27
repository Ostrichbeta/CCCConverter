import csv
import pathlib


dict_path = pathlib.Path(__file__).parent.parent.joinpath('dict')


def get_initials_dict():
    """
    Get the all the initials of the Yuet-ping dictionary and convert it to a dictionary variable.
    :return: dict
    """
    with open(dict_path.joinpath('initials.csv'), 'r', newline='') as initials_csv:
        reader = csv.reader(initials_csv, delimiter=',', quotechar='|')
        initials_list = [x for x in reader][1:]
        initials_csv.close()

    for idx, item in enumerate(initials_list):
        initials_list[idx][1] = str(item[1]).split("/")

    initials_dict = {x[0]: x[1] for x in initials_list}

    return initials_dict


def get_finals_dict():
    """
    Get the all the finals of the Yuet-ping and convert it to a dictionary variable.
    :return: dict
    """
    with open(dict_path.joinpath('finals.csv'), 'r', newline='') as finals_csv:
        reader = csv.reader(finals_csv, delimiter=',', quotechar='|')
        finals_list = [x for x in reader][1:]
        finals_csv.close()

    for idx, item in enumerate(finals_list):
        finals_list[idx][1] = str(item[1]).split("/")

    finals_dict = {x[0]: x[1] for x in finals_list}

    return finals_dict


def get_yuet_dict():
    """
    Get the elements from the Yuet-ping dictionary and convert it to a dictionary variable.
    :return: dict
    """
    with open(dict_path.joinpath('yuet_dict.csv'), 'r', newline='') as yuet_dict_csv:
        reader = csv.reader(yuet_dict_csv, delimiter=',', quotechar='|')
        kanji_list = [x for x in reader][1:]
        yuet_dict_csv.close()

        for idx, item in enumerate(kanji_list):
            kanji_list[idx][1] = str(item[1]).split("/")

    kanji_dict = {x[0]: x[1] for x in kanji_list}
    return kanji_dict

