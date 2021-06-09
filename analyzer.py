from random import randint
from quickSort import quicksort
from mergeSort import mergesort
from bubbleSort import bubbleSort
import time

def user_int_list(list_size, max_value):
    new_list = []
    for num in range(list_size):
        new_list.append(randint(1, max_value))

    return new_list

def analyze_func(func_name, arr):
    tic = time.time()
    func_name(arr)
    toc = time.time()
    seconds = toc - tic
    print(f"{func_name.__name__.capitalize()}\t-> Elapsed Time: {seconds:.5f}")


list_size = int(input("What size list do you want to create?"))
max_value = int(input("What is the max value of the range?"))
executions = int(input("How many times do you want to run?"))

list_size = 500
max_value = 100
executions = 2

for num in range(0, executions):
    print("-" * 40)
    print(f"Run: {num+1}")
    l = user_int_list(list_size, max_value)
    analyze_func(bubbleSort, l.copy())
    analyze_func(quicksort, l)
    analyze_func(mergesort, l)
    analyze_func(sorted, l)
