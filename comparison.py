import random
import timeit
from pprint import pprint
import matplotlib.pyplot as plt


def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    return lst


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    # Спочатку об'єднайте менші елементи
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Якщо в лівій або правій половині залишилися елементи,
    # додайте їх до результату
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged


def generate_random_array(size):
    return [random.randint(0, 10000) for _ in range(size)]


sizes = [100, 1000, 10000]

insertion_sort_times = {100: [], 1000: [], 10000: []}
merge_sort_times = {100: [], 1000: [], 10000: []}
timsort_times = {100: [], 1000: [], 10000: []}

for _ in range(10):
    for size in sizes:
        arr = generate_random_array(size)

        insertion_sort_time = timeit.timeit('insertion_sort(arr.copy())', number=1, globals=globals())
        insertion_sort_times[size].append(insertion_sort_time)

        merge_sort_time = timeit.timeit('merge_sort(arr.copy())', number=1, globals=globals())
        merge_sort_times[size].append(merge_sort_time)

        timsort_time = timeit.timeit('sorted(arr.copy())', number=1, globals=globals())
        timsort_times[size].append(timsort_time)

insertion_sort_times = {k: sum(v)/len(v) for k, v in insertion_sort_times.items()}
merge_sort_times = {k: sum(v)/len(v) for k, v in merge_sort_times.items()}
timsort_times = {k: sum(v)/len(v) for k, v in timsort_times.items()}

print("Вставка",)
pprint(insertion_sort_times)
print("Злиття",)
pprint(merge_sort_times)
print("Тімсорт",)
pprint(timsort_times)

ts_to_merge = {ts[0]: other[1]/ts[1] for ts, other in zip(timsort_times.items(), merge_sort_times.items())}
ts_to_insertion = {ts[0]: other[1]/ts[1] for ts, other in zip(timsort_times.items(), insertion_sort_times.items())}
print("Вставка / тімсорт",)
pprint(ts_to_insertion)
print("Злиття / тімсорт",)
pprint(ts_to_merge)

plt.figure()
plt.plot(sizes, insertion_sort_times.values(), label="Insertion")
plt.plot(sizes, merge_sort_times.values(), label="Merge")
plt.plot(sizes, timsort_times.values(), label="Timsort")
plt.legend()
plt.show()
