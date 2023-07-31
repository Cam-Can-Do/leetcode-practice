class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(A) + len(B)
        half = total // 2

        # make A the shorter array
        if len(A) > len(B):
            A, B = B, A

        # for A partitioning
        l = 0
        r = len(A) - 1

        while True:
            i = (l + r) // 2
            j = half - i - 2
    
            aLeft = A[i] if i >= 0 else float("-inf")
            bLeft = B[j] if j >= 0 else float("-inf")
            aRight = A[i+1] if i + 1 < len(A) else float("inf")
            bRight = B[j+1] if j + 1 < len(B) else float("inf")
    
            # partition is correct
            if aLeft <= bRight and bLeft <= aRight:
                if total % 2 == 0:  # total length is even
                    return (max(aLeft, bLeft) + min(aRight, bRight)) / 2
                else:
                    return min(aRight, bRight)
            elif aLeft > bRight:
                r -= 1
            else:
                l += 1
        
