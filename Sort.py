
def binary_search(x, num_list):
    num_list = sorted(num_list)
    count = 0
    print(num_list)
    left, right = 0, len(num_list) - 1
    while left <= right:
        middle = (left + right) // 2
        count += 1
        if x > num_list[middle]:
            left = middle + 1
        elif x < num_list[middle]:
            right = middle - 1
        else:
            print("count = %s" % count)
            return middle
    print("count = %s" %count)
    return -1


# l = [2,6,5,99,25,4,0,7,3]
# a = binary_search(100, l)
# print(a)

def bubble_sort(num):
    for i in range(1, len(num)):  # 排序的次数，共n-1次
        flag = True  # 设定一个标记，若为true，则表示此次循环没有进行交换，即，待排序列已经有序，排序已经完成
        for j in range(0, len(num)-i):  # j为列表下标
            if num[j] > num[j+1]:
                num[j], num[j+1] = num[j+1], num[j]
    return num

#
# l = [2,6,5,99,25,4,0,7,3]
# print(bubble_sort(l))

def insert_sort(num):
    for i in range(1, len(num)):
        j = i
        while(j > 0 and num[j] < num[j-1]):
            num[j-1], num[j] = num[j], num[j-1]
            j -= 1
    return num

l = [2,6,5,99,25,4,0,7,3,3]
print(insert_sort(l))