def bubble_sort(l:list) -> list:
    sorted = False
    i = 0
    while not sorted:
        sorted = True
        for j in range(len(l)-1):
             if l[j] > l[j+1]:
                  sorted = False
        if l[i] > l[i+1]:
            sorted = False
            l[i], l[i+1] = l[i+1], l[i]
        if i < len(l)-2:
                i+=1
        else: i = 0
    return l

def choise_sort(l:list) -> list:
        for i in range(len(l)-1):
            for j in range(i, len(l)-1):
                if l[i] > l[j]:
                    l[i], l[j] = l[j], l[i]
        return l

def std_sort(l:list) -> list:
    return sorted(l)

def q_sort(l:list) -> list:
    
    return l

if __name__ == '__main__':
    def not_to_use():
        nums = list(map(int, input().split()))
        print(bubble_sort(nums))
        print(std_sort(nums))
    not_to_use()
