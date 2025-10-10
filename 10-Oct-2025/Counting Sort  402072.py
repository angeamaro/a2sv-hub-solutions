# Problem: Counting Sort  - https://www.hackerrank.com/challenges/countingsort1/problem

def countingSort(arr):
    freq = [0] * 100
    for num in arr:
        freq[num] += 1
