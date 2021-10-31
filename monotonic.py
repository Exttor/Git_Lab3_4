def is_monotonic(nums):
    list1 = nums
    k = 0
    n = 0
    
    for i in list1:
        n += 1
    
    bool = True
    while k < (n - 2):
        if bool:
            if list1[k] <= list1[k+1] <= list1[k+2] or list1[k] >= list1[k+1] >= list1[k+2]:
                k += 1                
            else:
                bool = False
        else:
            break
    return bool
