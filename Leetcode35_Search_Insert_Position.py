nums = [1, 3, 5, 6, 7, 9]
target = 5


def binary_search(lo, hi, condition):
    while lo <= hi:
        mid = (lo+hi)//2
        result = condition(mid)
        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid-1
        else:
            lo = mid+1
            # return -1
    return indexOfInsertforLeft(lo, hi, result)


def find(num, target):
    def condition(mid):
        if num[mid] == target:
            if mid > 0 and num[mid-1] == target:
                return 'left'
            return 'found'
        elif num[mid] < target:
            return 'right'
        else:
            return 'left'
    return binary_search(0, len(num)-1, condition)


def indexOfInsertforLeft(lo, hi, result):
    if result == "right":
        return hi+1
    else:
        return lo
    # voyonkor hassokor solution
    # totaly customized by debugging code
    # when the element is not found at that time lo value gets higher than hi value
    # i write bullshit code


print(find(nums, target))
