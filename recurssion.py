def recurssion(nums):
    if nums == 1:
        return 1
    else:
        return nums+recurssion(nums-1)


def sum():
    number = 10
    result = recurssion(number)
    print("Sum of number 1 to %d" % number % result)
