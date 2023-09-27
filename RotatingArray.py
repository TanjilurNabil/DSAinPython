nums = [19, 24, 29, 3, 5, 7, 14]


def count_rotations_binary(nums):
    lo = 0
    hi = len(nums)-1

    while lo <= hi:
        mid = (lo+hi)//2
        mid_number = nums[mid]

        # Uncomment the next line for logging the values and fixing errors.
        print("lo:", lo, ", hi:", hi, ", mid:",
              mid, ", mid_number:", mid_number)

        if mid > 0 and nums[mid] < nums[mid]-1:
            # The middle position is the answer
            return mid

        elif nums[mid] < nums[hi]:
            # Answer lies in the left half
            hi = mid - 1

        else:
            # Answer lies in the right half
            lo = mid + 1

    return -1


def main(arr):
    return count_rotations_binary(arr)
