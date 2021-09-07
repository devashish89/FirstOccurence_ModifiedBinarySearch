# first occurrence of element using Modified Binary Tree
# Assumption and Pre-condition that list is sorted
def get_firstOccurrence(l,x):
    left = 0
    right = len(l) -1
    while left <= right:
        mid = (left + right)//2
        if x > l[mid]:
            left = mid + 1
        elif x < l[mid]:
            right = mid - 1
        elif x == l[mid]:
            if  mid ==0 or l[mid-1] != l[mid]:
                return mid
            else:
                right = mid - 1

    return -1


if __name__ == '__main__':
    lst = [10,10,10,4,7,20,14]
    lst.sort()
    print(lst)
    print(get_firstOccurrence(lst, 10))