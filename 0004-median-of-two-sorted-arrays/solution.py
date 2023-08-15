class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)
        half = total // 2

        if total == 0:
            return 0

        A = nums1
        B = nums2
        if len(A) > len(B):
            A, B = B, A

        l = 0
        r = len(A) - 1
        while True:
            aMiddle = (r + l) // 2
            bMiddle = half - aMiddle - 2
    
            aLeft = A[aMiddle] if aMiddle >= 0 else float("-inf")
            aRight = A[aMiddle + 1] if aMiddle + 1 < len(A) else float("inf")
            bLeft = B[bMiddle] if bMiddle >= 0 else float("-inf")
            bRight = B[bMiddle + 1] if bMiddle + 1 < len(B) else float("inf")
    
            # partition is correct
            if aLeft <= bRight and bLeft <= aRight: 
                # total length is even
                if total % 2 == 0:
                    return (max(aLeft, bLeft) + min(aRight, bRight)) / 2
                else:
                    return min(aRight, bRight)
            # incorrect partition
            else:
                if aLeft > bRight:
                    r = aMiddle - 1
                else:
                    l = aMiddle + 1


