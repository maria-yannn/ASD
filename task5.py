# сложность: все, кроме сортировки, O(n), сортировка O(n log n)
# итого O(n log n) по времени и O(n) по памяти

import re
from datetime import date, timedelta


def next_day(s):
    # "2024-06-20" -> "2024-06-21"
    d = date.fromisoformat(s)
    return str(d + timedelta(days=1))


s = '[("2024-06-01", "2024-06-20"), ("2024-06-05", "2024-06-15"), ("2024-06-08", "2024-06-12"), ("2024-06-10", "2024-06-25"), ("2024-06-10", "2024-06-11"), ("2024-06-10", "2024-06-18"), ("2024-06-12", "2024-06-14"), ("2024-06-15", "2024-06-16"), ("2024-06-22", "2024-06-28")]'
# s = input()

# вытаскиваем все даты подряд, так не важно, какие там кавычки
found = re.findall(r'\d{4}-\d{2}-\d{2}', s)

# собираем обратно пары (заезд, отъезд)
guests = []
for i in range(0, len(found) - 1, 2):
    guests.append((found[i], found[i + 1]))

# каждый гость = два события:
# +1 в день заезда, -1 на следующий день после отъезда
# (в день отъезда гость еще в отеле)
events = []
for check_in, check_out in guests:
    events.append((check_in, 1))
    events.append((next_day(check_out), -1))

# даты в формате ГГГГ-ММ-ДД сортируются как обычные строки
# при одинаковой дате -1 идет раньше +1, т.е. сначала уезжают, потом заезжают
events.sort()

cur = 0       # сколько гостей сейчас
best = 0      # максимум
best_day = None

for day, delta in events:
    cur += delta
    if cur > best:  # строго больше -> берем самый ранний день с максимумом
        best = cur
        best_day = day

if best_day is None:
    print("гостей нет")
else:
    print(best_day, "количество гостей =", best)