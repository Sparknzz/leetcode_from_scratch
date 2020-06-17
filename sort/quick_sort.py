import os

# 快速排序同样也是一种分治思想 只要有分治 那么解决方法就一定可以使用递归
# 使用递归就一定要 1. 找关系表达式(返回值)  2. 递归终止条件 

# 对于排序算法来说 子问题与父问题没有实际关系表达式 所以此类算法比较简单的递归
def quick_sort(arr, s_i, e_i):

    if e_i-s_i==0:
        return

    # 定义pivot变量
    pivot = arr[s_i]

    low_index = s_i
    high_index = e_i

    while(low_index < high_index):

        while(arr[high_index] >= pivot and high_index>0):
            high_index-=1

        arr[low_index] = arr[high_index]

        while(arr[low_index] <= pivot and low_index<high_index):
            low_index+=1
        
        arr[high_index] = arr[low_index]
        
    arr[low_index] = pivot

    quick_sort(arr, s_i, low_index)

    quick_sort(arr, low_index+1, e_i)

arr = [2, 3, 10, 4, 5, 11]

quick_sort(arr, 0, len(arr)-1)

print(arr)