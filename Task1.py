import random
import time
import matplotlib.pyplot as plt
import pandas as pd


# --------------------------
# Deterministic QuickSort
# --------------------------
def deterministic_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[-1]  # deterministyczny pivot - ostatni element
    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]
    return deterministic_quick_sort(left) + [pivot] + deterministic_quick_sort(right)


# --------------------------
# Randomized QuickSort
# --------------------------
def randomized_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot_index = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_index]
    left = [x for i, x in enumerate(arr) if i != pivot_index and x <= pivot]
    right = [x for i, x in enumerate(arr) if i != pivot_index and x > pivot]
    return randomized_quick_sort(left) + [pivot] + randomized_quick_sort(right)


# --------------------------
# Pomiar czasu wykonania
# --------------------------
def measure_time(sort_func, arr, repeats=5):
    times = []
    for _ in range(repeats):
        copy_arr = arr[:]  # kopia, żeby nie sortować już posortowanej
        start = time.perf_counter()
        sort_func(copy_arr)
        end = time.perf_counter()
        times.append(end - start)
    return sum(times) / len(times)


if __name__ == "__main__":
    sizes = [10_000, 50_000, 100_000, 500_000]
    results = {"Array Size": [], "Randomized QuickSort (s)": [], "Deterministic QuickSort (s)": []}

    for size in sizes:
        arr = [random.randint(0, 1_000_000) for _ in range(size)]
        rand_time = measure_time(randomized_quick_sort, arr)
        det_time = measure_time(deterministic_quick_sort, arr)

        results["Array Size"].append(size)
        results["Randomized QuickSort (s)"].append(rand_time)
        results["Deterministic QuickSort (s)"].append(det_time)

    # --------------------------
    # Tabela wyników
    # --------------------------
    df = pd.DataFrame(results)
    print("\n=== Wyniki porównania ===\n")
    print(df.to_string(index=False))

    # --------------------------
    # Wykres porównawczy
    # --------------------------
    plt.plot(df["Array Size"], df["Randomized QuickSort (s)"], marker='o', label="Randomized QuickSort")
    plt.plot(df["Array Size"], df["Deterministic QuickSort (s)"], marker='o', label="Deterministic QuickSort")
    plt.xlabel("Array size")
    plt.ylabel("Average execution time (s)")
    plt.title("Randomized vs Deterministic QuickSort Performance")
    plt.legend()
    plt.grid(True)
    plt.show()

    # --------------------------
    # Analiza
    # --------------------------
    print("\n--- Analysis ---")
    print("1. Obie wersje mają średnią złożoność O(n log n).")
    print("2. Deterministyczny QuickSort może trafić na najgorszy przypadek (O(n^2)) przy niekorzystnych danych.")
    print("3. Randomizowany QuickSort redukuje ryzyko najgorszego przypadku przez losowy wybór pivota.")
    print("4. Wyniki pokazują, że dla dużych tablic wersja randomizowana jest zwykle stabilniejsza i minimalnie szybsza.")