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
            aMid = (r + l) // 2
            bMid = half - aMid - 2

            aLeft = A[aMid] if aMid >= 0 else float("-inf")
            aRight = A[aMid+1] if aMid+1 < len(A) else float("inf")
            bLeft = B[bMid] if bMid >= 0 else float("-inf")
            bRight = B[bMid+1] if bMid+1 < len(B) else float("inf")
        
            # partitioning is correct
            if aLeft <= bRight and bLeft <= aRight:
                # if total size is even, the median is the average of the middle two elements
                if total % 2:
                    return min(aRight, bRight)
                # if total size is odd, then just return the middle element
                else:
                    return (max(aLeft, bLeft) + min(aRight, bRight)) / 2
            elif aLeft > bRight:
                r = aMid - 1
            else:
                l = aMid + 1 
