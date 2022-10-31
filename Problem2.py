#!/usr/bin/python3
n = 21
# Your code should be below this line
def switch(day):
    return {
        0: "Weekend",
        1: "Weekend",
        2: "Weekday",
        3: "Weekday",
        4: "Weekday",
        5: "Weekday",
        6: "Weekday",
    }[day]

if 1 <= n <= 31:
    # Zeller congruence formula
    m = 13  # January
    year = 2021  # 2022 - 1
    k = year % 100
    j = year // 100
    h = n + 13 * (m + 1) // 5 + k + k // 4 + j // 4 + 5 * j
    h = h % 7
    print(switch(h))
else:
    print("Not valid")
