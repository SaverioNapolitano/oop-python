def count_alpha_num(string):
    if isinstance(string, str):
        return {'digits': len({key: value for key, value in enumerate(string) if value.isdigit()}),
                'letters': len({key: value for key, value in enumerate(string) if value.isalpha()})}
