import logging
import re
import csv
from .parse_dict import *


def spilt_initials_finals(syllable: str):
    """
    Spilt the initial and final part from a syllable
    :param syllable: A Yuet-ping syllable, with or without the tone
    :return:
    """
    yuetping_pattern = re.compile(r"[a-z]*[1-6]?")
    initial = ""
    final = ""

    if not re.match(yuetping_pattern, syllable):
        # Invalid yuetping format
        logging.warning("Invalid yuetping syllable {0}.".format(syllable))
        return initial, final

    initials_list = get_initials_dict().keys()
    finals_list = get_finals_dict().keys()

    # Check if there are only finals
    for item in finals_list:
        match_pattern = re.match(re.compile(r"({0})[1-6]?$".format(item)), syllable)
        if match_pattern:
            initial = ""
            final = item
            return initial, final

    # If there are initials, match the initials first
    for item in initials_list:
        match_pattern = re.match(re.compile(r"({0})[a-z]*[1-6]?$".format(item)), syllable)
        if match_pattern:
            initial = item
            break

    # then the finals
    for item in finals_list:
        match_pattern = re.match(re.compile(r"[a-z]*({0})[1-6]?$".format(item)), syllable)
        if match_pattern:
            final = item
            break

    return initial, final


def split_chinese_segment(sentence: str):
    """
    Split the Chinese segments from a sentence for Yuet-ping conversion
    :param sentence: The sentence to be split
    :return: list
    """
    segment_parts = []
    buffer = ''
    for item in sentence:
        if re.match(re.compile(r"[\u4E00-\u9FFF\u3400-\u4DBF\uF900-\uFAFF\uE000-\uF8FF]$"), item):
            if buffer:
                segment_parts.append(buffer)
            segment_parts.append(item)
            buffer = ''
        else:
            buffer = buffer + item
    if buffer:
        segment_parts.append(buffer)
    segment_parts = [str(x).strip() for x in segment_parts]
    return segment_parts
