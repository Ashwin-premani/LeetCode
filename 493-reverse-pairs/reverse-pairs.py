class Solution:
    def reversePairs(self, nums: List[int]) -> int:
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
            count = 0  
            right = mid + 1
            for i in range(low, mid + 1):
                while right <= high and arr[i] > 2 * arr[right]:  # Fixed comparison
                    right += 1
                count += (right - (mid + 1))
            return count


        def merge_sort(arr, low, high):
            count = 0
            if low >= high:
                return count
            mid = (low + high) // 2
            count += merge_sort(arr, low, mid)
            count += merge_sort(arr, mid + 1, high)
            count += countpairs(arr, low, mid, high)
            merge(arr, low, mid, high)
            return count
            
        
        if not nums:
            return 0
            
        arr_copy = nums.copy()
        return merge_sort(arr_copy, 0, len(arr_copy) - 1)