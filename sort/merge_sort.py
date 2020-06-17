import os


def merge(arr, s_i, m, e_i):

    left_arr = arr[s_i:m+1]
    right_arr = arr[m+1:e_i+1]

    c_i = 0
    c_j = 0

    while c_i<len(left_arr) and c_j<len(right_arr):

        if left_arr[c_i] > right_arr[c_j]:
            arr[s_i] = right_arr[c_j]
            c_j+=1
        else:
            arr[s_i] = left_arr[c_i]
            c_i+=1

        s_i += 1

    while c_i < len(left_arr):
        arr[s_i] = left_arr[c_i]
        s_i += 1
        c_i += 1


    while c_j < len(right_arr):
        arr[s_i] = right_arr[c_j]
        s_i += 1
        c_j += 1


# 分治法主要需要注意的点一定是 递归的结束条件  返回值(即关系表达式) 通常来说可以直接使用全局变量 但更简洁的方式为引用变量！
def merge_sort(arr, s_i, e_i):

    if s_i < e_i:
        m = (s_i + e_i) // 2

        merge_sort(arr, s_i, m)
        merge_sort(arr, m+1, e_i)

        merge(arr, s_i, m, e_i)

arr = [2, 3, 10, 4, 5, 11]
merge_sort(arr, 0, len(arr))
print(arr)