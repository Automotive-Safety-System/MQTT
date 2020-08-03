import re


def copy_list(list, first_index, last_index):
    cpd_list = []
    for i in range(first_index, last_index + 1):
        cpd_list.append(list[i])
    return cpd_list


def parse_for_OTA():
    with open('outputFile.txt', 'r') as reader:
        patch_str = ''
        c = reader.read(1)
        while True:
            c = reader.read(1)
            if c == '}':
                break
            patch_str += c
    hex_list = []
    for item in patch_str.split(','):
        hex_list.append(re.sub(r"\s+", "", item))

    list = [1, 5, 9, 7, 8, 4, 8, 5, 9, 8]

    item_count = 0
    seg_count = 0
    hex_divided_list = []
    while len(hex_list) - item_count >= 100:
        for i in range(0, int(len(hex_list) / 100)):
            hex_divided_list.append(copy_list(hex_list, item_count, item_count + 99))
            item_count += 100

    hex_divided_list.append(copy_list(hex_list, item_count, len(hex_list) - 1))

    hex_string_list = []
    for item in hex_divided_list:
        hex_string_list.append(",".join(item))

    return hex_string_list
