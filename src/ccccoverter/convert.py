import logging
import re

from .parse_dict import *
from .spilt import spilt_initials_finals, split_chinese_segment


def convert_single_syllable(syllable: str):
    """
    Convert a single Yuet-ping syllable to CCC syllable.
    :param syllable: A Yuet-ping syllable
    :return: str
    """
    initial, final = spilt_initials_finals(syllable)

    # Invalid item
    if initial == "" and final == "":
        return [""]

    initials_dict = get_initials_dict()
    finals_dict = get_finals_dict()

    if not initial == "":
        converted_initial = initials_dict.get(initial)
        if not converted_initial:
            logging.warning("Invalid initial {0} in syllable {1}.".format(initial, syllable))
            return [""]
    else:
        converted_initial = []

    converted_final = finals_dict.get(final)
    if not converted_final:
        logging.warning("Invalid final {0} in syllable {1}.".format(final, syllable))
        return [""]

    possible_combinations = []
    if initial == "":
        for item in converted_final:
            possible_combinations.append(item)
    else:
        for itema in converted_initial:
            for itemb in converted_final:
                possible_combinations.append(itema + itemb)

    return possible_combinations


def convert_single_character(char: str, only_keep_first_spell=False, only_keep_first_pronunciation=False):
    """
    Convert a single Chinese character to its CCC pronunciation
    :param char: The character
    :param only_keep_first_spell: If a pronunciation has multiple ways to spell,
    only keep this first one. False by default
    :param only_keep_first_pronunciation: If a character has multiple ways to pronounce,
    only keep the first pronunciation. False by default
    :return: str
    """
    assert len(char) == 1, "Not a single character"
    yuet_dict = get_yuet_dict()
    if char in yuet_dict.keys():
        yuet_ping = yuet_dict[char]
        possible_combinations = []
        for item in yuet_ping:
            if only_keep_first_spell:
                possible_combinations.append(str(convert_single_syllable(item)[0]))
            else:
                possible_combinations.append('/'.join(convert_single_syllable(item)))
            if only_keep_first_pronunciation:
                return '||'.join(possible_combinations)
        return '||'.join(possible_combinations)
    else:
        return ""


def convert_sentence(sentence: str, only_keep_first_spell=False, only_keep_first_pronunciation=False):
    """
    Convert a sentence with the right spelling of the original Chinese characters and keep the other element
    :param sentence: The sentence to be converted
    :param only_keep_first_spell: If a pronunciation has multiple ways to spell,
    only keep this first one. False by default
    :param only_keep_first_pronunciation: If a character has multiple ways to pronounce,
    only keep the first pronunciation. False by default
    :return: str
    """
    text_segments = split_chinese_segment(sentence)
    output_segments = []
    for item in text_segments:
        if re.match(re.compile(r"[\u4E00-\u9FFF\u3400-\u4DBF\uF900-\uFAFF\uE000-\uF8FF]$"), item):
            conversion = convert_single_character(item, only_keep_first_spell, only_keep_first_pronunciation)
            if not conversion:
                output_segments.append(item + "*")
            else:
                output_segments.append(conversion)
        else:
            output_segments.append(item)
    output = ' '.join(output_segments)
    return output


def convert_sentence_map(sentence: str, only_keep_first_spell=False, only_keep_first_pronunciation=False):
    """
    Convert a sentence to a list of (original, converted) items with the original sequence.
    :param sentence: The sentence to be converted
    :param only_keep_first_spell: If a pronunciation has multiple ways to spell,
    only keep this first one. False by default
    :param only_keep_first_pronunciation: If a character has multiple ways to pronounce,
    only keep the first pronunciation. False by default
    :return: list
    """
    text_segments = split_chinese_segment(sentence)
    output_segments = []
    for item in text_segments:
        if re.match(re.compile(r"[\u4E00-\u9FFF\u3400-\u4DBF\uF900-\uFAFF\uE000-\uF8FF]$"), item):
            conversion = convert_single_character(item, only_keep_first_spell, only_keep_first_pronunciation)
            if not conversion:
                output_segments.append((item, ""))
            else:
                output_segments.append((item, conversion))
        else:
            output_segments.append((item, ""))
    return output_segments


if __name__ == '__main__':
    a = convert_sentence_map("榕樹下")
    pass