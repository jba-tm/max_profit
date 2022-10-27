from itertools import combinations


def max_profit(data: list):
    #
    # Write your code here.
    #
    min_value = 0
    max_value = 0
    current_value = 0

    for i, value in enumerate(data):
        if value < data[current_value]:
            current_value = i
        profit = data[max_value] - data[min_value]
        candidate = data[i] - data[current_value]
        if candidate > profit:
            min_value = current_value
            max_value = i
    if min_value == 0 and max_value == 0:
        return []
    return [min_value, max_value]


def main():
    data = [10, 9, 8, 8, 7, 4, 5, 5]

    # result = {}
    # for i, item in enumerate(data):
    #     last_index = data[i + 1:]
    #     if not last_index:
    #         break
    #     max_profit = max(data[i + 1:])
    #     result[item] = {
    #         'max_profit':
    #     }

    print(max_profit(data))


if __name__ == "__main__":
    main()
