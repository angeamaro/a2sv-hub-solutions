# Problem: Selection Sort - https://practice.geeksforgeeks.org/problems/selection-sort/1

class Solution: 
    def selectionSort(self, arr):
        n = len(arr)
        for i in range(n - 1):
            mini = i
            for j in range(i + 1, n):
                if arr[j] < arr[mini]:
                    mini = j
            arr[mini],arr[i] = arr[i],arr[mini]
        return arr