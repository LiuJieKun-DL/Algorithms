def insert_sort(alist):
    """Insert Sort"""
    n = len(alist)
    for j in range(1,n):
        i = j
        while i>0:
            if alist[i] < alist[i-1]:
                alist[i],alist[i-1] = alist[i-1],alist[i]
                i-=1
            else:
                break
if __name__ == '__main__':
    list = [54,26,93,17,7,31,44,55,20]
    insert_sort(list)
    print(list)


