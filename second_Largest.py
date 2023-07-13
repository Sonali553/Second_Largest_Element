lst = list(map(int, input().split()))
def second_Largest(lst):
    if len(lst) <= 1:
        return -1
    maxEle = float('-inf')
    for ele in lst:
        if ele > maxEle:
            maxEle = ele
    second_max = float('-inf')
    for ele in lst:
        if ele > second_max and ele != maxEle:
            second_max = ele
    return second_max
print(second_Largest([1, 2, 3, 4, 4]))
print(second_Largest([2, 1, 2]))
print(second_Largest([2]))
print(second_Largest(lst))
