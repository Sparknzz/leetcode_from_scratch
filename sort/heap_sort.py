import os

# 堆排序同样也是一种分治思想 只要有分治 那么解决方法就一定可以使用递归
# 使用递归就一定要 1. 找关系表达式(返回值)  2. 递归终止条件 

# 对于排序算法来说 子问题与父问题没有实际关系表达式 所以此类算法比较简单的递归
def heapify(arr, n, i):
    # n 是len(arr)
    # i 表示第几个节点

    l = 2*i + 1
    r = 2*i + 2
    largest = i

    if l<n and arr[largest]<arr[l]:
        largest = l

    if r<n and arr[largest]<arr[r]:
        largest = r

    # swap 
    if i != largest:
        temp = arr[i]
        arr[i] = arr[largest]
        arr[largest] = temp 

        # swap 之后要注意递归构建下面的堆 由于是跟largest位置更换  所以只需要构建largest那个位置就可以了
        heapify(arr, n, largest)

def heapSort(arr, n):

    heap_count = n//2 - 1

    # 首先要建立堆
    while heap_count>=0:
        # 自底向上建立堆
        heapify(arr, n, heap_count)
        heap_count-=1 

    # 构建完成之后 取出元素 完成排序
    n = n - 1
    while n>=0:
        # 将 第一个元素取出 然后再次构建
        temp = arr[0]
        arr[0] = arr[n]
        arr[n] = temp # 最后一个是最大的 

        heapify(arr, n, 0)

        n-=1

arr = [2, 3, 10, 4, 5, 11]

heapSort(arr, len(arr))

print(arr)