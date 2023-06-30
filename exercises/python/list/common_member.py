def common_member(first_list, second_list):
    return bool(len([item for item in first_list if item in second_list]))