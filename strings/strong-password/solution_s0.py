class Solution:

    #
    # Complete the 'minimumNumber' function below.
    #
    # The function is expected to return an INTEGER.
    # The function accepts following parameters:
    #  1. INTEGER n
    #  2. STRING password
    #
    def minimumNumber(self, n, password):
        n = len(password)
        miss_len = 0 if n >= 6 else 6 - n

        numbers = set("0123456789")
        lower_case = set("abcdefghijklmnopqrstuvwxyz")
        upper_case = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        special_characters = set("!@#$%^&*()-+")

        has_number = False
        has_lower = False
        has_upper = False
        has_special = False
        total_miss_types = 4

        for ch in set(password):
            has_number = has_number or ch in numbers
            has_lower = has_lower or ch in lower_case
            has_upper = has_upper or ch in upper_case
            has_special = has_special or ch in special_characters
            total_miss_types = 4 - has_number - has_lower - has_upper - has_special
            if not total_miss_types:
                break
        return max(miss_len, total_miss_types)
