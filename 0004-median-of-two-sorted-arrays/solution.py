class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)
        half = total // 2

        A, B = nums1, nums2
        if len(A) > len(B):
            A, B = B, A

        l = 0
        r = len(A) - 1

        while True:
            i = (l + r) // 2
            j = half - i - 2

            aLeft = A[i] if i >= 0 else float("-inf")
            aRight = A[i + 1] if i + 1 < len(A) else float("inf")
            bLeft = B[j] if j >= 0 else float("-inf") 
            bRight = B[j+1] if j + 1 < len(B) else float("inf")

            if aLeft <= bRight and bLeft <= aRight:
                if total % 2 == 0:
                    return (max(aLeft, bLeft) + min(aRight, bRight)) / 2
                else:
                    return min(aRight, bRight)
            elif aLeft > bRight:
                r = i - 1
            else:
                l = i + 1
            
        
