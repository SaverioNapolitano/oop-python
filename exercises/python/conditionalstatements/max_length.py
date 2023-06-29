def max_length(first_string, second_string):
    if isinstance(first_string, str) and isinstance(second_string, str):
        (print(first_string), print(second_string)) if len(first_string) == len(second_string) else print(
            max(first_string, second_string))
