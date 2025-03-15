class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        count = 0  # Initialize count as a normal variable
        
        def merge(arr, low, mid, high):
            temp = []
            left = low
            right = mid + 1
        
            while left <= mid and right <= high:
                if arr[left] <= arr[right]:
                    temp.append(arr[left])
                    left += 1
                else:
                    temp.append(arr[right])
                    right += 1
        
            while left <= mid:
                temp.append(arr[left])
                left += 1
        
            while right <= high:
                temp.append(arr[right])
                right += 1
        
            for i in range(low, high + 1):
                arr[i] = temp[i - low]
        
        def countpairs(arr, low, mid, high):
            nonlocal count  # Access count from outer scope
            right = mid + 1
            for i in range(low, mid + 1):
                while right <= high and arr[i] > 2 * arr[right]:  # Fixed comparison
                    right += 1
                count += (right - (mid + 1))


        def merge_sort(arr, low, high):
            if low >= high:
                return
                
            mid = (low + high) // 2
            merge_sort(arr, low, mid)
            merge_sort(arr, mid + 1, high)
            countpairs(arr, low, mid, high)
            merge(arr, low, mid, high)
        
        if not nums:
            return 0
            
        arr_copy = nums.copy()
        merge_sort(arr_copy, 0, len(arr_copy) - 1)
        
        return count