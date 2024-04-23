def filter_short_strings(arr):
    result = []
    for string in arr:
        if len(string) <= 3:
            result.append(string)
    return result