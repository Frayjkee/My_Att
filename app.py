def filter_short_strings(arr):
    result = []
    for string in arr:
        if len(string) <= 3:
            result.append(string)
    return result
def main():
    # Ввод массива строк с клавиатуры
    arr = input("Введите элементы массива через пробел: ").split()