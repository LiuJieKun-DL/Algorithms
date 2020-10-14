def bubble_sort(alist):
    """Bubble Sort"""
    n = len(alist)
    for j in range(n-1):
    #for j in range(len(alist),0,-1):
        count = 0
        for i in range(0,n-1-j):
        #for i in (j):
            # from head to tail
            if alist[i] > alist[i+1]:
                alist[i],alist[i+1] = alist[i+1],alist[i]
                count += 0
        if 0 == count:
            return




if __name__ == '__main__':
    list = [54,26,93,17,7,31,44,55,20]
    bubble_sort(list)
    print(list)
