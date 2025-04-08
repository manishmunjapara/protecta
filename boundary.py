# boundarychecker/checker.py

class boundary:
    def __init__(self):
        pass

    def is_within_range(self, value, min_val, max_val):
        return min_val <= value <= max_val

    def is_positive(self, value):
        return value > 0

    def is_negative(self, value):
        return value < 0

    def is_zero(self, value):
        return value == 0

    def is_even(self, value):
        return value % 2 == 0

    def is_odd(self, value):
        return value % 2 != 0

    def in_list(self, value, valid_list):
        return value in valid_list

    def not_in_list(self, value, invalid_list):
        return value not in invalid_list

    def is_length_between(self, string, min_len, max_len):
        return min_len <= len(string) <= max_len

    def is_type(self, value, expected_type):
        return isinstance(value, expected_type)
