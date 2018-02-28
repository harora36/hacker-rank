#!/bin/python3

import sys

def maxSubarray(arr):
    n = len(arr)
    arr_sum = seq_sum = 0
    max_arr = max_seq = float('-inf')
    has_positive = False
    largest_negative = float('-inf')
    for i in range(0, n):
        if (arr[i] >= 0):
            arr_sum += arr[i]
            seq_sum += arr[i]
            has_positive = True
        else:
            if (arr_sum > max_arr):
                max_arr = arr_sum
            if (arr[i] > largest_negative):
                largest_negative = arr[i]
            arr_sum += arr[i]
        if (arr_sum < 0):
            arr_sum = 0
        if (seq_sum < 0):
            seq_sum = 0
        max_arr = arr_sum if arr_sum > max_arr else max_arr
        max_seq = seq_sum if seq_sum > max_seq else max_seq
    if has_positive:
        return max_arr, max_seq
    return largest_negative , largest_negative

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        arr = list(map(int, input().strip().split(' ')))
        result = maxSubarray(arr)
        print (" ".join(map(str, result)))


