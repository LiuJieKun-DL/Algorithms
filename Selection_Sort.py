def select_sort(alist):
    """selection sort"""
    n = len(alist)

    for j in range(n-1):
        min_index = j
        for i in range(j+1,n):
            if alist[min_index] > alist[i]:
                min_index = i
        alist[j],alist[min_index] = alist[min_index],alist[j]
if __name__ == '__main__':
    list = [54,26,93,17,7,31,44,55,20]
    select_sort(list)
    print(list)


