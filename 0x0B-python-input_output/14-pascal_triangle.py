#!/usr/bin/python3
def pascal_triangle(n):
    if n <= 0:
        return []
    p_tri = [[1], [1,1]]
    list = [1,1]
    prev_list = [1,1]
    for i in range(1, n):
        prev_list = list
        list = [1]
        print("i", i)
        print("len", len(prev_list))
        for j in range(1, i-1):
            list.append(prev_list[j] + prev_list[j + 1])
        print("end")
        list.append(1)
        p_tri.append(list)
    return p_tri
