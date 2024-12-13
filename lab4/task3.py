from my_pkg import sorters, stopwatch, str_tools as st
import random

def rev(n:int):
    '''returns reversed range of length n'''
    return list(range(n)[::-1])

def rand_list(n:int):
    l = []
    for i in range(n):
        l.append(random.randint(0, 1000))
    return l

@stopwatch.func_time
def bubble(r,n):
    print(f'bubble sort of {n} items time:', end=' ')
    sorters.bubble_sort(r)


@stopwatch.func_time
def std(r,n):
    print(f'python std sort of {n} items time:', end=' ')
    sorters.std_sort(r)


@stopwatch.func_time
def choise(r,n):
    print(f'choise sort of {n} items time:', end=' ')
    with open('sorted_list.txt', 'w+') as f:
        f.write(str(sorters.choise_sort(r)))

n = int(input("how many elements in your array? "))
r = rev(n)
std(r, n)
# choise(r, n)
# bubble(r, n)

# lstr = 'LOWER'
# ustr = 'upper'
# cstr = 'capitalize'
# print('\n', f"{cstr} -> {st.capital(cstr)}\n", f"{lstr} -> {st.lowercase(lstr)}\n", f"{ustr} -> {st.uppercase(ustr)}\n")
