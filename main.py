import time
import random
from sorts.bubble_sort import bubble_sort
from sorts.selection_sort import selection_sort
from sorts.insertion_sort import insertion_sort
from sorts.merge_sort import merge_sort
from sorts.quick_sort import quick_sort

def get_input_array():
    user_input = input("Enter comma-separated numbers OR type 'random N': ").strip()
    if user_input.startswith("random"):
        _, n = user_input.split()
        return [random.randint(1, 100) for _ in range(int(n))]
    else:
        return list(map(int, user_input.split(',')))

def main():
    algorithms = {
        "1": ("Bubble Sort", bubble_sort),
        "2": ("Selection Sort", selection_sort),
        "3": ("Insertion Sort", insertion_sort),
        "4": ("Merge Sort", merge_sort),
        "5": ("Quick Sort", quick_sort)
    }

    print("Welcome to Sorting Visualizer!")
    for key, (name, _) in algorithms.items():
        print(f"{key}. {name}")

    choice = input("Choose an algorithm (1-5): ").strip()
    if choice not in algorithms:
        print("Invalid choice.")
        return

    arr = get_input_array()
    show_steps = input("Show sorting steps? (yes/no): ").lower() == "yes"

    print(f"\nUsing {algorithms[choice][0]} on: {arr}\n")

    start = time.time()
    sorted_arr, comparisons, swaps = algorithms[choice][1](arr.copy(), show_steps)
    end = time.time()

    print("\n✅ Sorted Array:", sorted_arr)
    print(f"🧮 Comparisons: {comparisons}")
    print(f"🔁 Swaps/Recursions: {swaps}")
    print(f"⏱️ Time Taken: {end - start:.5f} seconds")

if __name__ == "__main__":
    main()
