# Problem: Sort an Array - https://leetcode.com/problems/sort-an-array/description/

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergesort(arr):
            n = len(arr)
            if n > 1:
                m = n // 2
                l = arr[:m]
                r = arr[m:]

                mergesort(l)
                mergesort(r)

                i = j = k = 0
                ll,lr = len(l), len(r)
                while i < ll and j < lr:
                    if l[i] <= r[j]:
                        arr[k] = l[i]
                        i += 1
                    else:
                        arr[k] = r[j]
                        j += 1
                    k += 1
                
                while i < ll:
                    arr[k] = l[i]
                    i += 1
                    k += 1
                
                while j < lr:
                    arr[k] = r[j]
                    j += 1
                    k += 1
            return arr
        return mergesort(nums)



    
        