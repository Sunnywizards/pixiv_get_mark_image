import math

from locale import atof, setlocale, LC_NUMERIC
from util.constant import MAX_IMG_NUM_ONE_PAGE


def str_to_int(str_num: str):
    """
    convert "1,000" to 1000
    :param str_num:
    :return: int
    """
    setlocale(LC_NUMERIC, 'English_US')
    return int(atof(str_num))


def get_page_num(input_mark_num: int):
    return math.ceil(input_mark_num / MAX_IMG_NUM_ONE_PAGE)
