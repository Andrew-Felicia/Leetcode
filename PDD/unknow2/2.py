import sys


def maximum_animals(daily_food, fruits):
    n = len(daily_food)
    costs = [food * (n - day) for day, food in enumerate(daily_food)]
    costs.sort()
    accepted = 0
    for cost in costs:
        if cost > fruits:
            break
        fruits -= cost
        accepted += 1
    return accepted


def main():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    n, fruits = numbers[0], numbers[1]
    print(maximum_animals(numbers[2:2+n], fruits))


if __name__ == "__main__":
    main()
